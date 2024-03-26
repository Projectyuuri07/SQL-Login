from flask import Flask, render_template, request, redirect, url_for
import conect as conexao

app = Flask(__name__)

@app.route("/")
def homepage():
    return render_template('index.html')

@app.route("/login", methods=["POST"])
def login():
    username = request.form.get("username")
    password = request.form.get("password")
    
    # Consulta o banco de dados para verificar se o usuário e senha estão corretos
    usuarios = conexao.consultar_usuarios()
    for user in usuarios:
        if user[1] == username and user[2] == password:
            return redirect(url_for('success', username=username))
    
    # Se as credenciais estiverem incorretas, redireciona de volta para a página de login
    return redirect(url_for('failure'))

@app.route("/success/<username>")
def success(username):
    return f"<h1> Olá, {username}! Login bem-sucedido. </h1>"

@app.route("/failure")
def failure():
    return "<h1> Credenciais inválidas. Tente novamente. </h1>"

if __name__=='__main__':
    app.run(host='0.0.0.0')
