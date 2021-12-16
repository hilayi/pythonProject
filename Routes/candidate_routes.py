from Controller.candidate_controller import CandidateController
from __main__ import app
candidate_controller = CandidateController()


# ------------------Candidate's Routes------------------------
# Route to add new candidate to DB
@app.route('/add_candidate/', methods=['POST'])
def add_candidate():
    return candidate_controller.add_candidate()


# Route to delete candidate from DB
@app.route('/delete_candidate/<title>')
def delete_candidate(title):
    return candidate_controller.delete_candidate(title)


# Route to get all candidates from the DB
@app.route('/all_candidates')
def get_all_candidates():
    return candidate_controller.get_all_candidates()


# Route to get the most suitable candidate for job
@app.route('/candidate_finder/<title>')
def candidate_finder(title):
    return candidate_controller.candidate_finder(title)
