CREATE TABLE genero (
 nome VARCHAR(30) NOT NULL,
 icone VARCHAR(100),
 cor VARCHAR(10)
);

ALTER TABLE genero ADD CONSTRAINT PK_genero PRIMARY KEY (nome);


CREATE TABLE music (
 codigo INT NOT NULL,
 cantor VARCHAR(10),
 genero VARCHAR(30),
 duracao TIME(10),
 nome VARCHAR(50),
 url_imagem VARCHAR(255),
 nome_genero VARCHAR(30)
);

ALTER TABLE music ADD CONSTRAINT PK_music PRIMARY KEY (codigo);


ALTER TABLE music ADD CONSTRAINT FK_music_0 FOREIGN KEY (nome_genero) REFERENCES genero (nome);


