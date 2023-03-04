# crud-api-flask

* El desarrollo esta hecho con micro framework Flask. *
* funciona con Base de datos mysql *
  * en consola digitar *
  `flask init-db`
  * Ese comando crea la tabla usuarios en una base datos mysql
  * crear .env con datos de conexion y flask
  `FLASK_DATABASE_HOST=localhost`
  `FLASK_DATABASE_USER=root`
  `FLASK_DATABASE_PASSWORD=password`
  `FLASK_DATABASE=database`
  `FLASK_APP=crud`
  `FLASK_ENV=development`
  
* Endpoints
**Consultar todos los usuarios**
**GET**
`http://localhost:5000/api/usuario` 

**Agregar un Usuario**
**POST**
`http://localhost:5000/api/usuario`

**Obtener un usuario por su id**
**GET**
* /api/usuario/<int:id>
`http://localhost:5000/api/usuario/1`

**Actualizar un registro**
**PUT**
* /api/usuario/<int:id>
`http://localhost:5000/api/usuario/1`

**Eliminar registro**
**DELETE**
* /api/usuario/<string:id>
`http://localhost:5000/api/usuario/1`


* Para lograr validar el email ocupe validate email
`from validate_email import validate_email`
`valido = validate_email(email)`

* Para que tenga el formato correcto de fechas ocupe
`try:    `
  `fechaNac = datetime.strptime(fechaNac, '%Y-%m-%d')`  

