import math


def main(z):
    if z < -58:
        return math.arcsin(z)**6 - z**7
    elif -58 <= z < -8:
        return (math.floor(20*z**3-20))**7
    elif -8 <= z < 87:
        return ((z**3+27*z)**5-1-(math.ceil(z))**7)
    else:
        return((9*z**2+z**3)**3-1)


if __name__ == "__main__":
    main(15)
