from flask import Flask, render_template
import os
import database as db #acá importé el archivo de de baso de datos para poder trabajar en él


#ESTRUCTURA PARA LANZAR NUESTRA APLICACION A TRAVES DE UN PUERTO CON EL MODULO FLASK
#para acceder al archivo o la carpeta del proyecto
template_dir = os.path.dirname(os.path.abspath(os.path.dirname(__file__)))
#unir src y template a la carpeta del proyecto
template_dir = os.path.join(template_dir, 'src', 'template')

#inicializacion de Flask para que busque el index html y lo inicialize
app = Flask(__name__, template_folder= template_dir)


#Rutas de la aplicación
@app.route('/') #se coloca '/' para que con el mismo nombre de la aplicacion vayamos a ese index de html.
# esto se hace a traves de una funcion (la llame home porque me hace referencia a lo pincipal)
def home():
    return render_template('index.html')


if __name__ == '__main__':
    app.run(debug=True, port=4000)
#FIN



