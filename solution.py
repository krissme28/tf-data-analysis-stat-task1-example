import pandas as pd
import numpy as np
import math

chat_id = 317456038 # Ваш chat ID, не меняйте название переменной

def solution(x: np.array) -> float:
    # Измените код этой функции
    # Это будет вашим решением
    # Не меняйте название функции и её аргументы
    x = x - 139
    log_x = np.log(x)
    mu = np.mean(log_x)
    
    return mu # Ваш ответ
