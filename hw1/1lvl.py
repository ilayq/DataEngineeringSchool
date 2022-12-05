def sol1() -> None:
    x = float(input())
    s = 1
    for i in range(1, 11):
        s += 1 / (x ** i)
    print(s)


def sol2() -> list[int]:
    nums = [1, 1]
    for i in range(6):
        nums.append(nums[-1] + nums[-2])
    return nums


def sol3() -> None:
    c = sol2()
    d = sol2()
    s = 0
    for i in range(5):
        s += c[i]/d[i]
    print(s)


def sol4() -> None:
    s = 0
    n = 2
    for i in range(64):
        s += n ** i
    print(s / 15 / 1000)


def sol5() -> None:
    print(10 * 2 ** 8)


if __name__ == '__main__':
    sol1()
    print(sol2())
    sol3()
    sol4()
    sol5()
