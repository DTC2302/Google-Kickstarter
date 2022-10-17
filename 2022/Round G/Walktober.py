cases = int(input())
case = 1
while cases>=case:
    totalParticipants, TotalDays, johnId = map(int, input().split())
    stepsNeeded = 0
    johnSteps = []
    stepsPerDay = []
    for i in range(1, totalParticipants+1):
        participantI = input().split()
        if i == johnId:
            johnSteps = (participantI)
        stepsPerDay.append(participantI)
    for i in range(TotalDays):
        dayX = []
        for j in range(totalParticipants):
            dayX.append(int(stepsPerDay[j][i]))
        dayX.sort()
        stepsNeeded += int(dayX[-1]) - int(johnSteps[i])
    print(f'Case #{case}: {stepsNeeded}')
    case+=1
