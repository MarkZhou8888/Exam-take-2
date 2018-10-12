#creating array with class grades
arr = [83,24,22,97,32,53,75,77,93,28]
#creating function with for loop
def donuts(donut_party):
    donut_party = []
    avg = 0
# creating for loop that looks at all index values
    for num in arr:
#creating formula to calculate average
        avg = avg + num
    avg = num /10

    if num >= 90:
        print(" The class got an A average. Everyone gets a donut.")
    elif num >= 80:
        if num < 90:
            print(" The class got a B average. Everyone gets half a donut.")
    elif num >= 70:
        if num <80:
            print(" The class got a C average. Everyone gets a third of an donut.")
    elif num >= 65:
        if num <70:
            print(" The class got a D average. Everyone gives Mr. James half of a donut.")
    elif num <= 65:
        if num <70:
            print(" The class got an F average. You all fail the class.")
    print (donut_party)
#calling back function
donuts(arr)
