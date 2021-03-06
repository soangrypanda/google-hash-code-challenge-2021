# This module takes an input file as an input and parses it.
# Results are "meta" dict of keys 1, 2, 3, 4. 1's for No of pizzas, the rest - No of teams.
# Additional result is a "pizzas_list". Which is a list of pizzas.

def parse_file(filename):
    print(f"Entering parse_file for the file {filename}")

    file = open(filename, "r")

    # get info about number of pizzas and teams
    line = file.readline().split()
    meta = {
        1: line[0],  # 1 is for pizzas. don't want to have stings as keys.
        2: line[1],
        3: line[2],
        4: line[3]
    }

    # get info about pizzas
    pizzas_list = []
    ing_total = 0
    index = 0
    for line in file:
        line_list = line.split()
        ing_total += int(line_list.pop(0))
        line_list.sort()
        line_list = tuple(line_list)
        pizzas_list.append((line_list, index))
        index += 1

    print("parse_file is ready to return!")
    return meta, pizzas_list, ing_total
