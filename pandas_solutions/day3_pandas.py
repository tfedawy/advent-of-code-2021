import pandas as pd


def get_dec(number_list):
    return int("".join(str(i) for i in number_list), 2)


text_file = open("day3.txt", "r")
input_data = text_file.read()
text_file.close()

input_data = input_data.split('\n')
input_data = [i.split() for i in input_data]
input_data = [list(i[0]) for i in input_data]
input_data = pd.DataFrame(input_data).astype(int)

summary = list(input_data.sum() / input_data.count())
gamma_bin = [1 * (i >= 0.5) for i in summary]
epsilon_bin = [1 * (i < 0.5) for i in summary]
power_consumption = get_dec(gamma_bin) * get_dec(epsilon_bin)

print('Part 1 answer is:', power_consumption)

oxygen = input_data.copy()
carbon = input_data.copy()

i = 0
while oxygen.shape[0] > 1 and i < len(input_data.columns):
    criteria = (oxygen[i].sum() / oxygen[i].count() >= 0.5) * 1
    oxygen = oxygen.loc[oxygen[i] == criteria]
    i += 1

i = 0
while carbon.shape[0] > 1 and i < len(input_data.columns):
    criteria = (carbon[i].sum() / carbon[i].count() < 0.5) * 1
    carbon = carbon.loc[carbon[i] == criteria]
    i += 1

oxygen_bin = oxygen.iloc[0]
carbon_bin = carbon.iloc[0]
life_support_rating = get_dec(oxygen_bin) * get_dec(carbon_bin)

print('Part 2 answer is:', life_support_rating)
