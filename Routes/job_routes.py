from Controller.job_controller import JobController
from __main__ import app
job_controller = JobController()


# ------------------Job's Routes------------------------
# Route to add new job to DB
@app.route('/add_job/', methods=['POST'])
def add_job():
    return job_controller.add_job()


# Route to delete job from DB
@app.route('/delete_job/<title>')
def delete_job(title):
    return job_controller.delete_job(title)


# Route to get all jobs from the DB
@app.route('/all_jobs')
def get_all_jobs():
    return job_controller.get_all_jobs()

