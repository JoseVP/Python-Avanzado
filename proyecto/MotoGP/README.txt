Proyecto de Jose María Valenzuela Perez para el curso de Programacion Avanzada en Python
---------------------------------------------------------------------------------------

EJECUCION DEL PROGRAMA: python motogp_app.py

---------------------------------------------------------------------------------------

Esta aplicacion en python consiste en un scrapper que obtiene informacion
de los circuitos del campeonato actual de MotoGP asi como de los records
de cada circuito de la pagina oficial de MotoGP "www.motogp.com"

Esta informacion se muestra mediante una ventana de forma clara y sencilla



Para la ejecución de este programa es indispensable tener instalado
el framework scrapy (se puede obtener ejecutando "sudo easy_install scrapy")

Tambien es necesario crear una base de datos Mysql mediante los siguientes comandos

    CREATE DATABASE MotogpDB charset utf8;

    GRANT ALL ON MotogpDB.* TO 'admin'@'localhost' IDENTIFIED BY 'motogpadmin';
    
No es necesario crear las tablas puesto que el programa ya lo comprueba y las crea
si no estan creadas.

Si se desean crear manualmente se pueden hacer usando estos comandos:
    
    CREATE TABLE circuitos (id int(10) auto_increment primary key, 
                        gran_premio varchar(100) not null, 
                        nombre varchar(100) not null,
                        longitud varchar(100),
                        anchura varchar(100),
                        curvas_der int(2),
                        curvas_izq int(2),
                        recta_larga varchar(100),
                        fecha_construccion varchar(100),
                        fecha_modificacion varchar(100))ENGINE=INNODB;
                        
                        
    CREATE TABLE records_circuitos (id int(10) auto_increment primary key,
                                id_circuito int(10) not null,
                                categoria varchar(100) not null,
                                record varchar(100) not null,
                                temporada int(4) not null,
                                piloto varchar(100) not null,
                                motocicleta varchar(100),
                                tiempo varchar(100),
                                velocidad varchar(100),
                                foreign key (id_circuito) references circuitos(id) on delete cascade
                                )ENGINE=INNODB;