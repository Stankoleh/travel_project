

CREATE TABLE Country (
    id INT AUTO_INCREMENT PRIMARY KEY,
    name VARCHAR(100) NOT NULL,
    continent VARCHAR(100) NOT NULL,
    rating FLOAT DEFAULT 5.0,
    active BOOLEAN DEFAULT TRUE
);

CREATE TABLE Client (
    id INT AUTO_INCREMENT PRIMARY KEY,
    name VARCHAR(100) NOT NULL,
    surname VARCHAR(100) NOT NULL,
    passport VARCHAR(20) UNIQUE NOT NULL,
    phone VARCHAR(20),
    email VARCHAR(255)
);

CREATE TABLE Contract (
    id INT AUTO_INCREMENT PRIMARY KEY,
    client_id INT NOT NULL,
    contract_number VARCHAR(50) NOT NULL,
    FOREIGN KEY (client_id) REFERENCES Client(id) ON DELETE CASCADE
);

CREATE TABLE ContactInfo (
    id INT AUTO_INCREMENT PRIMARY KEY,
    client_id INT NOT NULL,
    phone VARCHAR(20),
    email VARCHAR(255),
    FOREIGN KEY (client_id) REFERENCES Client(id) ON DELETE CASCADE
);

CREATE TABLE Residence (
    id INT AUTO_INCREMENT PRIMARY KEY,
    country_id INT NOT NULL,
    address VARCHAR(200) NOT NULL,
    stars VARCHAR(10),
    occupied BOOLEAN DEFAULT FALSE,
    FOREIGN KEY (country_id) REFERENCES Country(id) ON DELETE CASCADE
);

CREATE TABLE Transport (
    id INT AUTO_INCREMENT PRIMARY KEY,
    name VARCHAR(50) NOT NULL,
    departure_date DATE,
    arrival_date DATE,
    direction VARCHAR(20),
    status VARCHAR(20) DEFAULT 'scheduled'
);

CREATE TABLE Journey (
    id INT AUTO_INCREMENT PRIMARY KEY,
    country_id INT NOT NULL,
    client_id INT NOT NULL,
    address VARCHAR(200) NOT NULL,
    stars VARCHAR(10),
    transport VARCHAR(50),
    start_date DATE,
    end_date DATE,
    direction VARCHAR(20),
    excursions BOOLEAN DEFAULT FALSE,
    price FLOAT DEFAULT 0.0,
    FOREIGN KEY (country_id) REFERENCES Country(id) ON DELETE CASCADE,
    FOREIGN KEY (client_id) REFERENCES Client(id) ON DELETE CASCADE
);
