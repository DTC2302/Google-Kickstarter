import copy
def matching(num_fabrics, fabrics):
    output = 0
    fabrics.sort(key = lambda x:(x[0], x[2]))
    by_color = copy.deepcopy(fabrics)
    fabrics.sort(key = lambda x:(x[1], x[2]))
    by_dur = copy.deepcopy(fabrics)
    for i in range(num_fabrics):
        if(by_color[i][2] == by_dur[i][2]):
            output+=1
    return output
    
    
    
    
cases = int(input())
case = 1
while case<=cases:
    num_fabrics = int(input())
    fabrics = []
    for i in range(num_fabrics):
        fabrics.append(tuple(map(str, input().split())))
    matched = matching(num_fabrics, fabrics)
    print(f'Case #{case}: {matched}')
    case+=1
    
