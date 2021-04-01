# Collections: Counter, namedtuple, OrderedDict, defaultdict, deque

from collections import Counter, namedtuple, OrderedDict, defaultdict, deque


# Counter
myString = "manivannan"
myCounter = Counter(myString)
print(myCounter)
print(myCounter.items())
print(myCounter.keys())
print(myCounter.values())
# gives n most common items
print(myCounter.most_common(2))
print(list(myCounter.elements()))


# namestuple
Point = namedtuple('Point', 'x,y')
pt = Point(1, 3)
print(pt)


# OrderedDict
ordered_dict = OrderedDict()
ordered_dict['a'] = 1
ordered_dict['b'] = 10
print(ordered_dict)


# defaultdict
d = defaultdict(int)
d['a'] = 1
d['b'] = 3
print(d['c'])  # gives default int value (0)


# deque
d = deque()

d.append(1)
d.appendleft(2)
d.append(5)
d.appendleft(6)
d.extend([2, 4, 5])
d.extendleft([8, 9, 11])

print(d)
print(d.pop())
print(d.popleft())

# rotate the queue
d.rotate(2)
print(d)
