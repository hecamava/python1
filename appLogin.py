# Se importan las librerias
from flask import Flask, render_template, request, flash, redirect, url_for, session
from flask_mysqldb import MySQL
import bcrypt  ## Esto se hace en encriptamiento OOOJJJJOOO Descrgar esto, lo hacen en 11:31 del video 

#Crea el objeto Flask
app=Flask(__name__)

#Establezco la llave secreta
app.secret_key="appLogin"

#Configura
app.config['MYSQL_HOST']='127.0.0.1'
app.config['MYSQL_USER']='root'
app.config['MYSQL_PASSWORD']='root' # pongo root por que nos dicen en el siguiente video:https://www.youtube.com/watch?v=20rj14SHlME
app.config['MYSQL_DB']='alumnotas'

#Crea el objeto MySql
mysql=MySQL(app)

# Semilla para encriptamiento
semilla= bcrypt.gensalt()

# Define la ruta principal
@app.route("/")

# Define la funcion principal
def main():  # ojo que el el video (https://www.youtube.com/watch?v=gUED5uFmyQI&list=PLkaQhEBG4ck2G7aIWge2OzqaI5iXVNTbA&index=2) dice index 
   if 'nombre' in session:
    # Carga template main.html
    return render_template('http://127.0.0.1:5000/inicio.html')
   else: 
   # Carga template main.html
    return render_template('http://127.0.0.1:5000/ingresar.html')


# Define la ruta del index

@app.route("/inicio")


# Define la funcion principal
def inicio():

  # verifica que haya sesion
  if 'nombre' in session:
    # Carga template main.html
    return render_template('inicio.html')
  else:
   # Carga template Ingresar
   return render_template('ingresar.html') 

 # Define la ruta de registro

@app.route("/registrar",methods=["GET","POST"])  

# Función para registrar

def registrar():
  if(request.method=="GET"):
        # Acceso no concedido
     # verifica que haya sesion
    if 'nombre' in session:
    # Carga template main.html
     return render_template('inicio.html')
    else:
    # Acceso no concedido
     return render_template('ingresar.html')
  else:
        #obtiene los datos
        nombre = request.form['nmNombreRegistro']
        correo = request.form['nmCorreoRegistro']
        password = request.form['nmNombrePasswordRegistro']
        password_encode = password.encode("uft-8")
        password_encriptado = bcrypt.hashpw(password_encode,semilla)
        
        #Preparar el Query para Insercion

        sQuery = "INSERT into Login(correo,password_encriptado,nombre) VALUES(%s,%s,%s)"

        # Crear cursor para ejecucion
        cur=mysql.connection.cursor()

        # Ejecuta la sentencia
        cur.execute(sQuery,(correo,password_encriptado,nombre))

        #Ejecuta el Commit
        mysql.connection.commit()

        # Registra la Sessión

        session['nombre']=nombre
        #session['correo']=correo

        # Redirige a Index
        return redirect(url_for('inicio'))

#Define la ruta de ingresar
@app.route("/registrar",methods=["GET","POST"])  
  
#Funcion para registrar

def ingresar():
      if(request.method=="GET"):
       if 'nombre' in session:
        # Carga template main.html
        # Acceso no concedido   
       
        return render_template("inicio.html") 
       else:
       # Acceso no concedido
        return render_template("ingresar.html") 
      else:   
       correo = request.form['nmCorreoLogin']
       password = request.form['nmPasswordLogin']
       password_encode = password.encode("uft-8")
     # Crea cursor para ejecución
       cur=mysql.connection.cursor()

       # Prepara el Query para consulta
       sQuery="Select correo, password, nombre FROM Login WHERE correo= %s"

       #Ejecuta la sentencia
       cur.execute(sQuery, [correo])

       # Obtengo el Dato
       usuario=cur.fetchome()

       # Cierro la consulta
       cur.close()


       #Verifica si obtuvo datos

       if(usuario != None):
         # Obtiene el password encriptado encode
         password_encriptado_encode = usuario[1].encode()
         print("Password_encode:", password_encode)
         print("Password_encriptado_encode:", password_encriptado_encode)

         # Verifica el password

         if(bcrypt.checkpw(password_encode,password_encriptado_encode)):
           #Registra la sesion
           session['nombre']=usuario[2]
         #  session['correo']=correo

           #Redirige a Index
          
           return redirect(url_for('inicio'))
         else:
            #Mensaje Flash

            flash("El password no es corecto","alert-warning")

            # Redirige a Ingresar
            return render_template('ingresar.html')
       else:

            #Mensaje Flash

            flash("El Correo no existe", "alert-warning")

            # Redirige a Ingresar
            return render_template('ingresar.html')

#Define la ruta de salida
@app.route("/salir")

#Funcion para salir

def salir():
  #limpia las sesiones
  session.clear()

  #Manda a ingresar

  return redirect(url_for('ingresar'))

  # Funcion principal

if __name__ == '__main__':
     #Ejecuta el servidor en Debug
     app.run(host='127.0.0.1',port=5002,debug=True)