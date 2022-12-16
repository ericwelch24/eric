itemName = input("Enter name of item purchased: ")
itemYear = int(input("Enter year purchased: "))
itemCost = int(input("Enter cost of item: "))
itemLife = int(input("Enter estimated life of item (in years): "))
depMethod= input("Enter method of depreciation (SL or DDB): ")

if depMethod == "SL":
    print("straight-line balance")

    depreciation1 = 0

    description = '{:10} {:35} {:35} {:35}'
    print(description.format("Year", "Value at beginning of year", "Amount depreciated during year", "Total depreciation to end of year"))

    for i in range(1, itemLife + 1):
        year = itemYear + (i-1)
        beginValue = itemCost - (depreciation1*(i-1))
        depreciation1 = (1/itemLife) * itemCost
        totalDep = (itemCost/itemLife) * i
        print(description.format(str(year), str(beginValue), str(depreciation1), str(totalDep)))

elif depMethod == "DDB":
    print("double-declining balance")

    depreciation2 = 0
    totalDep2 = 0
    beginValue2 = itemCost

    description2 = '{:10} {:35} {:35} {:35}'
    print(description2.format("Year", "Value at beginning of year", "Amount depreciated during year", "Total depreciation to end of year"))

    for i in range(1, itemLife + 1):
        year = itemYear + (i-1)
        beginValue2 = beginValue2 - (depreciation2)
        if i == itemLife:
            depreciation2 = beginValue2
            totalDep2 = itemCost
        else:
            depreciation2 = ((2/itemLife) * beginValue2)
            totalDep2 = totalDep2 + depreciation2
        print(description2.format(str(year), str(beginValue2), str(depreciation2), str(totalDep2)))
else:
    print("retry program")
