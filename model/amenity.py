from model.base_model import BaseModel


class Amenities(BaseModel):
    def __init__(self, name):
        super().__init__()
        self.name = name

    
