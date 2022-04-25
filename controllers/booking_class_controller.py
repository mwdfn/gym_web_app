from flask import Blueprint, Flask, redirect, render_template, request
from models.booking_class import BookingClass
import repositories.booking_class_repository as booking_class_repository
import repositories.member_repository as member_repository
import repositories.exercise_class_repository as exercise_class_repository

booking_classes_blueprint = Blueprint("booking_classes", __name__)

# Index
@booking_classes_blueprint.route("/bookings/")
def bookings():
    bookings = booking_class_repository.select_all()
    return render_template("bookings/index.html", bookings=bookings)

