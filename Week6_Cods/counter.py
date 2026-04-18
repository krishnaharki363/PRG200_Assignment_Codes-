class Counter:
    count = 0   # class variable

    def __init__(self):
        Counter.count += 1


# Create objects
c1 = Counter()
c2 = Counter()
c3 = Counter()

print("Number of objects:", Counter.count)