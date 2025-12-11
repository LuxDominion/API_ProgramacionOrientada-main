CREATE TABLE IF NOT EXISTS geos(
    id INTEGER NOT NULL AUTO_INCREMENT,
    lat FLOAT NOT NULL,
    lng FLOAT NOT NULL,

    CONSTRAINT pk_geos PRIMARY KEY (id)
);

CREATE TABLE IF NOT EXISTS addresses(
    id INTEGER NOT NULL AUTO_INCREMENT,
    street VARCHAR(100) NOT NULL,
    suite VARCHAR(50) NULL,
    city VARCHAR(50) NULL,
    zipcode VARCHAR(20) NULL,
    geoId INTEGER NULL,

    CONSTRAINT pk_addresses PRIMARY KEY (id),
    CONSTRAINT fk_addresses_geos FOREIGN KEY (geoId) REFERENCES geos(id)
);

CREATE TABLE IF NOT EXISTS companies(
    id INTEGER NOT NULL AUTO_INCREMENT,
    name VARCHAR(50) NOT NULL,
    catchPhrase VARCHAR(100) NOT NULL,
    bs VARCHAR(50) NOT NULL,

    CONSTRAINT pk_companies PRIMARY KEY (id)
);

CREATE TABLE IF NOT EXISTS users(
    id INTEGER NOT NULL AUTO_INCREMENT,
    name VARCHAR(50) NOT NULL,
    username VARCHAR(25) NOT NULL,
    email VARCHAR(255) NOT NULL,
    phone VARCHAR(25) NULL,
    website VARCHAR(255) NULL,
    addressId INTEGER NULL,
    companyId INTEGER NULL,

    CONSTRAINT pk_users PRIMARY KEY (id),
    CONSTRAINT fk_users_addresses FOREIGN KEY (addressId) REFERENCES addresses(id),    
    CONSTRAINT fk_users_companies FOREIGN KEY (companyId) REFERENCES companies(id)
);

CREATE TABLE IF NOT EXISTS posts(
    id INTEGER NOT NULL AUTO_INCREMENT,
    title VARCHAR(100) NOT NULL,
    body VARCHAR(255) NOT NULL,
    userId INTEGER NOT NULL,

    CONSTRAINT pk_posts PRIMARY KEY (id),
    CONSTRAINT fk_posts_users FOREIGN KEY (userId) REFERENCES users(id)
);

CREATE TABLE IF NOT EXISTS comments(
    id INTEGER NOT NULL AUTO_INCREMENT,
    name VARCHAR(50) NOT NULL,
    email VARCHAR(255) NOT NULL,
    body VARCHAR(255) NOT NULL,
    postId INTEGER NOT NULL,

    CONSTRAINT pk_comments PRIMARY KEY (id),
    CONSTRAINT fk_comments_posts FOREIGN KEY (postId) REFERENCES posts(id)
);