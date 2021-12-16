from Controller.main_controller import MainController
from flask import Response
import json
import sys
import logging


class SkillController:
    db = MainController.get_db()

# ---------------------------Skill's Functions--------------------------------------------------------
    def add_skill(self, name):
        try:
            if self.db.Skill.find_one({'name': name}) is None:
                self.db.Skill.insert_one({'name': name})
                return json.dumps({'Succeeded to add new skill': True}), 200, {'ContentType': 'application/json'}
            else:
                return json.dumps({'Skill already exists in DB': True}), 500, {'ContentType': 'application/json'}
        except Exception as e:
            # 404 - not found exc
            logging.exception(e)
            error_msg = "Oops! Failed to add skill %s occurred." % (sys.exc_info()[0])
            return json.dumps({error_msg: True}), 404, {'ContentType': 'application/json'}

    def delete_skill(self, name):
        try:
            if self.db.Skill.find_one({'name': name}) is not None:
                self.db.Skill.delete_one({'name': name})
                return json.dumps({'Succeeded to delete skill': True}), 200, {'ContentType': 'application/json'}
            else:
                return json.dumps({'Skill does not exist in DB': True}), 500, {'ContentType': 'application/json'}
        except Exception as e:
            # 404 - not found exc
            logging.exception(e)
            error_msg = "Oops! Failed to delete skill %s occurred." % (sys.exc_info()[0])
            return json.dumps({error_msg: True}), 404, {'ContentType': 'application/json'}

    def get_all_skills(self):
        try:
            skills = []
            for i in self.db.Skill.find({}):
                skills.append({'name': i['name']})
            return Response(json.dumps(skills), mimetype='application/json')
        except Exception as e:
            # 404 - not found exc
            logging.exception(e)
            error_msg = "Oops! Failed to get all skills %s occurred." % (sys.exc_info()[0])
            return json.dumps({error_msg: True}), 404, {'ContentType': 'application/json'}