def square_list(lis):
    """
    Error: could not concatenate an integer and a list
    Fix: put brackets around i**2 in order to make it a list so that new_list and [i**2] can concatenate
    """
    new_list = []
    for i in lis:
        new_list = new_list + [i**2]
    return new_list
print(square_list([2, 3, 4]))

def odd_list(listA, listB):
    odds = []
    for i in listA:
        if i % 2 == 1:
            odds += [i]
    for i in listB:
        if i % 2 == 1:
            odds += [i]
    return odds
print(odd_list(range(1,11), range(20, 31)))