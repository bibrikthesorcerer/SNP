# Author: Ignat Sakhovsky
# Email: ignatsahovsky@gmail.com

def coincidence(lst: list =[], rng: range=None) -> list:
    """
    Return a list of elements from lst whose values fit in rng.
    """
    # возвращаем список элементов из lst, которые являются числами и лежат в промежутке rng
    return [elem \
            for elem in lst \
            if isinstance(elem, (int,float)) \
                and rng.start <= elem < rng.stop]