import sys

import aocd

data = aocd.get_data()
text_file = open("data/day" + sys.argv[1] + ".txt", "w")
# text_file = open("data/day.txt", "w")
n = text_file.write(data)
text_file.close()
