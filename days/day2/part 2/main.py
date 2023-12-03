import re


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


def get_power(data: str):
    power = 1

    for color in ('red', 'green', 'blue'):
        power *= get_color_occurrence((re.findall(f'\\d+(?= {color})', data)))

    return power


power_sum = 0

try:
    lines = get_file_content('./input.txt')

    for line in lines:
        power_sum += get_power(line)

    print('Calculation completed, sum of power:', power_sum)

except Exception as e:
    print('Program stopped because of the following error:', e)
