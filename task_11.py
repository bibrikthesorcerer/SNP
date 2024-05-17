# Author: Ignat Sakhovsky
# Email: ignatsahovsky@gmail.com

class Dessert():
    def __init__(self, name: str="", calories: int=0):
        self.name = name
        self.calories = calories
    
    def __str__(self) -> str:
        return f"Dessert {self.name} with {self.calories} calories"

    def get_name(self) -> str:
        return self.name
    
    def get_calories(self) -> int:
        return self.calories
    
    def set_name(self, new_name: str):
        self.name = new_name
    
    def set_calories(self, new_cals: int):
        self.calories = new_cals

    def is_healthy(self) -> bool:
        return int(self.calories) < 200
    
    def is_delicious(self) -> bool:
        return True