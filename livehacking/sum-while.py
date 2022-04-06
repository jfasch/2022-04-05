import sys

limit = int(sys.argv[1])

i = 0
sum = 0

while i < limit:
    sum += i
    i += 1

print(sum)
