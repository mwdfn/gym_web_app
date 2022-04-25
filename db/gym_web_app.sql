DROP TABLE members;
DROP TABLE classes;
DROP TABLE attending_classes;


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
    exercise_class_id SERIAL REFERENCES exercise_classes(id),
    member_id SERIAL REFERENCES members(id)
);
