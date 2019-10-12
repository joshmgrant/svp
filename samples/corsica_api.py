from svp.api_object import API
from svp.api_object import APIResponse


class CorsicaAPI(API):

    def __init__(self):
        super().__init__("https://corsica-api-project.herokuapp.com/corsica")

    def default_normal(self):
        endpoint = "/normal"

        return self.get(endpoint)

    def default_exponential(self):
        endpoint = "/exponential"

        return self.get(endpoint)

    def default_uniform(self):
        endpoint = "/uniform"

        return self.get(endpoint)

