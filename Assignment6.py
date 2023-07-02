def ds(roll_no, name):
    ls = [roll_no, name]
    tup = (roll_no, name)
    se = {roll_no, name}
    dic = {"roll_no": roll_no, "name": name}

    print("Values before change:")
    print("List:", ls)
    print("Tuple:", tup)
    print("Set:", se)
    print("Dictionary:", dic)

    #updated values
    ls[0] = 38
    tup = (38, "Dhvani")
    se.remove(roll_no)
    se.add(30)
    dic["roll_no"] = 38

    print("\nValues after change:")
    print("List:", ls)
    print("Tuple:", tup)
    print("Set:", se)
    print("Dictionary:", dic)

    #delete
    del ls
    del tup
    del se
    del dic

    # print(dic,ls,tup,se)#error generated as all datastructures are deleted

ds(38, "Dhavni")
