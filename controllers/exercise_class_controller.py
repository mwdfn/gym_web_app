from flask import Blueprint, Flask, redirect, render_template, request

from models.exercise_class import ExerciseClass
import repositories.exercise_class_repository as exercise_class_repository

exercise_classes_blueprint = Blueprint("exercise_classes", __name__)

# Index
@exercise_classes_blueprint.route("/exerciseclasses/")
def exercise_classes():
    exercise_classes = exercise_class_repository.select_all()
    return render_template("exerciseclasses/index.html", exercise_classes=exercise_classes)

# New exercise class
@exercise_classes_blueprint.route("/exerciseclasses/new")
def new_class():
    return render_template("exerciseclasses/new.html")
    

# Create an exercise class
@exercise_classes_blueprint.route("/exerciseclasses", methods=["POST"])
def create_class():
    title = request.form["title"]
    instructor = request.form["instructor"]
    date = request.form["date"]
    start_time = request.form["start_time"]
    finish = request.form["finish"]
    new_class = ExerciseClass(title, instructor, date, start_time, finish)
    exercise_class_repository.save(new_class)
    return redirect("/exerciseclasses")


# # EDIT
# @humans_blueprint.route("/humans/<id>/edit")
# def edit_human(id):
#     human = human_repository.select(id)
#     return render_template('humans/edit.html', human=human)


# # UPDATE
# @humans_blueprint.route("/humans/<id>", methods=["POST"])
# def update_human(id):
#     name = request.form["name"]
#     human = Human(name, id)
#     human_repository.update(human)
#     return redirect("/humans")


# # DELETE
# @humans_blueprint.route("/humans/<id>/delete", methods=["POST"])
# def delete_human(id):
#     human_repository.delete(id)
#     return redirect("/humans")