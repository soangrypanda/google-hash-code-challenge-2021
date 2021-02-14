# This module takes an input file as an input and parses it.
# Results are "meta" dict of keys 1, 2, 3, 4. 1's for No of pizzas, the rest - No of teams.
# The other result is a "pizzas_dict". Keys are pizzas ingredients, values are No of pizzas with such ingredients.
# Additional result is a "pizzas_list". Which is a list of pizzas.
# Probably will delete one of "pizzas" at the end.

def parse_file(filename):
    file = open(filename, "r")

    # get info about number of pizzas and teams
    line = file.readline().split()
    meta = {
        1: line[0],  # 1 is for pizzas. don't want to have stings as keys.
        4: line[1],
        3: line[2],
        2: line[3]
    }

    # get info about pizzas
    pizzas_dict = {}
    pizzas_list = []
    for line in file:
        line_list = line.split()
        del line_list[0]
        line_list.sort()
        line_list = tuple(line_list)
        pizzas_list.append(set(line_list))
        if line_list in pizzas_dict:
            pizzas_dict[line_list] = pizzas_dict[line_list] + 1
        else:
            pizzas_dict[line_list] = 1

    return meta, pizzas_dict, pizzas_list
