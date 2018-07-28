from lib.action import BaseAction


class JobsGet(BaseAction):

    def run(self, **kwargs):
        self.login(**kwargs)
        return self.get("/jobs/{}".format(kwargs['id']))
