import csv

# automate file openings later
file_to_parse = open("inp1.in", "r")

# get an info about number of pizzas and teams
line = file_to_parse.readline().split()
meta_info = {
    "pizzas":   line[0],
    "four":     line[1],
    "three":    line[2],
    "two":      line[3]
}

# this is to store info about all ingredients
# without duplicates
ingredients = set()

# fill ingredients with unique ingredients
for line in file_to_parse:
    line_list = line.split()
    del line_list[0]
    ingredients.update(line_list)

# make ingredients orderable
ingredients = tuple(ingredients)

# well, here i parse the file once again to fill the table
# could've filled it while parsing the first time
# but this solution is easier and we have other things to do)

file_to_parse.seek(0)
file_to_parse.readline()
row = list()

with open("inp.csv", "w") as outfile:
    writer = csv.writer(outfile)
    writer.writerow(ingredients)

    for line in file_to_parse:
        line_list = line.split()
        for item in ingredients:
            if item in line_list:
                row.append(1)
            else:
                row.append(0)
        writer.writerow(row)
        row.clear()
