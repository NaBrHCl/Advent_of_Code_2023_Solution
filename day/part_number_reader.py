import re


class PartNumberReader:
    BUFFER_SIZE: int = 1
    SYMBOL: str = r'[^\d\s.]'

    def __init__(self, file_path: str):
        self.file = open(file_path)
        self.lines = [''] * (self.BUFFER_SIZE + 1)

        for _ in range(self.BUFFER_SIZE):
            self.lines.append(self.readline())

    def __iter__(self):
        return self

    def __next__(self) -> int:
        self.lines.pop(0)
        self.lines.append(self.readline())

        if self.lines[self.BUFFER_SIZE] == '':
            raise StopIteration

        return self.get_line_sum(self.BUFFER_SIZE)

    def readline(self) -> str:
        return self.file.readline().rstrip('\n')

    def get_line_sum(self, i: int) -> int:
        number_matches = re.finditer(r'\d+', self.lines[i])

        line_sum = 0

        for number_match in number_matches:
            if self.has_adjacent_symbol(number_match):
                line_sum += (int(number_match.group(0)))

        return line_sum

    def has_adjacent_symbol(self, number_match: re.Match) -> bool:
        line_index = self.BUFFER_SIZE - 1  # line above

        if self.contains_symbol(
                self.lines[line_index][max(number_match.start() - 1, 0): number_match.end() + 1]):
            return True

        line_index += 1  # same line

        if number_match.start() > 0 and self.is_symbol(self.lines[line_index][number_match.start() - 1]):
            return True

        if number_match.end() < len(self.lines[line_index]) and self.is_symbol(
                self.lines[line_index][number_match.end()]):
            return True

        line_index += 1  # line below

        if self.contains_symbol(
                self.lines[line_index][max(number_match.start() - 1, 0): number_match.end() + 1]):
            return True

    def is_symbol(self, line: str) -> bool:

        if line == '':
            return False

        return bool(re.fullmatch(self.SYMBOL, line))

    def contains_symbol(self, line: str) -> bool:

        if line == '':
            return False

        return bool(re.search(self.SYMBOL, line))
