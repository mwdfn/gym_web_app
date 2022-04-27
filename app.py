from flask import Flask, render_template


from controllers.member_controller import members_blueprint
from controllers.exercise_class_controller import exercise_classes_blueprint
from controllers.booking_class_controller import booking_classes_blueprint
from models.booking_class import BookingClass
from models.exercise_class import ExerciseClass
from models.member import Member

app = Flask(__name__)

app.register_blueprint(members_blueprint)
app.register_blueprint(exercise_classes_blueprint)
app.register_blueprint(booking_classes_blueprint)

@app.route('/')
def home():
    return render_template('index.html')

if __name__ == '__main__':
    app.run(debug=True)


