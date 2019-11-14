from bottle import Bottle, run

app = Bottle()

msg = '''
<center>
    <h1>Minha primeira página web com python</h1>
    <p> Python é uma linguagem fácil de aprender, você escreve pouco
        e é bem didática.
    </p>
    <center>
        <a href="/curso_python">Clique para acessar o curso</a>
    </cente>
</center>
'''

@app.route('/')
def index():
    return msg

@app.route('/curso_python')
def curso():
    return '<center><h1>Bem-vindo ao Curso de python</h1></center>\
            <center><a href="/">Voltar a página principal</a></center<'
run(app, host='localhost', port=8080)