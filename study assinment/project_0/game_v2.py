"""Game is a guess a number? Computer himself ansver what a number?"""

from itertools import count
import numpy as np

def random_predict(number:int=1) -> int:
    """Random guess a number

    Args:
        number (int, optional): Stock number. Defaults to 1.

    Returns:
        int: Value of tick
    """
    
    count = 0
    
    while True:
        count+=1
        predict_number = np.random.randint(1, 101)
        if number == predict_number:
            break
    return count

def score_game(random_predict) -> int:
    count_ls = []
    np.random.seed(1)
    random_array = np.random.randint(1, 101, size=(1000))
    
    for number in random_array:
        count_ls.append(random_predict(number))
        
    score = int(np.mean(count_ls))
    
    print(f"Ваш алгоритм угадывает число в среднем за {score} попыток")
    return score

#RUN
if __name__=='__main__':
    score_game(random_predict)
