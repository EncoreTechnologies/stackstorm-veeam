from lib.action import BaseAction


class BackupServersList(BaseAction):

    def run(self, **kwargs):
        self.login(**kwargs)
        return self.get("/backupServers")
