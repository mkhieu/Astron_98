def removeDuplicates(lis):
    unique_list = []
    for i in lis:
        if i not in unique_list:
            unique_list = unique_list + [i]
    return unique_list
print(removeDuplicates([1, 1, 2, 3, 4, 4]))