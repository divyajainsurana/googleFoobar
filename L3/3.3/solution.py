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


or
def solution(l):

    count = 0
    size = len(l)
    if size < 3: return 0

    cache = [0] * size
    for x in xrange(size):
        for y in xrange(x + 1, size):
            if l[y] % l[x] == 0:
                cache[y] += 1
                count += cache[x]

    return count
