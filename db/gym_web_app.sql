DROP TABLE booking_classes;
DROP TABLE exercise_classes;
DROP TABLE members;

CREATE TABLE members (
    id SERIAL PRIMARY KEY,
    name VARCHAR(255),
    age INT,
    gender VARCHAR(255) 
);

CREATE TABLE exercise_classes (
    id SERIAL PRIMARY KEY,
    title VARCHAR(255),
    instructor VARCHAR(255),
    date VARCHAR(255),
    start_time VARCHAR(255),
    finish VARCHAR(255)
);

CREATE TABLE booking_classes (
    id SERIAL PRIMARY KEY,
    exercise_class_id SERIAL REFERENCES exercise_classes(id) ON DELETE CASCADE,
    member_id SERIAL REFERENCES members(id) ON DELETE CASCADE
);
