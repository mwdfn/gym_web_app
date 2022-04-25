import pdb
from models.member import Member
from models.exercise_class import Excercise_class
from models.attending_class import Attending_class

import repositories.member_repository as member_repository
import repositories.exercise_class_repository as exercise_class_repository
import repositories.attending_class_repository as attending_class_repository

attending_class_repository.delete_all()
member_repository.delete_all()
exercise_class_repository.delete_all()

member_1 = Member("Dave Smith", 23, "Male")
member_repository.save(member_1)

exercise_class_1 = Excercise_class("Body Attack", "Joe Mills", "18/05/2022", "18:00", "19:00")
exercise_class_repository.save(exercise_class_1)

attending_class_1 = Attending_class(exercise_class_1, member_1)
attending_class_repository.save(attending_class_1)


