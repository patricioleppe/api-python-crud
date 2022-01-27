instructions = [
    # si por alguna razon 
    # tenemos que eliminar 
    # una tabla de la base, 
    # y no nos deje por que 
    # hay ref a llaves foraneas 
    # hacer esto:
    'SET FOREIGN_KEY_CHECKS=0;',
    
    'DROP TABLE IF EXISTS usuarios;',
    
    #luego de hacer esto puedo 
    # volver a darle seguridad 
    # para que no elimine tablas 
    # con referencias de llaves 
    # foraneas 
    'SET FOREIGN_KEY_CHECKS=1;',
    # triple comillas dobles:
    # me permite generar strings 
    # de multiples lineas .
    """
       
    CREATE TABLE `usuarios` (
        `id` VARCHAR(36) NOT NULL,
        `nombre` varchar(255) DEFAULT NULL,
        `apellido` VARCHAR(50) NOT NULL,
        `email` VARCHAR(255) NOT NULL,
        `fechanac` DATETIME,
        PRIMARY KEY (`id`)
    ) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci
    
    """
] 