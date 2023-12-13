sequences = []

with open('input.txt') as f:
    lines = f.read().split("\n")

    for line in lines:
        sequences.append(list(map(lambda x: int(x), line.split())))


def check(s):
    if not s:
        return True

    allzeros = True
    for i in s:
        if i != 0:
            allzeros = False
            break
    return allzeros


last = []
res = 0

for s in sequences:
    dp = s
    while not check(dp):
        last.append(dp[-1])
        for i in range(len(dp)-1):
            dp[i] = dp[i+1] - dp[i]
        del dp[-1]
    res += sum(last)
    last = []

print(res)

