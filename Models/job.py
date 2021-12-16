import Utils


class Job:
    # constructor
    def __init__(self, title, skills):
        self.title = title
        Utils.addSkills(self, skills)

