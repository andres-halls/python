from math import factorial

def variations(items, r):
    '''
    Calculates all r length variations of items 
    @arg items - list of items
    @arg r - length of variations
    @returns two-dimensional list of variations
    '''
    if r > len(items):
        return "variations: r cannot be bigger than the number of items!"

    if r == 1:
        return [[item] for item in items]

    result = []
    temp1 = []; temp2 = []
    numEach = factorial(len(items)) // factorial(len(items) - r) // len(items)

    for i, item in enumerate(items):
        temp1 = [[item] for _ in range(numEach)]
        temp2 = variations(items[:i] + items[i+1 :], r-1)
        result += [temp1[i] + temp2[i] for i in range(len(temp1))]

    return result

def combinations(items, r):
    '''
    Calculates all r length combinations of items 
    @arg items - list of items
    @arg r - length of combinations
    @returns two-dimensional list of combinations
    '''
    if r > len(items):
        return "variations: r cannot be bigger than the number of items!"

    if r == 1:
        return [[item] for item in items]

    result = []
    temp1 = []; temp2 = []
    numEach = factorial(len(items)) // factorial(len(items) - r) // len(items)

    for i, item in enumerate(items):
        temp1 = [[item] for _ in range(numEach)]
        temp2 = variations(items[:i] + items[i+1 :], r-1)
        result += [temp1[i] + temp2[i] for i in range(len(temp1))]

    return result

result = variations([1,2,3,4,5], 2)
for subList in result: print(', '.join(str(item) for item in subList))