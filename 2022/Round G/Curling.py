cases = int(input())
case = 1
while case<=cases:
    unneeded, radius = map(int, input().split())
    n = int(input())
    distances = []
    for i in range(n):
        x, y = map(int, input().split())
        x = abs(x)
        y = abs(y)
        dist = ((x**2) + (y**2))**(1/2)
        distances.append((dist, 'R'))
    n = int(input())
    for i in range(n):
        x, y = map(int, input().split())
        x = abs(x)
        y = abs(y)
        dist = ((x**2) + (y**2))**(1/2)
        distances.append((dist, 'Y'))
    distances.sort()
    scorer = 'R'
    if(len(distances)>0):
        if(distances[0][1] == 'R'):
            scorer = 'R'
        else:
            scorer = 'Y'
    r = 0
    y = 0
    if scorer =='R':
        for i in distances:
            if(i[1] == scorer) and i[0]<=(radius+unneeded):
                r+=1
            else:
                break
    else:
        for i in distances:
            if(i[1] == scorer) and i[0]<=(radius+unneeded):
                y+=1
            else:
                break
    print(f'Case #{case}: {r} {y}')
    case+=1
