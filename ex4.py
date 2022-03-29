import math


def main(n):
    if n == 0:
        return -0.03
    elif n == 1:
        return 0.54
    elif n >= 2:
        return main(n-1)/98 - 23 - (main(n-2))**2


if __name__ == "__main__":
    main(4)
