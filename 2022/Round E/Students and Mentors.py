cases = int(input())
case = 1
while case<=cases:
    students = int(input())
    scores = input().split()
    for i in range(len(scores)):
        scores[i] = int(scores[i])
    sorted_scores = sorted(scores, reverse = True)
    student = 1
    output = 'Case #' + str(case) + ":"
    highest_mentor = -1
    for i in scores:
        highest_mentor = -1
        for j in sorted_scores:
            if j<=i*2:
                if j == i:
                    if scores.count(j)>1:
                        highest_mentor=j
                        break
                else:
                    highest_mentor=j
                    break
        output = output + " " + str(highest_mentor)
        
    
        
    
    print(output)
    case += 1
