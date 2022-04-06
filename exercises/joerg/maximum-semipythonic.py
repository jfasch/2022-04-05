import sys

print('sys.argv:', sys.argv)

args = sys.argv[1:]

print('args:', args)

maximum = 0

for element in args:
    int_element = int(element)
    if int_element > maximum:
        maximum = int_element

print(maximum)
