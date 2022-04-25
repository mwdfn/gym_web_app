from flask import Blueprint, Flask, redirect, render_template, request

from models.exercise_class import ExerciseClass

exercise_classes_blueprint = Blueprint("exercise_classes", __name__)


