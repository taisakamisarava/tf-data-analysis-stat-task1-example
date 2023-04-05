import pandas as pd
import numpy as np


chat_id = 123456 # Ваш chat ID, не меняйте название переменной

def solution(x: np.array) -> float:

    # Генерация случайных ошибок измерения скорости
    errors = np.random.normal(loc=-21, scale=np.exp(1), size=x.shape)

    # Средняя скорость машин за 10 секунд с учетом ошибок измерения
    v_mean = np.mean(x + errors)

    # Начальная скорость машин
    v_0 = 0

    # Время ускорения (в данном случае 10 секунд)
    t = 10

    # Точечная оценка коэффициента ускорения
    a = (v_mean - v_0) / t

    return a
