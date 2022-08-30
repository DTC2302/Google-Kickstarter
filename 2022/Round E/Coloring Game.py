test_cases = int(input())
case = 1
while case<=test_cases:
    cells = int(input())
    bot = 0
    while cells>=1:
        bot = bot + 1
        cells = cells - 5
    print("Case #" + str(case) + ": " + str(bot))
    case = case+1

