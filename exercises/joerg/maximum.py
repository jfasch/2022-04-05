import sys

#print(sys.argv)

a_str = sys.argv[1]
b_str = sys.argv[2]

a = int(a_str)
b = int(b_str)

#print('a:', a, 'type(a):', type(a))
#print('b:', b, 'type(b):', type(b))

if a < b:
    print(b)
else:
    print(a)
