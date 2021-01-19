# Link: https://inf-ege.sdamgia.ru/test?id=7973651

def task2():
    for w in range(2):
        for z in range(2):
            for y in range(2):
                for x in range(2):
                    F = (x or not y) and not (w == z) and w
                    if F:
                        print(w, z, y, x)
# task2() - wzyx

def task5():
    for D in range(10000):
        N = bin(D)
        N = N[2::] + N[len(N) - 1]
        N = N + str(N.count('1') % 2)
        N = int(N, 2)
        if N > 105:
            print(N)
            break
# task5() - 111

def task6():
    s = 301
    n = 0
    while s > 0:
        s = s - 10
        n = n + 2
    print(n)
# task6() - 62

def task10():
    with open("onegin.txt", "r") as text:
        text = text.read().lower().split()
        for x in text:
            if "дом" in x:
                if len(x) == 3 or len(x) == 4:
                    print(x)
# task10() - 1

def task11():
    length = 11
    symbols = 7  # 74 -> 128 -> 2^7 -> 7
    bit_len = round(symbols * length / 8)
    mass = bit_len * 50
    print(mass)
# task11() - 500

def task12():
    inp = "1" * 45 + "2" * 45
    while "111" in inp:
        inp = inp.replace("111", "2", 1)
        inp = inp.replace("222", "1", 1)
    print(inp)
# task12() - 21

def task14():
    def convert(n, b):
        d = ''
        while n:
            d += str(int(n % b))
            n //= b
        return d[::-1]
    print(convert(36 ** 8 + 6 ** 20 - 12, 6).count("0"))
# task14() - 5

def task15():
    def F(m, n, A):
        return (2 * m + 3 * n > 40) or ((m < A) and (n <= A))

    for A in range(1000):
        OK = True
        for n in range(100):
            for m in range(100):
                OK = F(m, n, A)
                if not OK: break
            if not OK: break
        if OK:
            print(A)
            break
# task15() - 21

def task16():
    def F(n):
        if n == 1:
            return 3
        if n > 1:
            return F(n - 1) * (n - 1)
    print(F(6))
# task16() - 360

def task17():
    found = []
    for x in range(7286, 9406):
        if x % 13 == 0 and x % 15 == 0 and x % 7 != 0 and x % 17 != 0 and x % 20 != 0 and x % 27 != 0:
            found.append(x)
    print(str(len(found)) + str(min(found)))
# task17() - 67410

def task22():
    for z in range(1000):
        x = z
        L = 0
        M = 0
        while x > 0:
            L = L + 1
            if x % 2 == 0:
                M = M + x % 10
            x = x // 10
        if L == 3 and M == 8:
            print(z)
            break
# task22() - 108