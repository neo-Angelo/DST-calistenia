from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

# "Banco de dados" temporário e um contador para criar IDs únicos
treinos = []
proximo_id = 1

@app.route('/')
def index():
    return render_template('index.html', treinos=treinos)

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
            'concluido': False # Todo treino novo entra como pendente
        })
        proximo_id += 1
    
    return redirect(url_for('index'))

@app.route('/toggle/<int:id>', methods=['POST'])
def toggle_treino(id):
    # Inverte o status de concluído/pendente
    for t in treinos:
        if t['id'] == id:
            t['concluido'] = not t['concluido']
            break
    return redirect(url_for('index'))

@app.route('/deletar/<int:id>', methods=['POST'])
def deletar_treino(id):
    global treinos
    # Recria a lista ignorando o ID que queremos deletar
    treinos = [t for t in treinos if t['id'] != id]
    return redirect(url_for('index'))

@app.route('/editar/<int:id>', methods=['GET', 'POST'])
def editar_treino(id):
    # Busca o treino pelo ID
    treino = next((t for t in treinos if t['id'] == id), None)
    if not treino:
        return redirect(url_for('index'))

    # Se for POST, salva as alterações
    if request.method == 'POST':
        treino['exercicio'] = request.form.get('exercicio')
        treino['series'] = request.form.get('series')
        treino['repeticoes'] = request.form.get('repeticoes')
        treino['data'] = request.form.get('data')
        return redirect(url_for('index'))

    # Se for GET, mostra a tela de edição
    return render_template('editar.html', treino=treino)

if __name__ == '__main__':
    app.run(debug=True)