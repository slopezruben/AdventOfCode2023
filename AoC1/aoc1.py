input_file = open("aoc1_input.txt", "r")

number_string = ""
first_number = ""
second_number = ""
total = 0

for line in input_file.readlines():
    first_number = ""
    second_number = ""
    for char in line:
        if char.isdigit():
            if first_number == "":
                first_number = char
            second_number = char
    number_string = first_number + second_number
    print(number_string)
    if number_string != "":
        total += int(number_string)

print(total)
