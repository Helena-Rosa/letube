
CREATE DATABASE IF NOT EXISTS lenamusic;

USE lenamusic;


CREATE TABLE IF NOT EXISTS genero (
 nome VARCHAR(30) NOT NULL PRIMARY KEY,
 icone VARCHAR(100),
 cor VARCHAR(10)
);




CREATE TABLE IF NOT EXISTS music (
 codigo INT NOT NULL PRIMARY KEY AUTO_INCREMENT,
 cantor VARCHAR(30),
 genero VARCHAR(30),
 duracao TIME,
 nome VARCHAR(50),
 url_imagem VARCHAR(255),
 nome_genero VARCHAR(30),
 CONSTRAINT fk_music FOREIGN KEY (nome_genero) REFERENCES genero(nome)
);


