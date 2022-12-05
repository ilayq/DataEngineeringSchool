def sol1() -> None:
    x = 0.1
    s = 0
    i = 0
    while x ** i >= 10 ** -4:
        s += x ** i
        i += 2
    print(s)


def sol2() -> None:
    n, m = map(int, input().split())
    c = 0
    while n - m > 0:
        n -= m
        c += 1
    print(c, n)


def sol3() -> None:
    s = 10
    d = 10
    for i in range(6):
        d *= 1.1
        s += d
    print(s)
    s = 10
    c = 1
    d = 10
    while d < 100:
        s *= 1.1
        d += s
        c += 1
    print(c)
    s = 10
    c = 1
    while s < 20:
        s *= 1.1
        c += 1
    print(c)


def sol4() -> None:
    s = 10000
    c = 0
    while s < 20000:
        s *= 1.08
        c += 1
    print(c)


def sol5() -> None:
    s = 0.1
    c = 0
    while s > 10 ** -10
        s /= 2
        c += 1
    print(c)

