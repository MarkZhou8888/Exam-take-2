def Discriminant(a,b,c):
    if (b**2)-(4*a*c) > 0:
        print("two real roots")
    elif (b**2)-(4*a*c) == 0:
        print("one real root")
    elif (b**2)-(4*a*c) < 0:
        print("no real root")
    else:
        print("try again")
Discriminant(1,3,2)
