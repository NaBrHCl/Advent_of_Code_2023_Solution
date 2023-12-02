import re


def get_file_content(file_path: str):
    return open(file_path).readlines()


def get_calibration_data(line: str):
    digit_patterns = ('^\\D*(\\d)', '(\\d)\\D*?$')

    digits = list()

    for i in range(len(digit_patterns)):
        digit = re.search(digit_patterns[i], line)

        if digit == None or len(digit.groups()) != 1:
            raise 'Invalid calibration data input'
        else:
            digits.append(digit.group(1))

    result = ''

    for digit in digits:
        result += digit

    return int(result)


def calculate_calibration_sum(lines: list):
    sum = 0

    for i in range(len(lines)):

        try:
            sum += get_calibration_data(lines[i])

        except Exception as e:
            raise f'{e} occurred at line {i + 1}'

    return sum


try:
    data = get_file_content('./input.txt')

    result = calculate_calibration_sum(data)

    if result != None:
        print(f'Calculation completed, the sum is {result}')

except Exception as e:
    print('Program stopped due to the following error:', e)
