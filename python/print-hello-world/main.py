import random

random_number = random.randint(0, 1)
if random_number == 0:
    for char in [72, 101, 108, 108, 111, 44, 32, 87, 111, 114, 108, 100, 33]:
        print(chr(char), end='')
else:
    hello = ''.join([chr(x) for x in [72, 101, 108, 108, 111]])
    world = ''.join([chr(x) for x in [87, 111, 114, 108, 100, 33]])
    print(hello + ', ' + world, end='')