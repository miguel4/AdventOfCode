def fuel(n):
    tmp = int(int(n) / 3) - 2
    return 0 if tmp <= 0 else tmp + fuel(tmp)


with open('input.txt') as f:
    print(sum([fuel(l) for l in f.readlines()]))
