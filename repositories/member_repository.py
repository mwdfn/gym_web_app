from db.run_sql import run_sql
from models.exercise_class import ExerciseClass
from models.member import Member
# import repositories.exercise_class_repository as exercise_class_repository

def save(member):
    sql = "INSERT INTO members (name, age, gender) VALUES (%s, %s, %s) RETURNING id"
    values = [member.name, member.age, member.gender]
    results = run_sql(sql, values)
    id = results[0]['id']
    member.id = id


def select_all():
    members = []
    sql = "SELECT * FROM members"
    results = run_sql(sql)
    for result in results:
        member = Member(result["name"], result["age"], result["gender"])
        members.append(member)
    return members


def select(id):
    sql = "SELECT * FROM members WHERE id = %s"
    values = [id]
    result = run_sql(sql, values)[0]
    member = Member(result["name"], result["age"], result["gender"])
    return member


def delete_all():
    sql = "DELETE FROM members"
    run_sql(sql)


def delete(id):
    sql = "DELETE FROM members WHERE id = %s"
    values = [id]
    run_sql(sql, values)


def update(member):
    sql = "UPDATE members SET (name, age, gender) = (%s, %s,%s) WHERE id = %s"
    values = [member.name, member.age, member.gender, member.id]
    run_sql(sql, values)