global li
li = []
def compare(a, b, c, d, z):
    for i in [a, b, c , d]:
        if i < 0: 
            li.append(z)
            return 0
    z += 1
    return compare(a-2, b-1, c-1, d, z) + compare(a-2, b, c-2, d, z) + compare(a-1, b-1, c-2, d-1, z)
    
n = int(input())
for i in range(n):
    x = list(map(int, input().split()))
    compare(x[0], x[1], x[2], x[3], 0)
    print(max(li)-1)
    li.clear()

