from flask import Flask, render_template

from controllers.member_controller import members_blueprint
from controllers.exercise_class_controller import exercise_classes_blueprint
from controllers.attending_class_controller import attending_classes_blueprint
from models.attending_class import Attending_class
from models.exercise_class import Excercise_class
from models.member import Member

app = Flask(__name__)

app.register_blueprint(members_blueprint)
app.register_blueprint(exercise_classes_blueprint)
app.register_blueprint(attending_classes_blueprint)

@app.route('/')
def home():
    return render_template('index.html')

if __name__ == '__main__':
    app.run(debug=True)


