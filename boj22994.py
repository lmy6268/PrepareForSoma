import sys
input = sys.stdin.readline

n, m = list(map(int, input().split()))
maps = [input().strip() for _ in range(n)]
cmaps = [i for i in zip(*maps)]

r = [0]
c = [0]

for i in range(n-1):
    if maps[r[-1]] != maps[i+1]:
        r.append(i+1)
r.append(n)

for i in range(m-1):
    if cmaps[c[-1]] != cmaps[i+1]:
        c.append(i+1)
c.append(m)

dis_r = set()
dis_c = set()

for i in range(len(r)-1):
    dis_r.add(r[i+1] - r[i])
for i in range(len(c)-1):
    dis_c.add(c[i+1] - c[i])

dis_r = list(dis_r)
dis_c = list(dis_c)

if not dis_r:
    dis_r = [1]
if not dis_c:
    dis_c = [1]

def gcd(x, y):
    while y != 0:
        x, y = y, x%y
    return x

r_gcd = dis_r[0]
c_gcd = dis_c[0]

for i in range(1, len(dis_r)):
    r_gcd = gcd(r_gcd, dis_r[i])
for i in range(1, len(dis_c)):
    c_gcd = gcd(c_gcd, dis_c[i])

ans = []
for i in range(0, n, r_gcd):
    tmp = []
    for j in range(0, m, c_gcd):
        tmp.append(maps[i][j])
    ans.append(''.join(tmp))

print(len(ans), len(ans[0]))
for a in ans:
    print(a)