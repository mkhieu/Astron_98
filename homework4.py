zero_to_fifty = list(range(0,51))
print(zero_to_fifty)

def square_list(lis):
    """
    Error: could not concatenate an integer and a list
    Fix: put brackets around i**2 in order to make it a list so that new_list and [i**2] can concatenate
    """
    new_list = []
    for i in lis:
        new_list = new_list + [i**2]
    return new_list

def odd_list(listA, listB):
    odds = []
    for i in listA:
        if i % 2 == 1:
            odds += [i]
    for i in listB:
        if i % 2 == 1:
            odds += [i]
    return odds

def five_by_five():
    whole_list = []
    for i in range(0,5):
        mini_list = []
        for j in range(1,6):
            mini_list += [j + (5*i)]
        whole_list.append(mini_list)
    return whole_list

def question_every_three(lis):
    """
    Error: 'multiple_five' list index out of range
    Fix: every time j > 4 is true, multiple_five is always reset back to 0
    Error: cannot access local variable 'multiple_five'
    Fix: originally 'multiple_five' was used in the else statement meaning the code read" lis[multiple_five][j] = '?'",
         so I changed it to "lis[0][j] = '?'" because the only time that else statement would be used is for the '?' in
         the first list in lis
    """
    i = 2
    while i < 25:
        j = i
        if j > 4:
            multiple_five = 0
            while j > 4:
                multiple_five += 1
                j -= 5
            lis[multiple_five][j] = '?'
            j += 3
            if j < 5:
                lis[multiple_five][j] = '?'
        else:
            lis[0][j] = '?'
        i += 3
    return lis

def removeDuplicates(lis):
    unique_list = []
    for i in lis:
        if i not in unique_list:
            unique_list = unique_list + [i]
    return unique_list
