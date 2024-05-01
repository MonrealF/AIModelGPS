from flask import Flask, request, render_template
import os
import pymysql
from flask_mysqldb import MySQL

app = Flask(__name__)
app.config['MYSQL_HOST'] = 'localhost'
app.config['MYSQL_USER'] = 'root'
app.config['MYSQL_PASSWORD'] = ''
app.config['MYSQL_DB'] = 'iamodel'
mysql = MySQL(app)

@app.route('/')
def Index():
    return render_template('index.html')

@app.route('/upload', methods=['POST'])
def upload_file():
    file = request.files['file']
    if file:
        filename = file.filename

        # Carpeta uploads en la app flask (host)
        file.save(os.path.join('uploads', filename))

        # Guardar la url en la base de datos
        cur = mysql.connection.cursor()
        cur.execute('INSERT INTO imagen (nombre, formato, ruta, usuarioIDUsuario) VALUES (%s, %s, %s, %s)',
                   (filename, 'jpg', f"/uploads/{filename}", 1))
        mysql.connection.commit()
        
    return render_template('index.html')

@app.route('/add_image', methods=['POST'])
def add_image():
    if request.method == 'POST':
        request

@app.route('/delete_image')
def delete_image():
    return 'delete_image'

if __name__ == '__main__':
    app.run(port = 3000, debug = True)