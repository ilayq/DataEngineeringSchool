from Field import Field


class Game:
    def __init__(self) -> None:
        self.field = Field()
        
    def run(self):
        self.field.run()