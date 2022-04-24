from flask import Blueprint, Flask, redirect, render_template, request

from models.exercise_class import Excercise_class

exercise_classes_blueprint = Blueprint("exerceise_classes", __name__)


