import pandas as pd

text_file = open('../data/day2.txt', "r")
input_data = text_file.read()
text_file.close()
input_data = input_data.split('\n')
input_data = [[line.split()[0], int(line.split()[1])] for line in input_data]
data = pd.DataFrame(input_data, columns=['direction', 'amount'])

data['horizontal'] = data[data['direction'] == 'forward']['amount']
data.loc[data['direction'] == 'down', 'depth'] = data['amount']
data.loc[data['direction'] == 'up', 'depth'] = data['amount'] * -1
print("Part 1 answer: %0.0f" % (data['horizontal'].sum() * data['depth'].sum()))

data = pd.DataFrame(input_data, columns=['direction', 'amount'])
data['horizontal'] = data[data['direction'] == 'forward']['amount']
data.loc[data['direction'] == 'down', 'aim'] = data['amount']
data.loc[data['direction'] == 'up', 'aim'] = data['amount'] * -1
data['aim'] = data['aim'].cumsum()
data['aim'] = data['aim'].fillna(method='ffill')
data['depth'] = data['horizontal'] * data['aim']
print("Part 2 answer: %0.0f" % (data['horizontal'].sum() * data['depth'].sum()))
