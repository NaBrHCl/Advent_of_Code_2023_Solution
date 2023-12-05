import re
from bag import Bag


def get_file_content(file_path: str):
    return open(file_path, 'rt').readlines()


def get_color_occurrence(match: list):
    if len(match) == 0:
        return 0

    max_occurrence = int(match[0])

    for i in range(1, len(match)):
        if int(match[i]) > max_occurrence:
            max_occurrence = int(match[i])

    return max_occurrence


def get_bag(data: str):
    bag_id = re.search('(?<=Game )\\d+(?=: )', data)

    if bag_id is None:
        raise Exception('Invalid Game Header')

    bag_id = int(bag_id.group(0))

    bag_red = get_color_occurrence((re.findall('\\d+(?= red)', data)))
    bag_green = get_color_occurrence((re.findall('\\d+(?= green)', data)))
    bag_blue = get_color_occurrence(re.findall('\\d+(?= blue)', data))

    return Bag(bag_id, bag_red, bag_green, bag_blue)


def check_bag_possibility(guess_bag: Bag, test_bag: Bag):
    return guess_bag.red >= test_bag.red and guess_bag.green >= test_bag.green and guess_bag.blue >= test_bag.blue


guess_bag = Bag(0, 12, 13, 14)

id_sum = 0

try:
    lines = get_file_content('./input.txt')

    for line in lines:
        test_bag = get_bag(line)

        if check_bag_possibility(guess_bag, test_bag):
            id_sum += test_bag.id

    print('Calculation completed, sum of id:', id_sum)

except Exception as e:
    print('Program stopped because of the following error:', e)
