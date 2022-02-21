-- mysql -u root

CREATE DATABASE curso;

USE curso;

SHOW TABLES;

CREATE TABLE zapatos(
	id INT(11) NOT NULL AUTO_INCREMENT,
	marca VARCHAR(50) NOT NULL,
	tipo_zapato VARCHAR(50) NOT NULL,
	color VARCHAR(50) NOT NULL,
	talla float NOT NULL,

	PRIMARY KEY (id)
);

SELECT * FROM zapatos;

-- Un solo Valor

INSERT INTO zapatos (marca, tipo_zapato, color, talla) VALUES
('Nike','Tenis','Rojo','7.5');

-- Varios Valores

INSERT INTO zapatos (marca, tipo_zapato, color, talla) VALUES
('Nike','Tenis','Rojo','7.5'),
('Flexi','Vestir','Negro','8'),
('Cklass','Tacon','Plata','3');


-- Proxima interaccion: 

-- INSERTS
