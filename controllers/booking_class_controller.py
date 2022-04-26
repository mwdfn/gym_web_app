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


# New booking
@booking_classes_blueprint.route("/bookings/new")
def new_booking():
    exercise_classes = exercise_class_repository.select_all()
    members = member_repository.select_all()
    print(exercise_classes)
    return render_template("bookings/new.html", exercise_classes=exercise_classes, members=members)


# Create a booking
@booking_classes_blueprint.route("/bookings", methods=["POST"])
def create_booking():
    exercise_class_id = request.form["exercise_class_id"]
    member_id = request.form["member_id"]
    exercise_class = exercise_class_repository.select(exercise_class_id)
    member = member_repository.select(member_id)
    new_booking = BookingClass(exercise_class, member)
    booking_class_repository.save(new_booking)
    return redirect("/bookings")


# Edit a booking
@booking_classes_blueprint.route("/bookings/<id>/edit")
def edit_booking(id):
    booking = booking_class_repository.select(id)
    members = member_repository.select_all()
    exercise_classes = exercise_class_repository.select_all()
    return render_template('bookings/edit.html', booking=booking, members=members, exercise_classes=exercise_classes)


# Update a booking
@booking_classes_blueprint.route("/bookings/<id>", methods=["POST"])
def update_booking(id):
    member_id = request.form["member_id"]
    exercise_class_id = request.form["exercise_class_id"]
    member = member_repository.select(member_id)
    exercise_class = exercise_class_repository.select(exercise_class_id)
    booking = BookingClass(exercise_class, member, id)
    booking_class_repository.update(booking)
    return redirect("/bookings")


# Delete a booking
@booking_classes_blueprint.route("/bookings/<id>/delete", methods=["POST"])
def delete_booking(id):
    booking_class_repository.delete(id)
    return redirect("/bookings")
