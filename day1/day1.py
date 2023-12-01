data = open("input.txt").read().splitlines()

digits = {"one": "1",
          "two": "2", 
          "three": "3", 
          "four": "4",
          "five": "5",
          "six": "6",
          "seven": "7",
          "eight": "8",
          "nine": "9"}

result_1 = 0
result_2 = 0

for line in data:
    # Make a dictionary where the key is the index in the string
    # and the value is the string of the number
    part_1 = {i : c for i, c in enumerate(line) if c.isdigit()}

    # Then it's a simple job of getting the lowest and highest locations
    # using min and max
    result_1 += int(part_1[min(part_1)] + part_1[max(part_1)])

    # This was headachy, but similar. Instead, we find the location of
    # all the string representations of numbers.

    part_2 = {i : v for i, _ in enumerate(line) for k, v in digits.items() if line[i:].startswith(k)}
    
    # Handy Python trick. ** means to unpack a dictionary with the keys and values
    # intact. Doing this effectively combines our two dictionaries.

    part_2 = {**part_1, **part_2}

    # And then do the same as part 1. Get the min and max locations and add
    # them together
    result_2 += int(part_2[min(part_2)] + part_2[max(part_2)])

print(f"Part 1: {result_1}")
print(f"Part 2: {result_2}")
print("I hope tomorrow's is easier!")
