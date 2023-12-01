import re


def get_file_content(file_path):
    return open(file_path).readlines()


print(get_file_content('./input.txt'))
