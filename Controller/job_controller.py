from Controller.main_controller import MainController
from flask import Response, request
import json
import sys
import logging


class JobController:
    db = MainController.get_db()

# ---------------------------Job's Functions--------------------------------------------------------
    def add_job(self):
        try:
            # a multidict containing POST data
            data = request.form
            title = data['title']
            # json.loads() method can be used to parse a valid JSON string and convert it into a Python Dictionary
            skills = json.loads(data['skills'])

            if self.db.Job.find_one({'title': title}) is None:
                self.db.Job.insert_one({'title': title, 'skills': skills})
                return json.dumps({'Succeeded to add job': True}), 200, {'ContentType': 'application/json'}
            else:
                return json.dumps({'Job already exists in DB': True}), 500, {'ContentType': 'application/json'}
        except Exception as e:
            # 404 - not found exc
            logging.exception(e)
            error_msg = "Oops! Failed to add job %s occurred." % (sys.exc_info()[0])
            return json.dumps({error_msg: True}), 404, {'ContentType': 'application/json'}

    def delete_job(self, title):
        try:
            if self.db.Job.find_one({'title': title}) is not None:
                self.db.Job.delete_one({'title': title})
                return json.dumps({'Succeeded to delete job': True}), 200, {'ContentType': 'application/json'}
            else:
                return json.dumps({'Job does not exist in DB': True}), 500, {'ContentType': 'application/json'}
        except Exception as e:
            # 404 - not found exc
            logging.exception(e)
            error_msg = "Oops! Failed to delete job %s occurred." % (sys.exc_info()[0])
            return json.dumps({error_msg: True}), 404, {'ContentType': 'application/json'}

    def get_all_jobs(self):
        try:
            jobs = []
            for i in self.db.Job.find({}):
                jobs.append({'title': i['title'], 'skills': i['skills']})
            return Response(json.dumps(jobs), mimetype='application/json')
        except Exception as e:
            # 404 - not found exc
            logging.exception(e)
            error_msg = "Oops! Failed to get all jobs %s occurred." % (sys.exc_info()[0])
            return json.dumps({error_msg: True}), 404, {'ContentType': 'application/json'}
