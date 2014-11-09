import sys


def main():
    for arg in sys.argv[1:]:
        file_name = arg
        text_file = open(file_name, 'r')
        content = text_file.read()
        print(file_name+':')
        print(content)
        text_file.close()

if __name__ == '__main__':
    main()