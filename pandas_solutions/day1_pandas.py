import pandas as pd

text_file = open('../data/day1.txt', "r")
input_data = text_file.read()
text_file.close()
input_data = input_data.split('\n')
df = pd.DataFrame(input_data, columns=['input'])
df['increase'] = (df['input'] > df['input'].shift(1)) * 1
print("Part 1 answer: %0.0f" % (df['increase'].sum()))

df['window'] = df['input'].rolling(window=3).sum()
df['window_increase'] = (df['window'] > df['window'].shift(1)) * 1
print("Part 2 answer: %0.0f" % (df['window_increase'].sum()))
