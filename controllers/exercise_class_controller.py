from flask import Blueprint, Flask, redirect, render_template, request

from models.exercise_class import ExerciseClass
import repositories.exercise_class_repository as exercise_class_repository

exercise_classes_blueprint = Blueprint("exercise_classes", __name__)


@exercise_classes_blueprint.route("/exercise-classes")
def exercise_classes():
    exercise_classes = exercise_class_repository.select_all()
    return render_template("exercise-classes/index.html", exercise_classes=exercise_classes)

