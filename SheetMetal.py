x = [float(x) for x in input().split(" ")] # Steel
y = [x.pop(2), x.pop(-1)] # Machine
mini1, maxi1 = min(x), max(x)
mini2, maxi2 = min(y), max(y)
if mini1 > mini2 and mini1 > maxi2: ans = (mini1*maxi1 - mini2*maxi2)
else:
    if mini1 < mini2: mini2 = mini1
    if maxi1 < maxi2: maxi2 = maxi1 
    ans = (mini1*maxi1 - mini2*maxi2) / 2

print(round(ans, 2)) if ans > 0 else print(0)