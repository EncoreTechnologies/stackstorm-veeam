from st2common.runners.base_action import Action

import requests
import xmltodict


class BaseAction(Action):

    def login(self, **kwargs):
        self.base_url = "{}://{}:{}/api".format(kwargs['scheme'],
                                                kwargs['server'],
                                                kwargs['port'])
        self.session = requests.Session()
        username = kwargs.get('username')
        if not username:
            username = self.config['username']
        password = kwargs.get('password')
        if not password:
            password = self.config['password']
        self.session.auth = (username, password)
        self.session.verify = kwargs['ssl_verify']

        self.post("/sessionMngr/?v=latest")
        return self.session

    def request(self, method, endpoint, payload=None):
        response = self.session.request(method,
                                        "{}{}".format(self.base_url, endpoint),
                                        json=payload)
        response.raise_for_status()
        # parse the respose from XML into a "dict"
        return xmltodict.parse(response.content)

    def post(self, endpoint, payload=None):
        return self.request("POST", endpoint, payload=payload)

    def get(self, endpoint, payload=None):
        return self.request("GET", endpoint, payload=payload)
