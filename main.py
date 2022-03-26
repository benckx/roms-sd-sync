import os


def main():
    source_folder = '/home/benoit/roms/'
    console_folders = next(os.walk(source_folder))[1]
    print(console_folders)
    extensions_csv = open('extensions.csv', 'r')
    for line in extensions_csv:
        split = line.split(";")
        console_name = split[0]
        if (console_name in console_folders):
            print(console_name + ' -> ' + str(list_extensions(split[1])))


def list_extensions(extension_line):
    result = []
    split = extension_line.split(',')
    for item in split:
        sanitized = item.lstrip('.').rstrip('\n').lower()
        if not sanitized in result:
            result.append(sanitized)
    return result


if __name__ == '__main__':
    main()
