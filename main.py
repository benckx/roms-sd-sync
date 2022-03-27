import os


def main():
    extensions_dict = parse_extensions()
    for key in extensions_dict:
        print(key + ' -> ' + str(extensions_dict[key]))

    source_rom_folder = '/home/benoit/roms/'
    target_roms_folder = '/media/benoit/EASYROMS/'
    source_files = list_game_files(source_rom_folder)
    target_files = list_game_files(target_roms_folder)
    for file in source_files:
        print("(source)" + file)
    for file in target_files:
        print("(target)" + file)

    commands = generate_commands(source_files, target_files, target_roms_folder)
    os.remove('sync_roms.sh')
    output_file = open('sync_roms.sh', 'a')
    for command in commands:
        print(command)
        output_file.write(command + '\n')
    output_file.close()


def generate_commands(source_files, target_files, target_roms_folder):
    commands = []
    target_keys = [file_comparison_key(x) for x in target_files]
    for source_file in source_files:
        key = file_comparison_key(source_file)
        if not key in target_keys:
            commands.append('rsync -av --progress "' + source_file + '" "' + target_roms_folder + key + '"')
    return commands


def file_comparison_key(file_name):
    """
    :return: str
        Strip prefix of file name and keep only e.g. 'console/file_name.bin'
        This allows comparison between 2 folders with identical structures but different locations
    """
    split = file_name.split('/')
    console_name = split[-2]
    file_name = split[-1]
    return console_name + '/' + file_name


def list_game_files(folder):
    """
    :return: array of str
        File names of all ROMs in 'folder'
    """
    result = []
    console_folders = next(os.walk(folder))[1]
    console_folders.sort()
    extensions_dict = parse_extensions()
    for console_name in extensions_dict:
        if console_name in console_folders:
            files = list_game_files_console_folder(folder + console_name, extensions_dict[console_name])
            for file in files:
                result.append(folder + console_name + '/' + file)
    result.sort()
    return result


def list_game_files_console_folder(console_folder, extensions):
    """
    :return: array of str
        File names in the 'console_folder', filtered by 'extensions'
        It doesn't consider sub-folders.
    """
    result = []
    for x in os.walk(console_folder):
        file_names = x[2]
        for file_name in file_names:
            extension = file_name.split('.')[-1]
            if extension in extensions:
                result.append(file_name)
    return result


def parse_extensions():
    """
    Parse extensions.csv file as a dict console_name -> valid extensions, e.g.:
        dreamcast -> ['7z', 'gdi', 'cdi', 'cue', 'chd', 'bin']
        gba -> ['gb', 'gbc', 'gba', 'zip', '7z']
        megadrive -> ['mdx', 'md', 'smd', 'gen', 'bin', 'zip', '7z']
    """
    result = {}
    extensions_csv = open('extensions.csv', 'r')
    for line in extensions_csv:
        split = line.split(";")
        console_name = split[0]
        console_extensions = parse_extensions_line(split[1])
        result[console_name] = console_extensions
    return result


def parse_extensions_line(extension_line):
    result = []
    split = extension_line.split(',')
    for item in split:
        sanitized = item.lstrip('.').rstrip('\n').lower()
        if not sanitized in result:
            result.append(sanitized)
    return result


if __name__ == '__main__':
    main()
