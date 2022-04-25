from flask import Blueprint, Flask, redirect, render_template, request
from models.attending_class import Attending_class
import repositories.attending_class_repository as attending_class_repository
import repositories.member_repository as member_repository
import repositories.exercise_class_repository as exercise_class_repository

attending_classes_blueprint = Blueprint("attending_classes", __name__)

