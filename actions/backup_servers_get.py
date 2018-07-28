from lib.action import BaseAction


class BackupServersGet(BaseAction):

    def run(self, **kwargs):
        self.login(**kwargs)
        return self.get("/backupServers/{}".format(kwargs['id'])
