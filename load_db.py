import pdb
from models.member import Member
from models.exercise_class import ExerciseClass
from models.booking_class import BookingClass

import repositories.member_repository as member_repository
import repositories.exercise_class_repository as exercise_class_repository
import repositories.booking_class_repository as booking_class_repository

booking_class_repository.delete_all()
member_repository.delete_all()
exercise_class_repository.delete_all()

member_1 = Member("Dave Smith", 23, "Male")
member_repository.save(member_1)

member_2 = Member("Sarah Smith", 24, "Female")
member_repository.save(member_2)

member_3 = Member("Mark Jones", 28, "Male")
member_repository.save(member_3)

member_4 = Member("Tina Davies", 61, "Female")
member_repository.save(member_4)

member_5 = Member("Sam Williams", 42, "Male")
member_repository.save(member_5)

member_6 = Member("Shani Michael", 36, "Female")
member_repository.save(member_6)

member_7 = Member("Alivia Williams", 61, "Female")
member_repository.save(member_7)

member_8 = Member("Tina Davies", 50, "Female")
member_repository.save(member_8)

member_9 = Member("Merryn Blaese", 21, "Female")
member_repository.save(member_9)

member_10 = Member("Malcolm Franklin", 33, "Male")
member_repository.save(member_10)

member_11 = Member("Frederic Duffy", 25, "Female")
member_repository.save(member_11)

exercise_class_1 = ExerciseClass("Body Attack", "Joe Mills", "18/05/2022", "18:00", "19:00")
exercise_class_repository.save(exercise_class_1)

exercise_class_2 = ExerciseClass("Body Balance", "Trevor Andrews", "10/05/2022", "17:00", "18:00")
exercise_class_repository.save(exercise_class_2)

exercise_class_3 = ExerciseClass("Cross Fit", "Magda Pas", "14/05/2022", "19:00", "21:00")
exercise_class_repository.save(exercise_class_3)

booking_class_1 = BookingClass(exercise_class_1, member_1)
booking_class_repository.save(booking_class_1)

booking_class_2 = BookingClass(exercise_class_2, member_2)
booking_class_repository.save(booking_class_2)

booking_class_3 = BookingClass(exercise_class_3, member_3)
booking_class_repository.save(booking_class_3)




