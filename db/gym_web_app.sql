DROP TABLE members;
DROP TABLE classes;


CREATE TABLE members (
    id SERIAL PRIMARY KEY,
    name VARCHAR(255)
    age INT,
    gender VARCHAR(255)
);

CREATE TABLE classes (
    id SERIAL PRIMARY KEY,
    title VARCHAR(255),
    date VARCHAR(255),
    instructor VARCHAR(255)
    start_time VARCHAR(255),
    finish VARCHAR(255)
);

e
