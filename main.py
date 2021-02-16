from parse import *
from knapsack import *
from order_or_teams import *
from out import *

file_name = "inp_min"
(meta, pizzas_list) = parse_file(file_name)
print(meta)
print(pizzas_list)

meta_cpy = meta.copy()
del meta_cpy[1]
all_teams = []
for key, value in meta_cpy.items():
    for i in range(0, int(value)):
        all_teams.append(key)
print(all_teams)

orders_of_teams = give_all_teams_orders(all_teams)

no_of_pizzas = meta[1]
print(no_of_pizzas)

result = {"value": 0, "deliveries": 0, "piz_to_team": list()}

for order in orders_of_teams:
    piz_l_cpy = pizzas_list.copy()
    team_index = 0
    total_deliveries = 0
    total_value = 0
    piz_to_team = list()
    order_len = len(order)
    while len(piz_l_cpy) >= 2 and team_index < order_len:
        members = order[team_index]
        pizzas_indexes = list()
        dp = dp_pizzas(piz_l_cpy, members)
        if dp[1] != 0:
            print(f"for team of {members} max value of pizzas is {dp[1]} with the following pizzas:")
            for i in dp[0]:
                print(piz_l_cpy[i])
                pizzas_indexes.append(piz_l_cpy[i][1])
                piz_l_cpy[i] = 0
            piz_to_team.append((members, pizzas_indexes))
            print(piz_l_cpy)
            piz_l_cpy = list(filter((0).__ne__, piz_l_cpy))
            print(piz_l_cpy)
            total_deliveries += 1
            total_value += dp[1]
        else:
            print("pizzas less then members!")
            print(piz_l_cpy)
        team_index += 1

    if total_value > result["value"]:
        result["value"] = total_value
        result["deliveries"] = total_deliveries
        result["piz_to_team"].clear()
        result["piz_to_team"] = piz_to_team.copy()
    elif total_value == result["value"] and total_deliveries > result["deliveries"]:
        result["deliveries"] = total_deliveries
        result["piz_to_team"].clear()
        result["piz_to_team"] = piz_to_team.copy()
    print(f"For order {order}:")
    print(f"Total deliveries are {total_deliveries}")
    print(f"Total value is {total_value}")

print("THAT IS ALL!")
print(result)

make_out_file(result, file_name)
