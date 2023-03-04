from validate_email import validate_email
from flask import (Blueprint,request)
from flask.json import jsonify
from .db import get_db
from datetime import datetime

bp = Blueprint('crud', __name__)


@bp.route('/api/usuario', methods=['GET']) 
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



@bp.route('/api/usuario', methods=['POST'])
def agrega_usuarios():
    
    if request.method == 'POST':
        try:    
            db, c = get_db()   
            data = request.get_json()
            nombre = data['nombre']
            apellido = data['apellido']
            email = data['email']
            fechaNac = data['fechaNac']
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
                
                    sql='INSERT into usuarios ( nombre, apellido, email, fechaNac) values ( %s, %s, %s, %s)'
                    c.execute(sql,( nombre, apellido, email, fechaNac))
                    
                    db.commit()
                    return jsonify({"message" : "Datos agregados correctamente"})        
            else:
                return jsonify({"message" : "Ingrese un email valido"})
    
        except Exception as e:
            return jsonify({'message' : 'Ocurrio un error'})


@bp.route('/api/usuario/<int:id>', methods=['GET'])
def usuario(id):
    if request.method == "GET":
        try:    
            db, c = get_db()
            sql="SELECT count(*) as cont FROM usuarios where id = %s"
            c.execute(sql,(id,))
            dato = c.fetchone()
            dat=dato['cont']
            
            if dat > 0:
                sql="SELECT id, nombre, apellido, email, fechaNac FROM usuarios  where id=%s"
                c.execute(sql,(id,))
                usuario = c.fetchone()
                
                return jsonify({"datos" : usuario})
            else:
                return jsonify({'message' : 'Usuario no existe en la base de datos'})
            
        except Exception as e:
            return jsonify({'Detalle Error' : e})


@bp.route('/api/usuario/<int:id>', methods=['PUT'])
def actualiza_usuario(id):

    if request.method == 'PUT':
        data = request.get_json()
        nombre = data['nombre']
        apellido = data['apellido']
        email = data['email']
        fechaNac = data['fechaNac']
        try:    
            fechaNac = datetime.strptime(fechaNac, '%Y-%m-%d')
            valido = validate_email(email)
            if valido:
                try:  
                    db, c = get_db()
                    sql="SELECT count(*) as cont FROM usuarios where id = %s"
                    c.execute(sql,(id,))
                    dato = c.fetchone()
                    dat=dato['cont']
                    
                    if dat > 0:
                        sql='UPDATE usuarios set nombre = %s, apellido = %s, email = %s, fechaNac = %s  WHERE id=%s'
                    
                        try: 
                            c.execute(sql,(nombre, apellido, email, fechaNac , id))
                            db.commit()
                        
                            return jsonify({'message' : 'Datos actualizados correctamente.'})
                        
                        except Exception as e:
                            return jsonify({'Detalle Error' : e}) 
                    else:
                        return jsonify({'message' : "Usuario no se puede actualizar porque no existe en la base de datos."})

                except Exception as e:
                    return jsonify({'Detalle Error' : e})
            else:
                return jsonify({"message" : "Ingrese un email valido"})
        except Exception as e:
            return jsonify({'message' : 'Ocurrio un error'})

    
@bp.route('/api/usuario/<int:id>', methods=['DELETE'])
def borrar_usuario(id):
    if request.method == 'DELETE':
        try:
            db, c = get_db()
            sql="SELECT count(*) as cont FROM usuarios where id = %s"
            try:
                c.execute(sql,(id,))
                dato = c.fetchone()
                dat=dato['cont']
                
                if dat > 0:
            
                    sql='DELETE from usuarios where id = %s'
                    try: 
                        c.execute(sql,(id,))
                        db.commit()
                        return jsonify({'message':'Usuario fue eliminado de la base de datos'})
                    except Exception as e:
                        return jsonify({'Error' : e})
                else:
                    return jsonify({'message' : "Usuario no se puede eliminar porque no existe en la base de datos."})

            except Exception as e:
                return jsonify({'Error' : e})        
        except Exception as e:
            return jsonify({'Error' : e})



