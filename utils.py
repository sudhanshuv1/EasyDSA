import random

def getRandomArray(n, type, min, max):
    nums = []
    for i in range(n):
        if type == 'int':
            nums.append(random.randint(min, max))
        else:
            nums.append(random.uniform(min, max))
    return nums