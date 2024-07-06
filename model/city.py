from model.base_model import BaseModel

class City(BaseModel):
    def __init__(self, name, country_code):
        super().__init__()
        self.name = name
        self.country_code = country_code

