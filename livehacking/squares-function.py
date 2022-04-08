def squares(input_list):
    squares_list = []
    for num in input_list:
        squares_list.append(num**2)
    return squares_list

x = [2,1,3,5,2]
sqs = squares(x)
print(sqs)

y = [4, 5, 1, 3]
sqs1 = squares(y)
print(sqs1)
