from st2common.runners.base_action import Action

import requests
import xmltodict

CONFIG_OPTIONS = [
    'scheme',
    'server',
    'ssl_verify',
    'port',
    'username',
    'password',
]


class BaseAction(Action):

    def resolve_config_options(self, **kwargs):
        for opt in CONFIG_OPTIONS:
            if kwargs.get(value):
                continue

            if self.config.get(opt):
                kwargs[opt] = self.config.get(opt)
            else:
                raise ValueError("Error option needs to be specified as an"
        return kwargs

    def login(self, **kwargs):
        kwargs = self.resolve_config_options(**kwargs)
        self.base_url = "{}://{}:{}/api".format(kwargs['scheme'],
                                                kwargs['server'],
                                                kwargs['port'])
        self.session = requests.Session()
        self.session.auth = (kwargs['username'], kwargs['password'])
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
