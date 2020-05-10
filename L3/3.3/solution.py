def solution(l):
    # Your code here
    ans = 0
    d = {
        i: {j for j in range(i+1, len(l)) if l[j]%l[i]==0}
        for i in range(len(l))
    }
    for x, v in d.items():
        if v: ans += sum(len(d[y]) for y in v)
    return ans
