cases = int(input())
case = 1
while case <= cases:
    bags_kids = input().split()
    kids = int(bags_kids[1])
    candy = (input().split())
    total_candy = 0
    for i in range(len(candy)):
        total_candy += int(candy[i])
    remaining = total_candy % kids
    print("Case #" + str(case) + ":", str(remaining))
    case += 1
