import sys


def main():
    file_name = sys.argv[1]
    text_file = open(file_name, 'r')
    content = text_file.read()
    print(content)
    text_file.close()

if __name__ == '__main__':
    main()