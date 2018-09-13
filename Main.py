import os
import random


def get_dirs_and_files(path):
    dir_list = [directory for directory in os.listdir(path) if os.path.isdir(path + '/' + directory)]
    file_list = [directory for directory in os.listdir(path) if not os.path.isdir(path + '/' + directory)]

    return dir_list, file_list


def classify_pic(path):
    # To be implemented by Diego: Replace with ML model
    if "dog" in path:
        return 0.5 + random.random() / 2

    return random.random() / 2


def process_dir(path):

    dir_list, file_list = get_dirs_and_files(path)

    cat_list = []
    dog_list = []

    # Your code goes here
    for path, dir, file in os.walk('c:/Users/wenro/documents/1.1catsdogs.zip/1.1catsdogs/pictures/maria'):
        for dir in dir_list:
            if dir.startswith(' '):
                print(file_list)
            if dir_list.startswith('dog'):
                dog_list = process_dir(dir.path)
            else:
                cat_list = process_dir(dir.path)
    return cat_list, dog_list


def main():
    start_path = './' # current directory

    process_dir(start_path)


main()

