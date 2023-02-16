def unique(list):
    list2 = []
    for i in list:
        if i not in list2:
            list2.append(i)
    print(list2)