from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

# "Base de dados" temporária
treinos = []
proximo_id = 1
xp_total = 0  # Sistema de pontuação

def calcular_status(xp):
    # A cada 100 XP, sobe 1 nível
    nivel = (xp // 100) + 1
    xp_atual = xp % 100
    return nivel, xp_atual

@app.route('/')
def index():
    # 1. Lógica da Barra de Pesquisa
    termo_pesquisa = request.args.get('busca', '').lower()
    
    if termo_pesquisa:
        # Filtra os treinos se houver uma pesquisa
        treinos_exibicao = [t for t in treinos if termo_pesquisa in t['exercicio'].lower()]
    else:
        treinos_exibicao = treinos

    # 2. Lógica de Nível e XP
    nivel, xp_atual = calcular_status(xp_total)
    
    return render_template('index.html', 
                           treinos=treinos_exibicao, 
                           busca=termo_pesquisa,
                           nivel=nivel, 
                           xp_atual=xp_atual, 
                           xp_total=xp_total)

@app.route('/adicionar', methods=['POST'])
def adicionar_treino():
    global proximo_id
    exercicio = request.form.get('exercicio')
    series = request.form.get('series')
    repeticoes = request.form.get('repeticoes')
    data = request.form.get('data')

    if exercicio and series and repeticoes and data:
        treinos.append({
            'id': proximo_id,
            'exercicio': exercicio,
            'series': series,
            'repeticoes': repeticoes,
            'data': data,
            'concluido': False
        })
        proximo_id += 1
    
    return redirect(url_for('index'))

@app.route('/toggle/<int:id>', methods=['POST'])
def toggle_treino(id):
    global xp_total
    for t in treinos:
        if t['id'] == id:
            if not t['concluido']:
                t['concluido'] = True
                xp_total += 25  # Ganha XP ao concluir
            else:
                t['concluido'] = False
                xp_total -= 25  # Perde XP se desmarcar
            break
    return redirect(url_for('index'))

@app.route('/deletar/<int:id>', methods=['POST'])
def deletar_treino(id):
    global treinos, xp_total
    for t in treinos:
        if t['id'] == id:
            # Se eliminar um treino já feito, remove o XP correspondente
            if t['concluido']:
                xp_total -= 25
            treinos.remove(t)
            break
    return redirect(url_for('index'))

@app.route('/editar/<int:id>', methods=['GET', 'POST'])
def editar_treino(id):
    treino = next((t for t in treinos if t['id'] == id), None)
    if not treino:
        return redirect(url_for('index'))

    if request.method == 'POST':
        treino['exercicio'] = request.form.get('exercicio')
        treino['series'] = request.form.get('series')
        treino['repeticoes'] = request.form.get('repeticoes')
        treino['data'] = request.form.get('data')
        return redirect(url_for('index'))

    return render_template('editar.html', treino=treino)

if __name__ == '__main__':
    app.run(debug=True)