from flask import Flask, render_template, request, redirect, url_for, flash  # render_template es para redireccionar a plantillas
from flask_mysqldb import MySQL #Para manejar la base de datos MySql


app = Flask(__name__)
#para ejecutar el Mysql
# para que no nos muestre errores, como dicen en el siguiente video:https://www.youtube.com/watch?v=20rj14SHlME
app.secret_key="ebcqaeyzfqtgtal"

#mysql connection:
#app.config['MYSQL_HOST']='127.0.0.1:3306'
app.config['MYSQL_HOST']='127.0.0.1'
app.config['MYSQL_USER']='root'
app.config['MYSQL_PASSWORD']='root' # pongo root por que nos dicen en el siguiente video:https://www.youtube.com/watch?v=20rj14SHlME
app.config['MYSQL_DB']='alumnotas'
mysql=MySQL(app)

#settings
app.secret_key='mysecretkey'  #como va protegida nuestra sesion

@app.route('/') #cada vez que un usuario inicie en la ruta principal, retornamos peticion a la ruta mediante:
def Index():
 return 'Hola Mundo'   # Aqui es  por que aparece el pantayaso inicial Hola Mundo


 # Agregamos el medallero:
@app.route('/add_insertmedal')
def add_insertmedal():
   cur=mysql.connection.cursor()
   cur.execute('SELECT * FROM olimpicos')
   data=cur.fetchall()
  # print(data), se quita por que ya no lo necesitamos
   return render_template ('insertmedal.html', olimpicos=data )  # no es necrsario ponerle el nombre de la carpeta eso lo asume automaticamente


@app.route('/index2')
def index2():
      return render_template ('index2.html')  # no es necrsario ponerle el nombre de la carpeta eso lo asume automaticamente


@app.route('/insertmedal', methods=['POST'])
def insertmedal():
 if request.method == 'POST':
  Pais = request.form['Pais']
  Oro = request.form['Oro']
  Plata = request.form['Plata']
  Bronce = request.form['Bronce'] 
  #print(Pais) 
  #print(Oro)
  #print(Plata) 
  #print(Bronce)
  # como ya vimos que nos imprimio mediante print, ahora haremos el cursor para mysql
  
  cur=mysql.connection.cursor()
  cur.execute('INSERT INTO olimpicos(Pais,Oro,Plata,Bronce) VALUES(%s,%s,%s,%s)',(Pais,Oro,Plata,Bronce))
  # esta linea de commit es decir, realizamos la conexion, escribimos la consulta, ejecutamos la consulta, e insertamos los datos
  mysql.connection.commit()
 flash('Contacto adicionado satisfactoriamente')
 return redirect(url_for('insertmedal'))



@app.route('/edit_insertmedal/<Pais>')   
#def edit_insertmedal():   
def get_insertmedal(Pais):
 #  return 'edit insertmedal'
 cur=mysql.connection.cursor()
 cur.excute('SELECT * FROM olimpicos WHERE Pais=%s',(Pais)) 
 data=cur.fetchall()   # para hacer un arreglo de un solo registro
 return render_template('edit-olimpicos1.html',insertmedal=data[0])
 
@app.route('/updatemedal/<Pais>', methods=['POST'])
def updatemedal_contact(Pais):
 if request.method=='POST':
  Pais=request.form['Pais'] 
  Oro=request.form['Oro'] 
  Plata=request.form['Plata'] 
  Bronce=request.form['Bronce'] 
  cur=mysql.connection.cursor()
 # en python no hay problema de comillas, hacemos """", por que el update
 # es grande 
 cur.excute("""
 UPDATE olimpicos SET Pais = %s, Oro= %s,  Plata=%s, Bronce = %s
 WHERE Pais = %s             
 """, (Pais, Oro,Plata,Bronce)) # Dudas con el Pais, en 57:33 del video manejan id como un pivovte. 
 mysql.connection.commit()
 flash('Registro actualizado satisfactoriamente')
 return redirect(url_for('insertmedal')) 



 #print(data[0])
 #return 'recibido'
@app.route('/delete_insertmedal/<string:Pais>')   
def delete_insertmedal(Pais):
   cur=mysql.connection.cursor()
   cur.execute('DELETE FROM olimpicos Where Pais= {0}'.format(Pais))
   mysql.connection.commit()
   flash('Pais Removido Satisfacoriamente')
   return redirect(url_for('insertmedal'))

if __name__ == '__main__':  # si el archivo que arranca todo es insertarinfo.py, entonces:
 app.run(port=3000, debug=True)   # utilizamos puerto 3000, debug es que cuando hacemos cambio en el servidor estos reinician automaticamente
 # de las linea de código 1 al 5 es para iniciar el servidor.

