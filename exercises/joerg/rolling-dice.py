import random

ntries = 0
while True:
    ntries += 1
    eyes = random.randrange(1,7)
    if eyes == 6:
        print('yay! tries:', ntries)
        break

