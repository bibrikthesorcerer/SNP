# Author: Ignat Sakhovsky
# Email: ignatsahovsky@gmail.com

class WrongNumberOfPlayersError(Exception):
    """
    Custom exception for an incorrect number of players in RPS game.
    """
    def __init__(self):
        super().__init__("Incorrect number of players")
    
class NoSuchStrategyError(Exception):
    def __init__(self, strategy) -> None:
        # вместе с сообщением об ошибке, выведем саму неверную стратегию
        super().__init__(f"Met unknown strategy: {strategy}")

def rps_game_winner(lst:list[list[str]]) -> str:
    """
    Determine winner in RPS game based on players' moves.
    """
    # подано больше или меньше 2 игроков
    if len(lst) != 2:
        raise WrongNumberOfPlayersError() 
    
    # распаковали значения
    p1_name, p1_move = lst[0]
    p2_name, p2_move = lst[1]

    # loses описывает все варианты проигрыша, а также всевозможные стратегии
    loses = {
        "R": "P",
        "P": "S",
        "S":"R" }

    # если встретили неизвестную стратегию, поднимем исключение и выведем ее для простоты дебага
    if(p1_move not in loses):
        raise NoSuchStrategyError(p1_move)  
    if(p2_move not in loses):
        raise NoSuchStrategyError(p2_move)
    
    # если ход первого игрока проигрывает ходу второго, то победил второй. иначе - первый
    if (p2_move in loses[p1_move]):
        return f"{p2_name} {p2_move}"
    else:
        return f"{p1_name} {p1_move}"