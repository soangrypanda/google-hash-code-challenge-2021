from parse import *
from knapsack import *

(meta, pizzas_dict, pizzas_list) = parse_file("inp.in")
print(meta)
print(pizzas_dict)
print(pizzas_list)

meta_cpy = meta.copy()
del meta_cpy[1]
all_teams = []
for key, value in meta_cpy.items():
    for i in range(0, int(value)):
        all_teams.append(key)
print(all_teams)

no_of_pizzas = meta[1]
print(no_of_pizzas)

piz_l_cpy = pizzas_list.copy()
team_index = 0
while len(piz_l_cpy) >= 2:
    members = all_teams[team_index]
    dp = dp_pizzas(piz_l_cpy, members)
    print(f"for team of {members} max value of pizzas is {dp[1]} with the following pizzas:")
    for i in dp[0]:
        print(piz_l_cpy[i])
        piz_l_cpy[i] = 0
    print(piz_l_cpy)
    piz_l_cpy = list(filter((0).__ne__, piz_l_cpy))
    print(piz_l_cpy)
    team_index += 1
print("THAT IS ALL!")
