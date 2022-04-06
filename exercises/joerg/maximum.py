import sys

# print(sys.argv)

a_str = sys.argv[1]
b_str = sys.argv[2]

# print('a_str:', a_str, type(a_str), 'b_str:', b_str, type(b_str))

a = int(a_str)
b = int(b_str)

# print('a:', a, type(a), 'b:', b, type(b))

if a < b:
    print(b)
else:
    print(a)
