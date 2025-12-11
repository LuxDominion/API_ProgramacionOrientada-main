CREATE TABLE IF NOT EXISTS usuarios(
    id INTEGER NOT NULL AUTO_INCREMENT,
    nombre VARCHAR(50) NOT NULL,
    correo VARCHAR(255) NOT NULL,
    contrasena_hash VARCHAR(255) NOT NULL,
    contrasena_salt VARCHAR(255) NOT NULL,

    CONSTRAINT pk_usuarios PRIMARY KEY (id)
);
