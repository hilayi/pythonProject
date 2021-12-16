from Controller.skill_controller import SkillController
from __main__ import app
skill_controller = SkillController()


# ------------------Skill's Routes------------------------
# Route to add new skill to DB
@app.route('/add_skill/<name>')
def add_skill(name):
    return skill_controller.add_skill(name)


# Route to delete skill from DB
@app.route('/delete_skill/<name>')
def delete_skill(name):
    return skill_controller.delete_skill(name)


# Route to get all skills from the DB
@app.route('/all_skills')
def get_all_skills():
    return skill_controller.get_all_skills()

