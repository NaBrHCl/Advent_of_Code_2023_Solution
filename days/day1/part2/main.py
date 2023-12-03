import re


def get_file_content(file_path: str):
    return open(file_path).readlines()


def get_calibration_data(line: str):
    alphabetic_numerals = {
        'one': '1',
        'two': '2',
        'three': '3',
        'four': '4',
        'five': '5',
        'six': '6',
        'seven': '7',
        'eight': '8',
        'nine': '9'
    }

    digit_pattern = f'(?=(\\d|{"|".join(alphabetic_numerals.keys())}))'

    digits = list()

    numbers = re.findall(digit_pattern, line)

    if numbers is None or len(numbers) == 0:
        raise Exception('Invalid calibration data input')

    result = ''

    digit_index = (0, -1)

    for i in digit_index:
        if numbers[i].isdigit():
            result += numbers[i]
        else:
            result += alphabetic_numerals[numbers[i]]

    return int(result)


def calculate_calibration_sum(lines: list):
    sum = 0

    for i in range(len(lines)):
        try:
            sum += get_calibration_data(lines[i])

        except Exception as e:
            raise Exception(f'{e} occurred at line {i + 1}')

    return sum


try:
    data = get_file_content('./input.txt')

    result = calculate_calibration_sum(data)

    if result is not None:
        print(f'Calculation completed, the sum is {result}')

except Exception as e:
    print('Program stopped due to the following error:', e)
