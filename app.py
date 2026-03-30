from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

# "Banco de dados" temporário usando uma lista
treinos = []

@app.route('/')
def index():
    # Renderiza o HTML e passa a lista de treinos para a página
    return render_template('index.html', treinos=treinos)

@app.route('/adicionar', methods=['POST'])
def adicionar_treino():
    # Captura os dados enviados pelo formulário HTML
    exercicio = request.form.get('exercicio')
    series = request.form.get('series')
    repeticoes = request.form.get('repeticoes')
    data = request.form.get('data')

    # Se todos os campos foram preenchidos, adiciona na lista
    if exercicio and series and repeticoes and data:
        treinos.append({
            'exercicio': exercicio,
            'series': series,
            'repeticoes': repeticoes,
            'data': data
        })
    
    # Redireciona de volta para a página inicial
    return redirect(url_for('index'))

if __name__ == '__main__':
    app.run(debug=True)