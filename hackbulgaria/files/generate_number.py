import sys
from random import randint


def main():
    file_name = sys.argv[1]
    num = sys.argv[2]

    file = open(file_name, 'w')

    numbers = []
    for i in range(int(num)):
        numbers.append(str(randint(1, 1000)))

    file.write(' '.join(numbers))
    file.close()

if __name__ == '__main__':
    main()