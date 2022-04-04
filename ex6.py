def main(x):
    if (x[3] == 'ELM'):
        return 9
    elif (x[2] == 1985):
        if (x[1] == 'X10'):
            return 8
        if (x[1] == 'AWK'):
            return 7
        else:
            return 6
    elif (x[2] == 2002):
        if (x[0] == 'IDL'):
            return 5
        if (x[0] == 'X10'):
            return 4
        else:
            return 3
    else:
        if (x[0] == 'IDL'):
            return 2
        if (x[0] == 'X10'):
            return 1
        else:
            return 0


if __name__ == "__main__":
    main(['IDL', 'X10', 1985, 'ELM'])
