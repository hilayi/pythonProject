from Controller.main_controller import MainController
from flask import Response, request
import json
import sys
import logging


class CandidateController:
    db = MainController.get_db()

# ---------------------------candidate's Functions--------------------------------------------------------
    def add_candidate(self):
        try:
            # a multidict containing POST data
            data = request.form
            title = data['title']
            # json.loads() method can be used to parse a valid JSON string and convert it into a Python Dictionary
            skills = json.loads(data['skills'])

            if self.db.Candidate.find_one({'title': title}) is None:
                self.db.Candidate.insert_one({'title': title, 'skills': skills})
                return json.dumps({'Succeeded to add candidate': True}), 200, {'ContentType': 'application/json'}
            else:
                return json.dumps({'Candidate already exists in DB': True}), 500, {'ContentType': 'application/json'}
        except Exception as e:
            # 404 - not found exc
            logging.exception(e)
            error_msg = "Oops! Failed to add candidate %s occurred." % (sys.exc_info()[0])
            return json.dumps({error_msg: True}), 404, {'ContentType': 'application/json'}

    def delete_candidate(self, title):
        try:
            if self.db.Candidate.find_one({'title': title}) is not None:
                self.db.Candidate.delete_one({'title': title})
                return json.dumps({'Succeeded to delete candidate': True}), 200, {'ContentType': 'application/json'}
            else:
                return json.dumps({'Candidate does not exist in DB': True}), 500, {'ContentType': 'application/json'}
        except Exception as e:
            # 404 - not found exc
            logging.exception(e)
            error_msg = "Oops! Failed to delete candidate %s occurred." % (sys.exc_info()[0])
            return json.dumps({error_msg: True}), 404, {'ContentType': 'application/json'}

    def get_all_candidates(self):
        try:
            candidates = []
            for i in self.db.Candidate.find({}):
                candidates.append({'title': i['title'], 'skills': i['skills']})
            return Response(json.dumps(candidates), mimetype='application/json')
        except Exception as e:
            # 404 - not found exc
            logging.exception(e)
            error_msg = "Oops! Failed to get all candidates %s occurred." % (sys.exc_info()[0])
            return json.dumps({error_msg: True}), 404, {'ContentType': 'application/json'}

    def candidate_finder(self, title):
        try:
            job = self.db.Job.find_one({'title': title})
            if job is None:
                return json.dumps({'Job does not exist in DB': True}), 200, {'ContentType': 'application/json'}
            else:
                job_skills = set(job['skills'])
                suitable_candidates = self.db.Candidate.find({"title": title})
                most_suitable = None
                count_skills = len(job['skills'])
                for candidate in suitable_candidates:
                    skills_diff = job_skills - set(candidate['skills'])
                    if len(skills_diff) <= count_skills:
                        most_suitable = (candidate['title'], candidate['skills'])
                        count_skills = len(skills_diff)
                if most_suitable is None:
                    return json.dumps({'Sorry, there is no candidate the suitable to job': True}), 404, {'ContentType': 'application/json'}
                else:
                    return Response(json.dumps(most_suitable), mimetype='application/json')
        except Exception as e:
            # 404 - not found exc
            logging.exception(e)
            error_msg = "Oops! Failed to find suitable candidate for job %s occurred." % (sys.exc_info()[0])
            return json.dumps({error_msg: True}), 404, {'ContentType': 'application/json'}


