from glob import glob
import csv

progress_file = glob('progress*.csv')
minutes_file = glob('*minutes*.csv')

assert(len(progress_file) == 1)
assert(len(minutes_file) == 1)

data = {}

with open(progress_file[0]) as csvfile:
        progress_reader = csv.reader(csvfile)
        header = next(progress_reader)[2:]
        for row in progress_reader:
            data[row[1]] = [sum([float(x) for x in row[2:]])]

with open(minutes_file[0]) as csvfile:
        minutes_reader = csv.reader(csvfile)
        header = next(minutes_reader)[2:]
        for row in minutes_reader:
            if row[1] in data:
                data[row[1]].append(sum([int(x) for x in row[2:]]))


result = sorted(data.items(), key=lambda item: item[1][0])

print('Results: the first number is total points, the second number is total time')
for item in result:
    print(item)

names, points_time = zip(*result)
points, time = zip(*points_time)

import matplotlib.pyplot as plt
fig, ax = plt.subplots()
ax.plot(names, points,'-', label='points')

ax2 = ax.twinx()
ax2.plot(names,time,'-r', label='time')

ax.legend(loc=0)
ax2.legend(loc=1)

ax.set(xlabel='students', ylabel='points',
       title='Class sorted by points')
ax2.set_ylabel(r"time")

plt.sca(ax)
plt.xticks(rotation=270)

fig.savefig("snapshot.png")
plt.show()


