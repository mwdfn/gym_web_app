from flask import Blueprint, Flask, redirect, render_template, request

from models.member import Member
import repositories.member_repository as member_repository

members_blueprint = Blueprint("members", __name__)

# Index
@members_blueprint.route("/members/")
def members():
    members = member_repository.select_all()
    return render_template("members/index.html", members=members)

# New exercise class
@members_blueprint.route("/members/new")
def new_class():
    return render_template("members/new.html")
    

# Create an exercise class
@members_blueprint.route("/members", methods=["POST"])
def create_class():
    name = request.form["name"]
    age = request.form["age"]
    gender = request.form["gender"]
    new_member = Member(name, age, gender)
    member_repository.save(new_member)
    return redirect("/members")


# Edit a member
@members_blueprint.route("/members/<id>/edit")
def edit_member(id):
    member = member_repository.select(id)
    return render_template('members/edit.html', member=member)


# Upade a member
@members_blueprint.route("/members/<id>", methods=["POST"])
def update_member(id):
    name= request.form["name"]
    age = request.form["age"]
    gender = request.form["gender"]
    member = Member(name, age, gender, id)
    member_repository.update(member)
    return redirect("/members")


# Delete a member
@members_blueprint.route("/members/<id>/delete", methods=["POST"])
def delete_member(id):
    member_repository.delete(id)
    return redirect("/members")