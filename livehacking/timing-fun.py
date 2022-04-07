import time

def filter_even(iterable):
    nums = []
    for element in iterable:
        if element % 2 == 0:
            nums.append(element)
    return nums

def filter_divisible(iterable, divisor):
    nums = []
    for element in iterable:
        if element % divisor == 0:
            nums.append(element)
    return nums


before = time.time()
for num in filter_even(filter_divisible(filter_divisible(range(10**8), 7), 5)):
    pass
after = time.time()

print(after - before)
