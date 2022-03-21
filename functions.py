def function(a):
    print(a)
    print(type(a), "+", a[2])
    print("a has a length of ", len(a))
    print()
    if len(a) < 8:
        print("(a) less than 8?", len(a) < 8)
        print((len(a) < 8))
    elif len(a) == 12:
        print("a is equal to 12", (len(a) == 12))
    else:
        print("(a) greater than 8? ", (len(a) > 8))
    print()
    islessthan4 = (len(a) < 8)
    print("a is less than 8: ", islessthan4)

    for x in a:
        print(x)

