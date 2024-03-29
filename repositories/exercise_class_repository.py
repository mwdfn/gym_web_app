from db.run_sql import run_sql
from models.exercise_class import ExerciseClass
from models.member import Member


def save(exercise_class):
    sql = "INSERT INTO exercise_classes (title, instructor, date, start_time, finish) VALUES (%s, %s, %s, %s, %s) RETURNING id"
    values = [exercise_class.title, exercise_class.instructor, exercise_class.date, exercise_class.start_time, exercise_class.finish]
    results = run_sql(sql, values)
    id = results[0]['id']
    exercise_class.id = id


def select_all():
    exercise_classes = []
    sql = "SELECT * FROM exercise_classes"
    results = run_sql(sql)
    for result in results:
        exercise_class = ExerciseClass(result["title"], result["instructor"], result["date"], result["start_time"], result["finish"], result["id"])
        exercise_classes.append(exercise_class)
    return exercise_classes


def select(id):
    sql = "SELECT * FROM exercise_classes WHERE id = %s"
    values = [id]
    result = run_sql(sql, values)[0]
    exercise_class = ExerciseClass(result["title"], result["instructor"], result["date"], result["start_time"], result["finish"], result["id"])
    return exercise_class


def delete_all():
    sql = "DELETE FROM exercise_classes"
    run_sql(sql)


def delete(id):
    sql = "DELETE FROM exercise_classes WHERE id = %s"
    values = [id]
    run_sql(sql, values)


def update(exercise_class):
    sql = "UPDATE exercise_classes SET (title, instructor, date, start_time, finish) = (%s, %s, %s, %s, %s) WHERE id = %s"
    values = [exercise_class.title, exercise_class.instructor, exercise_class.date, exercise_class.start_time, exercise_class.finish, exercise_class.id]
    run_sql(sql, values)


def select_bookings_in_class(id):
    bookings = []
    sql = "SELECT members.* FROM members INNER JOIN booking_classes ON booking_classes.member_id = members.id WHERE booking_classes.exercise_class_id = %s"
    values = [id]
    results = run_sql(sql, values)
    print(results)
    for result in results:
        member = Member(result["name"], result["age"], result["gender"])
        bookings.append(member)
    return bookings

