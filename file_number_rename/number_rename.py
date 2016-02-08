import os
import argparse


def rename_files(directory_path, start_index, padding):
    working_dir = os.getcwd()
    os.chdir(directory_path)
    index = start_index
    sorted_directory = os.listdir(directory_path)
    sorted_directory.sort()
    for file in sorted_directory:
        file_name = file
        if os.path.isfile(file_name):
            new_name = rename_file_name(file_name, index, padding)
            os.rename(file_name, new_name)
            index += 1
    os.chdir(working_dir)


def check_int(input_string):
    success = False
    try:
        int(input_string)
        success = True
    except:
        pass
    return success


def rename_file_name(original_file_name, number_to_rename_to, padding):
    separators = '_.,'
    separator_position = find_first_separator(original_file_name, separators)

    new_file_name = original_file_name
    old_preposition = original_file_name[:separator_position]
    if check_int(old_preposition):
        new_preposition = str(number_to_rename_to).zfill(padding)
        new_file_name = new_preposition + original_file_name[separator_position:]
    return new_file_name


def find_first_separator(original_file_name, separators):
    position_list = []
    for separator in separators:
        position = original_file_name.find(separator)
        if not position == -1:
            position_list.append(position)
    position_list.sort()

    return position_list[0]


def parse_arguments():
    parser = argparse.ArgumentParser()
    parser.add_argument('--start', default=1, type=int, help="The number to start with the numbering")
    parser.add_argument('path', type=str, help="The full path to directory, containing the files to rename.")
    parser.add_argument('--padding', type=int, help="The number of characters the number is represented in (=3 -> 003_filename")
    return parser.parse_args()


if __name__ == "__main__":
    args = parse_arguments()
    directory = os.path.dirname(__file__)
    rename_files(args.path, args.start, args.padding)

# TODO parse "CD - 01" etc.