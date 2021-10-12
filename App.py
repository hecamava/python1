from flask import Flask, render_template,request,redirect,url_for, flash, request
from flask_mysqldb import MySQL
from werkzeug.datastructures import RequestCacheControl


app=Flask(__name__)

#Conexion a base de datos con los siguientes datos
app.config['MYSQL_HOST']='127.0.0.1' # 127.0.0.1:3306
app.config['MYSQL_USER']='root'
app.config['MYSQL_PASSWORD']='root' # pongo root por que nos dicen en el siguiente video:https://www.youtube.com/watch?v=20rj14SHlME  root
app.config['MYSQL_DB']='alumnotas'

mysql=MySQL(app)

#Configuraciones
app.secret_key='mysecretkey'

#La siguiente es indicar que cada vez que un usuario entre a nuestra ruta principal de nuestra aplicacion, vamos a

@app.route('/')  
def inicio2():
    cur=mysql.connection.cursor()
    cur.execute('Select * from olimpicos')
    data= cur.fetchall()
    return render_template('inicio2.html', contacts=data) 
#Creacion de otra ruta para agregar paises,,,,,  @app.route es para la creacion de rutas 
@app.route('/add_olimpicos',methods=['POST'])
def add_olimpicos():
#def - se define una funcion que retorna inicialmnete un texto
    if request.method == 'POST':
        Oro= request.form['Oro']
        Plata= request.form['Plata']
        Bronce=request.form['Bronce']
        cur= mysql.connection.cursor()
        cur.execute('INSERT INTO olimpicos(Pais,Oro,Plata,Bronce) VALUES(%s,%s,%s)',(Oro,Plata,Bronce))
        mysql.connection.commit()
        flash('Medallero agregado correctamente')
        return redirect(url_for('add_olimpicos'))
        return render_template('inicio2.html', contacts=data)  # 8 de Octubre 2021
        
@app.route('/Editar/<Pais>')
def get_olimpicos(Pais):
    cur= mysql.connection.cursor()
    cur.execute('Select * from olimpicos where Pais=%s',(Pais))
    data=cur.fetchall()
    return render_template('edit-olimpicos2.html', contact=data[0])

@app.route('/update/<Pais>', methods = ['POST'])   
def update_olimpicos(Pais):
    if request.method=='POST':
        Oro= request.form['Oro']
        Plata= request.form['Plata']
        Bronce=request.form['Bronce']
        cur= mysql.connection.cursor()
        cur.execute("""
            UPDATE olimpicos
            SET Oro = %s,
                Plata = %s,
                Bronce = %s
            WHERE Pais = %s     
        """,(Oro,Plata,Bronce,Pais))
        mysql.connection.commit()
        flash('Medalleria de pais Actualizado')
        return redirect(url_for('inicio2.html'))
        return render_template('inicio2.html', contacts=data)  # 8 de Octubre 2021

    @app.route('/Borrar/<string:Pais>')
    def delete_Olimpicos(Pais):
            cur = mysql.connection.cursor()
            cur.execute('DELETE FROM Olimpicos WHERE Pais = {0}'.format(Pais))
            mysql.connection.commit()
            flash('Pais borrado satisfactoriamente')
            return redirect(url_for('inicio2.html'))

            return render_template('inicio2.html',contacts=data)  # 8 de Octubre 2021 

# Llamar el puerto y con debug los cambios que se hagan en el servidor los reinicia automaticamente
if __name__=='__main__':
    app.run(port=3000,debug=True)
 #Lineas anteriores son para iniciar un servidor   