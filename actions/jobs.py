from lib.action import BaseAction


class Jobs(BaseAction):

    def run(self, **kwargs):
        self.login(**kwargs)
        return self.get("/jobs")
