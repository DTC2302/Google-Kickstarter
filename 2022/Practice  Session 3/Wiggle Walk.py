from copy import deepcopy
cases = int(input())
case = 1
while case<= cases:
    locations = input().split()
    location = [int(locations[3]), int(locations[4])]
    commands = input()
    been = set()
    been.add(tuple(location))
    for i in commands:
        if i == 'N':
            while 1:
                location[0]-=1
                if not(tuple(location) in been):
                    been.add(tuple(location))
                    break
        elif i == "E":
            while 1:
                location[1]+=1
                if not(tuple(location) in been):
                    been.add(tuple(location))
                    break
                
        elif i == 'S':
            while 1:
                location[0]+=1
                if not(tuple(location) in been):
                    been.add(tuple(location))
                    break
        else:
            while 1:
                location[1]-=1
                if not(tuple(location) in been):
                    been.add(tuple(location))
                    break
    print("Case #" + str(case) + ": " + str(location[0]) + " " + str(location[1]))
    case+=1
    #2:23
