from parse import *
from knapsack import *
from order_or_teams import *
from out import *

dir_path = Path(__file__).parent.absolute()
inp_files, inp_path = give_inp_files(dir_path)
out_path = handle_out_dir(dir_path)

for file_name in inp_files:
    (meta, pizzas_list, ing_total) = parse_file(inp_path / file_name)

    print(meta)
    print(f"ing total is {ing_total}")

    meta_cpy = meta.copy()
    del meta_cpy[1]
    all_teams = []
    for key, value in meta_cpy.items():
        for i in range(0, int(value)):
            all_teams.append(key)
    print(f"no of teams is {len(all_teams)}")

    no_of_pizzas = int(meta[1])
    print(f"no of pizzas is {no_of_pizzas}")

    optimal_order = dp_teams(all_teams, no_of_pizzas)
    print(optimal_order)
    teams_to_deliver = optimal_order[0]

    result = {"value": 0, "deliveries": 0, "piz_to_team": list()}
    piz_l_cpy = pizzas_list.copy()
    team_index = 0
    total_deliveries = 0
    total_value = 0
    piz_to_team = list()
    order_len = len(teams_to_deliver)
    while len(piz_l_cpy) >= 2 and team_index < order_len:
        members = teams_to_deliver[team_index]
        pizzas_indexes = list()
        dp = dp_pizzas(piz_l_cpy, members)
        if dp[1] != 0:
            # print(f"for team of {members} max value of pizzas is {dp[1]} with the following pizzas:")
            for i in dp[0]:
                # print(piz_l_cpy[i])
                pizzas_indexes.append(piz_l_cpy[i][1])
                piz_l_cpy[i] = 0
            piz_to_team.append((members, pizzas_indexes))
            # print(piz_l_cpy)
            piz_l_cpy = list(filter((0).__ne__, piz_l_cpy))
            # print(piz_l_cpy)
            total_deliveries += 1
            total_value += dp[1]
        # else:
            # print("pizzas less then members!")
            # print(piz_l_cpy)
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
    print(f"For order {teams_to_deliver}:")
    print(f"Total deliveries are {total_deliveries}")
    print(f"Total value is {total_value}")
    print(f"Pizzas left: {piz_l_cpy}")

    print("THAT IS ALL!")
    print(result)

    make_out_file(result, file_name, out_path)
print("End of program!")
