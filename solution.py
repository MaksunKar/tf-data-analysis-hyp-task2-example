import numpy as np
from scipy.stats import mannwhitneyu

chat_id = 790154026  # Ваш chat ID, не меняйте название переменной


def solution(x: np.array, y: np.array) -> bool:
    result = mannwhitneyu(x, y, alternative='two-sided')
    alpha = 0.03
    if result.pvalue < alpha:
        return True
    else:
        return False




