from validate_email import validate_email

from flask import (Blueprint,request)
from flask.json import jsonify
from crud.db import get_db
from datetime import datetime

bp = Blueprint('crud', __name__)


@bp.route('/api/usuarios', methods=['GET']) 
def usuarios():
    try:    
        db, c = get_db()
        sql="SELECT id, nombre, apellido, email, fechanac FROM usuarios"
    
        c.execute(sql)
        data = c.fetchall()
        usuarios = []
        for row in data:
            print (row)
            usuario = {
                'id' : row['id'],
                'nombre' : row['nombre'],
                'apellido' : row['apellido'],
                'email' : row['email'],
                'fechanac' : row['fechanac']
            }
            usuarios.append(usuario)
        if usuarios:    
            return jsonify({"datos" : usuarios})
        else:
            return jsonify({"message" : "no existen datos"})
    except Exception as e:
        return jsonify({'Detalle Error' : e})


@bp.route('/api/agrega_usuarios/<string:nombre>/<string:apellido>/<string:email>/<string:fechaNac>', methods=['GET','POST'])
def agrega_usuarios(nombre, apellido, email, fechaNac):
    db, c = get_db()   
    if request.method == 'POST':
        try:    
            fechaNac = datetime.strptime(fechaNac, '%Y-%m-%d')

            valido = validate_email(email)
            if valido:
            
                sql="SELECT count(*) as cont FROM usuarios where  email = %s"
                c.execute(sql,(email,))
                dato = c.fetchone()
                dat=dato['cont']
                
                if dat > 0:
                    return jsonify({'message': "Email ya existe, no se puede grabar."})
                else:
                
                    sql='INSERT into usuarios (id, nombre, apellido, email, fechaNac) values (UUID(), %s, %s, %s, %s)'
                    c.execute(sql,( nombre, apellido, email, fechaNac))
                    
                    db.commit()
                    return jsonify({"message" : "Datos agregados correctamente"})        
            else:
                return jsonify({"message" : "Ingrese un email valido"})
    
        except Exception as e:
            return jsonify({'message' : 'fecha con formato erroneo, intente: YYYY-mm-dd'})


@bp.route('/api/usuario/<string:id>', methods=['GET'])
def usuario(id):
    try:    
        db, c = get_db()
        sql="SELECT id, nombre, apellido, email, fechaNac FROM usuarios  where id=%s"
        c.execute(sql,(id,))
        usuario = c.fetchone()
        
        return jsonify({"datos" : usuario})
        
    except Exception as e:
        return jsonify({'Detalle Error' : e})


@bp.route('/api/actualiza_usuario/<string:id>/<string:nombre>/<string:apellido>/<string:email>/<string:fechaNac>', methods=['PUT'])
def actualiza_usuario(id, nombre, apellido, email, fechaNac):

    if request.method == 'PUT':
        try:    
            fechaNac = datetime.strptime(fechaNac, '%Y-%m-%d')

            valido = validate_email(email)
            if valido:
                try:  
                    db, c = get_db()
                    sql='UPDATE usuarios set nombre = %s, apellido = %s, email = %s, fechaNac = %s  WHERE id=%s'
                
                    try: 
                        c.execute(sql,(nombre, apellido, email, fechaNac , id))
                        db.commit()
                    
                        return jsonify({'message' : 'Datos actualizados correctamente.'})
                    
                    except Exception as e:
                        return jsonify({'Detalle Error' : e})         

                except Exception as e:
                    return jsonify({'Detalle Error' : e})
            else:
                return jsonify({"message" : "Ingrese un email valido"})
        except Exception as e:
            return jsonify({'message' : 'fecha con formato erroneo, intente: YYYY-mm-dd'})

    
@bp.route('/api/borrar_usuario/<string:id>', methods=['DELETE'])
def borrar_usuario(id):
    if request.method == 'DELETE':
        try:
            
            db, c = get_db()
            sql='DELETE from usuarios where id = %s'
            try: 
                c.execute(sql,(id,))
                db.commit()
                
                return jsonify({'message':'Usuario fue eliminado de la base de datos'})
            
            except Exception as e:
                return jsonify({'Detalle Error' : e})
        
        except Exception as e:
             return jsonify({'Detalle Error' : e})



