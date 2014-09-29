def variations(items, r, strResult = False):
    '''
    Calculates all r length variations of items 
    @arg items - list of items
    @arg r - length of variations
    @arg strResult - if True, returns result as multi-line string
    @returns two-dimensional list of variations or multi-line string
    '''
    if items == []:
        return []

    if r > len(items):
        return "variations: r cannot be bigger than the number of items!"

    if r == 1:
        return [[item] for item in items]

    result = []; subVariations = []

    for i, item in enumerate(items):
        subVariations = variations(items[:i] + items[i+1 :], r-1)
        if subVariations == []: break
        for item2 in subVariations:
            result += [[item] + item2]

    if strResult:
        resultStr = ""
        for subList in result:
            resultStr += ', '.join(str(item) for item in subList)
            resultStr += '\n'

        return resultStr
    else:
        return result

def combinations(items, r, strResult = False):
    '''
    Calculates all r length combinations of items 
    @arg items - list of items
    @arg r - length of combinations
    @arg strResult - if True, returns result as multi-line string
    @returns two-dimensional list of combinations or multi-line string
    '''
    if items == []:
        return []

    if r > len(items):
        if strResult:
            return "combinations: r cannot be bigger than the number of items!"
        else:
            return []

    if r == 1:
        return [[item] for item in items]

    result = []; subCombinations = []

    for i, item in enumerate(items):
        subCombinations = combinations(items[i+1:], r-1)
        if subCombinations == []: break
        for item2 in subCombinations:
            result += [[item] + item2]

    if strResult:
        resultStr = ""
        for subList in result:
            resultStr += ', '.join(str(item) for item in subList)
            resultStr += '\n'

        return resultStr
    else:
        return result

print(variations([1,2,3,4,5], 3, True))
print(combinations([1,2,3,4,5], 3, True))