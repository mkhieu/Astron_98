def five_by_five():
    whole_list = []
    for i in range(0,5):
        mini_list = []
        for j in range(1,6):
            mini_list += [j + (5*i)]
        whole_list.append(mini_list)
    return whole_list
print(five_by_five())

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
print(question_every_three(five_by_five()))