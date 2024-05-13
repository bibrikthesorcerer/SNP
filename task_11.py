# Author: Ignat Sakhovsky
# Email: ignatsahovsky@gmail.com

class Dessert():
    def __init__(self, name: str="", calories: int=0):
        self.__name = name
        self.__calories = calories
    
    def __str__(self) -> str:
        return f"Dessert {self.__name} with {self.__calories} calories"

    def get_name(self) -> str:
        return self.__name
    
    def get_calories(self) -> int:
        return self.__calories
    
    def set_name(self, new_name: str):
        self.__name = new_name
    
    def set_calories(self, new_cals: int):
        self.__calories = new_cals

    def is_healthy(self) -> bool:
        return self.__calories < 200
    
    def is_delicious(self) -> bool:
        return True