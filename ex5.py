import math


def main(y, x, z):
    q = 0
    n = len(y)
    for i in range(1, n+1):
        q += 81*(y[math.ceil(i/4)-1]+45*(z[n-i])**3 +
                 (x[n-1-math.ceil(i/4)])**2)**5
    return q


if __name__ == "__main__":
    main([0.16, 0.03, -0.41, -0.65, -0.26],
         [-0.03, -0.8, -0.94, -0.51, 0.97],
         [-0.43, -0.15, 0.92, 0.72, -0.15]))
