from flask import Blueprint, Flask, redirect, render_template, request
from db.run_sql import run_sql

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

# Show exercise class details <<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<
@exercise_classes_blueprint.route("/exerciseclasses/<id>")
def show_exercise_class(id):
    bookings = exercise_class_repository.select_bookings_in_class(id)
    exercise_class = exercise_class_repository.select(id)
    return render_template("exerciseclasses/show_details.html", bookings=bookings, exercise_class=exercise_class)   

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


# Edit an exercise class
@exercise_classes_blueprint.route("/exerciseclasses/<id>/edit")
def edit_class(id):
    exercise_class = exercise_class_repository.select(id)
    return render_template('exerciseclasses/edit.html', exercise_class=exercise_class)


# Upade an exercise class
@exercise_classes_blueprint.route("/exerciseclasses/<id>", methods=["POST"])
def update_human(id):
    title = request.form["title"]
    instructor = request.form["instructor"]
    date = request.form["date"]
    start_time = request.form["start_time"]
    finish = request.form["finish"]
    exercise_class = ExerciseClass(title, instructor, date, start_time, finish, id)
    exercise_class_repository.update(exercise_class)
    return redirect("/exerciseclasses")


# Delete an exercise class
@exercise_classes_blueprint.route("/exerciseclasses/<id>/delete", methods=["POST"])
def delete_class(id):
    exercise_class_repository.delete(id)
    return redirect("/exerciseclasses")




