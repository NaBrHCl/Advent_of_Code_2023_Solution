import re


def get_file_content(file_path: str) -> list:
    return [line.rstrip('\n') for line in open(file_path).readlines()]


def get_asterisk_matches(text: str) -> iter:
    return re.finditer(r'\*', text)


def get_asterisks(lines: list) -> list:
    asterisks = list()

    for index, line in enumerate(lines):
        asterisk_matches = get_asterisk_matches(line)

        asterisks_on_line = list()

        for asterisk_match in asterisk_matches:
            asterisks_on_line.append(asterisk_match.start())

        asterisks.append(asterisks_on_line)

    return asterisks


def get_number_position(lines: list, number_line: int, number_col: int) -> list:
    number_left = number_col

    while lines[number_line][number_left - 1].isdigit():
        number_left -= 1

    number_right = number_col + 1

    while number_right < len(lines[number_line]) and lines[number_line][number_right].isdigit():
        number_right += 1

    return [number_left, number_right]


def get_adjacent_number_product_sum(lines: list, asterisks: list) -> int:
    sum = 0

    for asterisk_line, asterisks_on_line in enumerate(asterisks):  # for asterisks on a line
        for asterisk_col_index, asterisk_col in enumerate(asterisks_on_line):  # for each asterisk on a line

            adjacent_numbers = list()

            # check line above

            adjacent_numbers_on_line_pos = list()

            if asterisk_line > 0:
                pointer_line = asterisk_line - 1

                number_matches = re.finditer(r'\d+', lines[pointer_line][max(asterisk_col - 1, 0): asterisk_col + 2])

                for number_match in number_matches:
                    positions = get_number_position(lines, pointer_line,
                                                    max(asterisk_col - 1, 0) + number_match.start())

                    if positions not in adjacent_numbers_on_line_pos:
                        adjacent_numbers_on_line_pos.append(positions)
                        adjacent_numbers.append(int(lines[pointer_line][positions[0]:positions[1]]))

            # check same line

            pointer_line = asterisk_line

            if asterisk_col > 0:
                number_matches = re.finditer(r'\d+', lines[pointer_line][asterisk_col - 1])

                for number_match in number_matches:
                    positions = get_number_position(lines, pointer_line, asterisk_col - 1)
                    adjacent_numbers.append(int(lines[pointer_line][positions[0]:positions[1]]))

            if asterisk_col < len(lines[pointer_line]) - 1:
                number_matches = re.finditer(r'\d+', lines[pointer_line][asterisk_col + 1])

                for number_match in number_matches:
                    positions = get_number_position(lines, pointer_line, asterisk_col + 1)

                    adjacent_numbers.append(int(lines[pointer_line][positions[0]:positions[1]]))

            # check line below

            adjacent_numbers_on_line_pos = list()

            if asterisk_line < len(lines) - 1:
                pointer_line = asterisk_line + 1

                number_matches = re.finditer(r'\d+', lines[pointer_line][max(asterisk_col - 1, 0): asterisk_col + 2])

                for number_match in number_matches:
                    positions = get_number_position(lines, pointer_line,
                                                    max(asterisk_col - 1, 0) + number_match.start())

                    if positions not in adjacent_numbers_on_line_pos:
                        adjacent_numbers_on_line_pos.append(positions)
                        adjacent_numbers.append(int(lines[pointer_line][positions[0]:positions[1]]))

            if len(adjacent_numbers) == 2:
                sum += adjacent_numbers[0] * adjacent_numbers[1]

    return sum


lines = get_file_content('./input.txt')

asterisks = get_asterisks(lines)

result = get_adjacent_number_product_sum(lines, asterisks)

print('The sum is:', result)
