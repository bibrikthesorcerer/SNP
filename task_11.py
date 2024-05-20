# Author: Ignat Sakhovsky
# Email: ignatsahovsky@gmail.com

class Dessert():
    def __init__(self, name: str="", calories: int=0):
        self._name = name
        self._calories = calories
    
    def __str__(self) -> str:
        return f"Dessert {self._name} with {self._calories} calories"

    def get_name(self) -> str:
        return self._name
    
    def get_calories(self) -> int:
        return self._calories
    
    def set_name(self, new_name: str):
        self._name = new_name
    
    def set_calories(self, new_cals: int):
        self._calories = new_cals

    def is_healthy(self) -> bool:
        try:
            return int(self._calories) < 200
        except ValueError:
            print("Cannot convert calories to int.")
            return None
    
    def is_delicious(self) -> bool:
        return True
    
    name = property(get_name, set_name)
    calories = property(get_calories, set_calories)
