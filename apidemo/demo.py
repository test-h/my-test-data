def test_get_str():
    str_context = "welcomnihao&shui!di"

    list1  = list(str_context)
    list2 = []
    for i in list1:
        if i == "s":
            list2.append(i)
        elif i == "h":
            list2.append(i)
        elif i == "d":
            list2.append(i)
    print(list2)
    list3 = list(set(list2))
    print(list3.sort(key=list1.index))
    new_str = "".join(list3)
    print(new_str)



