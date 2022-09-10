from flask import Flask, render_template

app = Flask(__name__)


# toda pagina flasks, precisa de um
# route  - > que é pagina inicial e também uma é um caminho depois do seu domínio  dominio.com"/index"
@app.route(
    '/')  # 'app' nome do site para o flask /  @app é um decorator (linha codigo que atribui uma nova funcionalidade para o def)
# função - > o que você quer exibir naquela página
def homepage():  # put application's code here # def nome da função
    # uma função 'def' precisa retornar uma resposta   ' return'
    return render_template('homepage.html')

# templates para paginas html


@app.route('/contatos')
def contatos():
    return render_template('contatos.html')

# o if abaixo diz que vai rodar tudo que estiver na linha de codigo se ele fo rodado diretamente,
# mas se ele for importado não será rodado o que estiver dentro


@app.route('/usuarios/<nome_usuario>')
def usuarios(nome_usuario):
    return render_template('usuarios.html', nome_usuario=nome_usuario)

if __name__ == '__main__':
    app.run(debug=True)
