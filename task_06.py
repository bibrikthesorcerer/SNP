# Author: Ignat Sakhovsky
# Email: ignatsahovsky@gmail.com

class WrongNumberOfPlayersError(Exception):
    def __init__(self, message="Incorrect number of players"):
        super().__init__(message)
    
class NoSuchStrategyError(Exception):
    def __init__(self, strategy) -> None:
        super().__init__(f"Met unknown strategy: {strategy}")

def rps_game_winner(lst:list):

    if len(lst) != 2:
        raise WrongNumberOfPlayersError() # подано больше или меньше 2 игроков
    
    p1_name, p1_move = lst[0]
    p2_name, p2_move = lst[1]

    # loses описывает все варианты проигрыша, а также все возможные стратегии
    loses = {
        "R": "P",
        "P": "S",
        "S":"R"
    }

    # если встретили неизвестную стратегию, поднимем исключение и выведем ее для простоты дебага
    if((not p1_move in loses)):
        raise NoSuchStrategyError(p1_move)  
    if((not p2_move in loses)):
        raise NoSuchStrategyError(p2_move)
    
    # если ход первого игрока проигрывает ходу второго, то вернем сообщение о победе второго. иначе аналогично
    if (p2_move in loses[p1_move]):
        return f"{p2_name} {p2_move}"
    else:
        return f"{p1_name} {p1_move}"