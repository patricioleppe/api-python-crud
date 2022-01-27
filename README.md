# crud-api-prueba
* El desarrollo esta hecho con micro framework Flask. *
* Lo hice con Base de datos mysql *
  * en consola digitar *
  `flask init-db`
  * Ese comando crea la tabla en una base datos mysql
  * Esta tabla crea un id varchar(36). 
  * Al momento de ser insertado el registro le paso al id esta funcion UUID()
  


* Endpoints
**Consultar todos los usuarios**
* /api/usuarios
`http://localhost:5000/api/usuarios` 

**Agregar un Usuario**
* /api/agrega_usuarios/<string:nombre>/<string:apellido>/<string:email>/<string:fechaNac>
`http://localhost:5000/api/agrega_usuarios/Roberto/Rojas/condor@gmail.com/2020-02-02`

**Obtener un usuario por su id**
* /api/usuario/<string:id>
`http://localhost:5000/api/usuario/2b7b2a34-7eb9-11ec-8925-00155df5d1ae`

**Actualizar un registro**
* /api/actualiza_usuario/<string:id>/<string:nombre>/<string:apellido>/<string:email>/<string:fechaNac>
`http://localhost:5000/api/actualiza_usuario/2b7b2a34-7eb9-11ec-8925-00155df5d1ae/Patricio/Leppe/lala@lala.cl/2020-02-02`

**Eliminar registro**
* /api/borrar_usuario/<string:id>
`http://localhost:5000/api/borrar_usuario/09c8d470-7ec0-11ec-8925-00155df5d1ae`


* Para lograr validar el email ocupe validate email
`from validate_email import validate_email`
`valido = validate_email(email)`
            `if valido:`

* Para que tenga el formato correcto de fechas ocupe

`try:    `
      `fechaNac = datetime.strptime(fechaNac, '%Y-%m-%d')`

* Las dos validaciones al pasar los datos por la url los valida y entrega un mensaje en formato json.

