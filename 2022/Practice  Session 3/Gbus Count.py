cases = int(input())
case = 1
while case <= cases:
    print("Case #" + str(case) + ':', end = ' ')
    buses = input()
    cities = input().split()
    for i in range(len(cities)):
        cities[i] = int(cities[i])
    gbus_cities = list()
    for i in range(0, len(cities), 2):
        gbus_cities.append([cities[i], cities[i+1]])
    number_cities = int(input())
    for i in range(number_cities):
        number_buses = 0
        city = int(input())
        for j in range(len(gbus_cities)):
            gbus = gbus_cities[j]
            if city>= gbus[0] and city<= gbus[1]:
                number_buses += 1
        print(str(number_buses), end = ' ')
    print()
    if case != cases:
        empty_line = input()
    case+=1
    
