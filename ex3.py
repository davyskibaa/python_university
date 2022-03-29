import math


def main(a, n, b):
    y = 1
    z = 0
    w = 0
    for i in range(1, b + 1):
        for c in range(1, n + 1):
            for k in range(1, a + 1):
                x = ((math.ceil(k))**2-37*c**3-9*(math.log2(i))**6)
                y = y * x
            z = z + y
            y = 1
        w = w + z
        z = 0
    return w


if __name__ == "__main__":
    main(3, 5, 2)
