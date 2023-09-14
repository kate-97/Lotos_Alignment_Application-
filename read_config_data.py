CONFIG_FILE_NAME = '.config_application'


def get_path(directory_name):
    f = open(CONFIG_FILE_NAME, 'r')
    path_to_directory = None

    lines = f.readlines()

    for line in lines:
        if line.startswith(directory_name):
            pos = line.index('=')
            path_to_directory = line[pos+1:]
            path_to_directory = path_to_directory.strip()
            break

    return path_to_directory