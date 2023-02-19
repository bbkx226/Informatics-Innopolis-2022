start, end = 1, int(input())
print("\n")

while(True):
    mid = (start+end) // 2
    print(mid)
    guess = int(input())
    if guess != 0:
        if guess == 1: start = mid + 1
        elif guess == -1: end = mid
    else:
        break
    print("\n")
