from part_number_reader import PartNumberReader


part_number_reader = PartNumberReader('./input.txt')

sum = 0

for line_sum in part_number_reader:
    sum += line_sum

print('sum is', sum)
