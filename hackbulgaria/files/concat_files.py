import sys


def main():
    content = []

    for arg in sys.argv[1:]:
        file = open(arg, 'r')
        content.append(file.read())
        content.append('\n')
        file.close()

    file = open('MEGATRON.txt', 'a')
    file.write(''.join(content))
    file.close

if __name__ == '__main__':
    main()