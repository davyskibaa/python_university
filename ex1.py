import math


def main(y, x, z):
    return math.sqrt(4*(y-x**3-0.03)**7+51*z**2) + \
        (96*(abs(98*y*y+z**3)**6)-(1-58*x-y**3)**4) / \
        (math.sin(y+68+y*y)**2-(z+47*x*x)**4)


if __name__ == "__main__":
    main(0.35, -0.31, 0.93)
