def solution(x, y):
    x, y, ans = int(x), int(y), 0
    while True:
        if x == 0 or y == 0: return 'impossible'
        elif x == 1 or y == 1: return str(ans+x+y-2)
        elif x > y: x, y, ans = x%y, y, ans+x//y
        elif y > x: y, x, ans = y%x, x, ans+y//x
