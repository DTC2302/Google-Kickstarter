cases = int(input())
case =1
while case<=cases:
    total = 0
    n = int(input())
    array = list(map(int, input().split()))
    for (i,k) in enumerate(array):
        subTotal = 0
        if(k<0):
            total+=0
        else:
            total+=k
            subTotal+=k
            for j in range(i+1, n):
                subTotal+=array[j]
                if(subTotal <0):
                    break
                else:
                    total+=subTotal
    print(f'Case #{case}: {total}')
    case+=1
