import re


def main(s):
    pattern1 = re.findall(r'\W\d{1,4}', s)
    temp = " ".join(pattern1)
    pattern1 = re.findall(r'\S\d{1,4}', temp)
    pattern2 = re.findall(r'>([.\s\w]\w+[.\s\w])<', s)
    temp = " ".join(pattern2)
    pattern2 = re.findall(r'\w+', temp)
    d = dict()
    length = len(pattern1)
    for i in range(0, length):
        d[pattern2[i]] = int(pattern1[i])
    return(d)


if __name__ == "__main__":
    print(main("\\begin<data>local 6033|>usxe</data>,<data> local 4896 "
               "|>arusxe</data>, <data> local 774 |> abeve </data>, \\end"))
