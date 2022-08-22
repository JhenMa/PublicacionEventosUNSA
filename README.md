ddd-flask-example
=================

A terse example of DDD-inspired architecture using Flask and SQLAlchemy and MongoDB as storage options.


setup.py --- Code Golf
=================

from blogex_app import Context

if __name__ == "__main__": Context.setup()

presentation.py --- Cook Book
=================

from jinja2 import Undefined
from jinja2.filters import do_mark_safe

def linebreaksp(text):
    if text is None or isinstance(text, Undefined):
        return text 
    text = "<p>" + text.replace('\n', '</p><p>') + "</p>"
    return do_mark_safe(text)

def register_filters(app):
    app.jinja_env.filters['linebreaksp'] = linebreaksp

orm_repository_base.py --- Monolithic
=================

class RepositoryBase(object):
    def __init__(self, db):
        self.db = db

    def session(self):
        return self.db.session

    def create(self, item):
        self.session().add(item)
        self.session().commit()
        
## :red_circle: Practicas de Codigo Legible
### :newspaper_roll: **Comentar y Documentar**: <br>
Se documentara cada funcion y metodo que se use en el codigo, para poder ser entendido por cualquiera que revise el codigo. <br>
```
@app.route('/validateLogin', methods = ['POST'])
def validateLogin():
    _username = request.form['inputEmail']
    _password = request.form['inputPassword']
    conn = mysql.connect()
    cursor = conn.cursor()
    cursor.callproc('validarLogin',(_username,))#Llamamos al procedimiento validarLogin de nuestra base de datos
    data = cursor.fetchall()#Obtenemos el resultado  en este caso una tabla
    if len(data)>0:#Si la tabla no esta vacia
        if str(data[0][7]) == _password:
            session['user'] = data[0][0]#asignamos dni
            if data[0][8]:
               return redirect('/userHome')
            else: 
                return redirect('/vendedorHome')
        else:
            return render_template('error.html', error='Usuario o contraseña es incorrecta')
    else:
        return render_template('error.html', error = 'Usuario no existe')
    cursor.close()
    conn.close()
```
### :newspaper_roll: **Organizar las carpetas del proyecto**: <br>
Separar lo que es el dominio, los controladores y repositorio.

![image](https://github.com/JhenMa/PublicacionEventosUNSA/blob/main/Captura%20de%20pantalla%202022-08-22%20133156.png)
### :newspaper_roll: **Identacion correspondiente**: <br>
Identar cada linea de codigo, o darle la sangria correspondiente, para tener un codigo mas ordenado y facil de comprender.<br>
```
@app.route('/signUp', methods = ['POST','GET'])
def signUp():
    _dni = request.form['inputDNI']
    _nombre = request.form['inputNombre']
    _p_apellido = request.form['inputP_Apellido']
    _s_apellido = request.form['inputS_Apellido']
    _direccion = request.form['inputDireccion']
    _telefono = request.form['inputTelefono']
    _email = request.form['inputEmail']
    _password = request.form['inputPassword']
    if _dni and _nombre and _p_apellido and _s_apellido and _direccion and _telefono and _email and _password:
        conn = mysql.connect()
        if (conn):
            print("Conexion establecida")
        else:
            print("Conexion fallida")
        cursor = conn.cursor()
        cursor.callproc('crearPersona',(_dni, _nombre, _p_apellido, _s_apellido, _direccion, _telefono, _email, _password))
        data = cursor.fetchall()
        if len(data) ==0:
            conn.commit()
            print("Usuario fue creado!")
            return json.dumps({'mensaje':'usuario fue creado!'})
        else:
            print({'error':str(data[0])})
    else:
        return json.dumps({'mensaje': 'Campos estan vacios!'})
    cursor.close()
    conn.close()
```
### :newspaper_roll: **Usar un mismo lenguaje**: <br>
Si vamos a programar con sentencias en español, para ser entendidas por cualquiera que revise el codigo, procurar hacerlo solo en ese idioma, excepto por palabras reservadas del lenguaje de programacion usado.<br>
```
CREATE TABLE persona(
	dni INT NOT NULL,
    nombres VARCHAR(30) NULL,
    p_apellido VARCHAR(30)NULL,
    s_apellido VARCHAR(30) NULL,
    direccion VARCHAR(30)NULL,
    telefono VARCHAR(30)NULL,
    usuario varchar(30) NULL, 
    contra VARCHAR(30) NOT NULL,
    PRIMARY KEY(dni)
);
```
### :newspaper_roll: **Una funcion, una tarea**: <br>
Al momento de declarar las funciones, estas solo deben de realizar una tarea en especifico, para no tener problemas si es que esque se modifica la funcion y pueda afectar a las demas.
```
# Funcion para obtener todas las actividades
def get_actividads(self):  
    ...
return data

# Funcion para agregar una actividad
def add_actividad(self, nombre, descripcion,
    fechaInicio, fechaFin, enlaceReunion, isProtocolar,
    isPonencia, isPanel, isConcurso, bases):
    ...    
return data
```
# Principios SOLID

## 1. S-Principio de Resposabilidad Única:
  Este principio tiene como objetivo separar los comportamientos para que, si surgen errores como resultado de su cambio, no         afecten otros comportamientos no relacionados.
  Un ejemplo de este principio es aplicado en la clase Lista_de_eventos en la cual unicamente se encargaa de insertar y retornar     eventos:
  
  ![Responsabilidad_Unica](https://user-images.githubusercontent.com/82920949/185822105-f5dc1f4e-9e6d-4a54-a193-c04ea91d60cf.PNG)

## 2. O-Principio de Abierto-Cerrado:
  Este principio tiene como objetivo extender el comportamiento de una Clase sin cambiar el comportamiento existente de esa Clase.   Esto es para evitar causar errores dondequiera que se use la Clase.
  Para aplicar este ejemplo todas  las clases deben descender de una clase abstracta donde se presenten todos aquellos métodos que   son la base de las respectivas clases.
  
  ![Open_Closed](https://user-images.githubusercontent.com/82920949/185822594-98e96308-56dd-46ea-9886-87dfecc9a21f.PNG)

## 3. L - Sustitución de Liskov:
  Este principio tiene como objetivo hacer cumplir la coherencia para que la Clase principal o su Clase secundaria se puedan     usar de la misma manera sin errores.
  Para aplicar este ejemplo todas  las clases que sean subtipos de una superclase , y esta misma debe incluir solo aquellos       métodos que comparten ambas subclases sin romper la lógica.
  En nuestra superclase Usuario solo contiene aquellos métodos que comparten las subclases :Ponente y Asistente , ya  que el     ponente no tiene los mismos métodos que asistente y viceversa.

    Super Clase Usuario:
  
  ![L_Usuario](https://user-images.githubusercontent.com/82920949/185823531-e695240c-3752-42ed-a028-25a33e3e57c4.PNG)
      
    Sub Clase Asistente:
  
  ![L_Asistente](https://user-images.githubusercontent.com/82920949/185823749-cdfdfdc6-368f-4caa-8d9c-eb9ed240cd06.PNG)

    Sub Clase Ponente:
    
   ![L_Ponentee](https://user-images.githubusercontent.com/82920949/185823791-6cf54861-1cd7-4f64-bf25-50f776a07483.PNG)
