from statistics import median


def main():
    # a = [9, 2, 3, 4, 5, 6, 7, 8, 1, 3]
    a = input("Numbers by Space\n")
    a = [int(i) for i in a.split(" ")]
    a.sort()
    print(median(a))

main()
