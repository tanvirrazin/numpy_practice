import random
import numpy as np
from collections import Counter
import matplotlib.pyplot as plt

print('------------- Part 1: Random Numbers with Python ---------------')
outcome = random.randint(1, 6)
print(outcome)

print([random.randint(1, 6) for _ in range(10)])

outcome = np.random.randint(1, 7, size=10)
print(outcome)

print(np.random.randint(1, 7))
print(np.random.randint(1, 7, size=1))
print(np.random.randint(1, 7, size=10))
print(np.random.randint(1, 7, size=(10,)))
print(np.random.randint(1, 7, size=(4, 3)))

print('')
print('------------- Part 2: Random Choices with Python ---------------')
professionals = ["scientist", "philosopher", "engineer", "priest"]
print(random.choice("abcdefghij"))
print(random.choice(professionals))
print(random.choice(("apples", "bananas", "cherries")))

print('')
print('------------- Part 3: Weighted Random Choices ------------------')

def find_interval(x, partition):
    for i in range(0, len(partition)):
        if x < partition[i]:
            return i-1
    return -1

I = [0, 3, 5, 7.8, 9, 12, 13.8, 16]
for x in [-1.3, 0, 0.1, 3.2, 5, 6.2, 7.9, 10.8, 13.9, 15, 16, 16.5]:
    print(find_interval(x, I), end=", ")
print('')

def weighted_choice(sequence, weights):
    x = np.random.random()
    cum_weights = [0] + list(np.cumsum(weights))
    index = find_interval(x, cum_weights)
    return sequence[index]

faces_of_die = [1, 2, 3, 4, 5, 6]
weights = [1/12, 1/6, 1/6, 1/6, 1/6, 3/12]
outcomes = []
n = 10000

for _ in range(n):
    outcomes.append(weighted_choice(faces_of_die, weights))

c = Counter(outcomes)
for key in c:
    c[key] = c[key] / n

print(sorted(c.values()))

def find_interval(x, partition, endpoints=True):
    for i in range(0, len(partition)):
        if x < partition[i]:
            return i-1 if endpoints else i
    return -1 if endpoints else len(partition)

I = [0, 3, 5, 7.8, 9, 12, 13.8, 16]

for x in [-1.3, 0, 0.1, 3.2, 5, 6.2, 7.9, 10.8, 13.9, 15, 16, 16.5]:
    print(find_interval(x, I), end=", ")
print('')

for x in [-1.3, 0, 0.1, 3.2, 5, 6.2, 7.9, 10.8, 13.9, 15, 16, 16.5]:
    print(find_interval(x, I, endpoints=False), end=", ")
print('')

print('')
print('----------------- Part 4: Random seed --------------------')
random.seed(42)
for _ in range(10):
    print(random.randint(1, 10), end=", ")
print('')

random.seed(42)
for _ in range(10):
    print(random.randint(1, 10), end=", ")
print('')

print('')
print('----------------- Part 5: Random Numbers in Python with Gaussian and Normalvariate Distribution ------------')
n = 1000
values = []
frequencies = {}
while len(values) < n:
    value = random.gauss(180, 30)
    if 130 < value < 230:
        frequencies[int(value)] = frequencies.get(int(value), 0) + 1
        values.append(value)
print(values[:10])

freq = list(frequencies.items())
freq.sort()
# plt.plot(*list(zip(*freq)))
# plt.show()

print('')
print('----------------- Part 6: Exercise With Zeros and Ones --------------')
def random_ones_and_zeros(p):
    x = random.random()
    if x < p:
        return 1
    else:
        return 0

n = 1000000
print(sum(random_ones_and_zeros(0.8) for i in range(n)) / n)

def random_ones_and_zeros(p):
    while True:
        x = random.random()
        yield 1 if x < p else 0

def firstn(generator, n):
    for i in range(n):
        yield next(generator)

n = 1000000
print(sum(x for x in firstn(random_ones_and_zeros(0.8), n)) / n)

def ebitter(bitstream):
    while True:
        bit1 = next(bitstream)
        bit2 = next(bitstream)
        if bit1 + bit2 == 1:
            bit3 = next(bitstream)
            if bit2 + bit3 == 1:
                yield 1
            else:
                yield 0

def ebitter2(bitstream):
    bit1 = next(bitstream)
    bit2 = next(bitstream)
    bit3 = next(bitstream)
    while True:
        if bit1 + bit2 == 1:
            if bit2 + bit3 == 1:
                yield 1
            else:
                yield 0
        bit1, bit2, bit3 = bit2, bit3, next(bitstream)

n = 1000000
print(sum(x for x in firstn(ebitter(random_ones_and_zeros(0.8)), n)))
print(sum(x for x in firstn(ebitter2(random_ones_and_zeros(0.8)), n)))

print('')
print('------------------- Part 7: Synthetical Sales Figures --------------')

fh = open("sales_figures.csv", "w")
fh.write("Year, Frankfurt, Munich, Berlin, Zurich, Hamburg, London, Toronto, Strasbourg, Luxembourg, Amsterdam, Rotterdam, The Hague\n")
growthrates = np.array([1] * 12)
sales = np.array([1245.89, 2220.00, 1635.77, 1936.25, 1002.03, 2099.13,  723.99, 990.37, 541.44, 1765.00, 1802.84, 1999.00])
for year in range(1997, 2016):
    line = str(year) + ", " + ", ".join(map(str, sales))
    fh.write(line + "\n")

    if year % 4 == 0:
        min_percent = 0.98
        max_percent = 1.06
        growthrates = (max_percent - min_percent) * np.random.random_sample(12) + min_percent
    sales = np.around(sales * growthrates, 2)
fh.close()

print('')
print('-------------- Part 8: Exercise --------------')
print('---- Ex: 1------')
outcomes = [random.randint(1, 6) for _ in range(10000)]
even_pips = [x for x in outcomes if x % 2 == 0]
greater_two = [x for x in outcomes if x > 2]
combined = [x for x in outcomes if x%2 == 0 and x > 2]
print(len(even_pips) / len(outcomes))
print(len(greater_two) / len(outcomes))
print(len(combined) / len(outcomes))
