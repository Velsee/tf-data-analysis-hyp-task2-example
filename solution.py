import pandas as pd
import numpy as np
from scipy.stats import mannwhitneyu


chat_id = 1253313260 # Ваш chat ID, не меняйте название переменной

def solution(x: np.array, y: np.array) -> bool:
    _, p_value = mannwhitneyu(x, y, alternative="two-sided")
    return p_value < 0.07
    url = "https://raw.githubusercontent.com/Velsee/Data/main/historical_data.csv"
url1 = "https://raw.githubusercontent.com/Velsee/Data/main/modified_data_of_type_1.csv"
url2 = "https://raw.githubusercontent.com/Velsee/Data/main/modified_data_of_type_2.csv"
url3 = "https://raw.githubusercontent.com/Velsee/Data/main/modified_data_of_type_3.csv"
historical_data = pd.read_csv(url).to_numpy()
modified_data_of_type_1 = pd.read_csv(url1).to_numpy()
modified_data_of_type_2 = pd.read_csv(url2).to_numpy()
modified_data_of_type_3 = pd.read_csv(url3).to_numpy()
print(solution(historical_data, modified_data_of_type_1))
print(solution(historical_data, modified_data_of_type_2))
print(solution(historical_data, modified_data_of_type_3))
