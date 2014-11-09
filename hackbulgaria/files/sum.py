import sys


def sum_numbers(numbers):
    return sum(map(int, numbers))


def main():
    file_name = sys.argv[1]

    file = open(file_name, 'r')
    numbers = file.read().split(' ')
    file.close()

    print(sum_numbers(numbers))


if __name__ == '__main__':
    main()