import os


def main():
    source_folder = '/home/benoit/roms/'
    console_folders = next(os.walk(source_folder))[1]
    console_folders.sort()
    print(console_folders)
    extensions_csv = open('extensions.csv', 'r')
    for line in extensions_csv:
        split = line.split(";")
        console_name = split[0]
        if (console_name in console_folders):
            console_folder = source_folder + console_name
            console_extensions = parse_extensions(split[1])
            print(list_game_files(console_folder, console_extensions))
            # print(console_name + ' -> ' + str(list_extensions(split[1])))


def list_game_files(console_folder, extensions):
    result = []
    for x in os.walk(console_folder):
        file_names = x[2]
        for file_name in file_names:
            extension = file_name.split('.')[-1]
            if extension in extensions:
                result.append(file_name)

    return result


def parse_extensions(extension_line):
    result = []
    split = extension_line.split(',')
    for item in split:
        sanitized = item.lstrip('.').rstrip('\n').lower()
        if not sanitized in result:
            result.append(sanitized)
    return result


if __name__ == '__main__':
    main()
