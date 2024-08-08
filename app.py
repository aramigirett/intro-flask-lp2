from flask import Flask, render_template

app= Flask(__name__)

@app.route('/inicio')
def inicio():
    return"Hola mundo"

@app.route('/contacto')
def contacto():
    return "<h3>Introducciendo HTML desde el servidor</h3>"

@app.route('/contacto2')
def contacto2():
    return render_template('contacto.html')


# se pregunta por el proseco principal
if __name__=='__main__':
    app.run(debug=True)
