while True:
    try:
        a = int(input())
        num = [int(b) for b in input().split(" ")]
        num.reverse()
        for i in range(0, a):
            print(num[i], end=" ")
    except:
        break