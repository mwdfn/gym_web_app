from db.run_sql import run_sql
from models.booking_class import BookingClass
from models.member import Member
from models.exercise_class import ExerciseClass
import repositories.member_repository as member_repository
import repositories.exercise_class_repository as exercise_class_repository


def save(booking_class):
    sql = "INSERT INTO booking_classes (exercise_class_id, member_id) VALUES (%s, %s) RETURNING id"
    values = [booking_class.exercise_class.id, booking_class.member.id]
    results = run_sql(sql, values)
    id = results[0]['id']
    booking_class.id = id


def select_all():
    booking_classes = []
    sql = "SELECT * FROM booking_classes"
    results = run_sql(sql)
    for result in results:
        exercise_class = exercise_class_repository.select(result["exercise_class_id"])
        member = member_repository.select(result["member_id"])
        booking_class = BookingClass(exercise_class, member, result["id"])
        booking_classes.append(booking_class)
    return booking_classes


def select(id):
    sql = "SELECT * FROM booking_classes WHERE id = %s"
    values = [id]
    result = run_sql(sql, values)[0]
    exercise_class = exercise_class_repository.select(result["exercise_class_id"])
    member = member_repository.select(result["member_id"])
    booking_class = BookingClass(exercise_class, member, result["id"])
    return booking_class


def delete_all():
    sql = "DELETE FROM booking_classes"
    run_sql(sql)


def delete(id):
    sql = "DELETE FROM booking_classes WHERE id = %s"
    values = [id]
    run_sql(sql, values)


def update(booking_class):
    sql = "UPDATE booking_classes SET (exercise_class_id, member_id) = (%s, %s) WHERE id = %s"
    values = [booking_class.exercise_class.id, booking_class.member.id, booking_class.id]
    run_sql(sql, values)