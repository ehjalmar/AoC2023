class Bag:

    def __init__(self, number_of_red: int, number_of_blue: int, number_of_green: int):
        self.number_of_red = number_of_red
        self.number_of_blue = number_of_blue
        self.number_of_green = number_of_green
    
    def get_power(self):
        return self.number_of_red * self.number_of_blue * self.number_of_green