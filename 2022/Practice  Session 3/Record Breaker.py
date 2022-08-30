cases = int(input())
case = 1
while case <= cases:
    days = int(input())
    visitors = input().split()
    record_breakers = 0
    highest = 0
    for i in range(len(visitors)):
        visitors[i] = int(visitors[i])
    highest_day = max(visitors)
    for i in range(len(visitors)):
        breaker = True
        if visitors[i] == highest_day:
            if i == len(visitors) - 1 and visitors.count(visitors[i]) == 1:
                record_breakers += 1
            elif visitors[i]>visitors[i+1]:
                record_breakers+=1
            break
        if i == 0:
            if visitors[i] <= visitors[i+1]:
                breaker = False
                highest = visitors[i]
            else:
                highest = visitors[i]
        elif i == len(visitors) - 1:
            if visitors[i] <= highest:
                breaker = False
        else:
            if visitors[i] <= highest or visitors[i+1] >= visitors[i]:
                breaker = False
            else:
                highest = visitors[i]
        if breaker == True:
            record_breakers += 1
    print("Case #" + str(case) + ": " + str(record_breakers))
    case += 1
