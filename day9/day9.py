def lasts(series):
    while series:
        yield series[-1]
        series = [b-a for a,b in zip(series, series[1:])]

series = [[int(x) for x in line.split()] for line in open('input.txt')]
print(sum(sum(lasts(s)) for s in series))
print(sum(sum(lasts(s[::-1])) for s in series))