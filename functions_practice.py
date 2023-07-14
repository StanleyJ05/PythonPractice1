def hello():
    print ("Hello user!")

def pack(car, bike, bus):
    return [car, bike, bus]

def lunch(lunchList):
    if len(lunchList) == 0:
        print ("I do not have any lunch")
    else:
        for i in range (len(lunchList)):
            for i in range(len(lunchList)):
                if i == 0:
                    print (f"First I eat {lunchList[0]}")
                else:
                    print (f"Next I eat {lunchList[1]}")

hello()
print(pack("car", "bike","bus"))
print (pack(1,2,3))
lunch([])
lunch(["fries"])
lunch(["fries","apple", "chips", "orange", "sandwich"])


