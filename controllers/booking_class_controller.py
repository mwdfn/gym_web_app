from flask import Blueprint, Flask, redirect, render_template, request
from models.booking_class import BookingClass
import repositories.booking_class_repository as booking_class_repository
import repositories.member_repository as member_repository
import repositories.exercise_class_repository as exercise_class_repository

booking_classes_blueprint = Blueprint("booking_classes", __name__)

