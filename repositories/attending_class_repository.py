from db.run_sql import run_sql
from models.attending_class import Attending_class
from models.member import Member
from models.exercise_class import Excercise_class
import repositories.member_repository as member_repository
import repositories.exercise_class_repository as exercise_class_repository


def save(attending_class):
    sql = "INSERT INTO attending_classes (exercise_class_id, member_id) VALUES (%s, %s) RETURNING id"
    values = [attending_class.exercise_class.id, attending_class.member.id]
    results = run_sql(sql, values)
    id = results[0]['id']
    attending_class.id = id


def select_all():
    attending_classes = []
    sql = "SELECT * FROM attending_classes"
    results = run_sql(sql)
    for result in results:
        exercise_class = exercise_class_repository.select(result["exercise_class_id"])
        member = member_repository.select(result["member_id"])
        attending_class = Attending_class(exercise_class, member, result["id"])
        attending_classes.append(attending_class)
    return attending_classes


def select(id):
    sql = "SELECT * FROM attending_classes WHERE id = %s"
    values = [id]
    result = run_sql(sql, values)[0]
    exercise_class = exercise_class_repository.select(result["exercise_class_id"])
    member = member_repository.select(result["member_id"])
    attending_class = Attending_class(exercise_class, member, result["id"])
    return attending_class


def delete_all():
    sql = "DELETE FROM attending_classes"
    run_sql(sql)


def delete(id):
    sql = "DELETE FROM attending_classes WHERE id = %s"
    values = [id]
    run_sql(sql, values)


def update(attending_class):
    sql = "UPDATE attending_classes SET (exercise_class_id, member_id) = (%s, %s) WHERE id = %s"
    values = [attending_class.exercise_class.id, attending_class.member.id, attending_class.id]
    run_sql(sql, values)