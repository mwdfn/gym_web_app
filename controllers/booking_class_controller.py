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



















# # EDIT
# @bitings_blueprint.route("/bitings/<id>/edit")
# def edit_biting(id):
#     biting = biting_repository.select(id)
#     humans = human_repository.select_all()
#     zombies = zombie_repository.select_all()
#     return render_template('bitings/edit.html', biting=biting, humans=humans, zombies=zombies)


# # UPDATE
# @bitings_blueprint.route("/bitings/<id>", methods=["POST"])
# def update_biting(id):
#     human_id = request.form["human_id"]
#     zombie_id = request.form["zombie_id"]
#     human = human_repository.select(human_id)
#     zombie = zombie_repository.select(zombie_id)
#     biting = Biting(human, zombie, id)
#     biting_repository.update(biting)
#     return redirect("/bitings")


# # DELETE
# @bitings_blueprint.route("/bitings/<id>/delete", methods=["POST"])
# def delete_biting(id):
#     biting_repository.delete(id)
#     return redirect("/bitings")
