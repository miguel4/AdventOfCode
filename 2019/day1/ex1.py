def c(n):
    return int(int(n) / 3) - 2


with open('input.txt') as f:
    print(sum([c(l) for l in f.readlines()]))
