import numpy as np
from scipy.stats import ttest_ind

chat_id = 790154026  # Ваш chat ID, не меняйте название переменной


def solution(x: np.array, y: np.array) -> bool:
    result = ttest_ind(x, y)
    alpha = 0.03
    if result[1] > alpha:
        return True
    else:
        return False




