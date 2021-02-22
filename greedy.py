# I should tell you, this is a very, very shady way of solving this problem. If you need a normal way, look into
# order_or_teams.py - it is correct, but much slower.
# Lets call this module an "experimental approximation".
# But it still gives a list of teams for knapsack.py to process that is good.

def greedy(meta):
    pizzas = int(meta[1])
    two_t = int(meta[2])
    three_t = int(meta[3])
    four_t = int(meta[4])
    teams_to_deliver = list()
    teams = two_t + three_t + four_t

    pizzas_c = pizzas
    two_t_c = two_t
    three_t_c = three_t
    four_t_c = four_t

    while two_t_c - 1 >= 0 and pizzas_c - 2 >= 0:
        two_t_c -= 1
        pizzas_c -= 2
    while three_t_c - 1 >= 0 and pizzas_c - 3 >= 0:
        three_t_c -= 1
        pizzas_c -= 3
    while four_t_c - 1 >= 0 and pizzas_c - 4 >= 0:
        four_t_c -= 1
        pizzas_c -= 4

    print(pizzas_c, two_t_c, three_t_c, four_t_c)

    if pizzas_c == 0 or two_t_c + three_t_c + four_t_c == 0:
        pizzas_c = pizzas
        two_t_c = two_t
        three_t_c = three_t
        four_t_c = four_t
        while two_t_c - 1 >= 0 and pizzas_c - 2 >= 0:
            two_t_c -= 1
            pizzas_c -= 2
            teams_to_deliver.append(2)
        while three_t_c - 1 >= 0 and pizzas_c - 3 >= 0:
            three_t_c -= 1
            pizzas_c -= 3
            teams_to_deliver.append(3)
        while four_t_c - 1 >= 0 and pizzas_c - 4 >= 0:
            four_t_c -= 1
            pizzas_c -= 4
            teams_to_deliver.append(4)

    elif pizzas_c % 2 == 0 and teams % 2 == 0:
        prev_piz = pizzas_c
        prev_four = four_t_c
        pizzas_c = pizzas
        two_t_c = two_t
        three_t_c = three_t
        four_t_c = four_t

        for _ in range(int(prev_piz / 2 + (four_t - prev_four))):
            four_t_c -= 1
            pizzas_c -= 4
            teams_to_deliver.append(4)

        while two_t_c - 1 >= 0 and pizzas_c - 2 >= 0:
            two_t_c -= 1
            pizzas_c -= 2
            teams_to_deliver.append(2)
        while three_t_c - 1 >= 0 and pizzas_c - 3 >= 0:
            three_t_c -= 1
            pizzas_c -= 3
            teams_to_deliver.append(3)
        while four_t_c - 1 >= 0 and pizzas_c - 4 >= 0:
            four_t_c -= 1
            pizzas_c -= 4
            teams_to_deliver.append(4)

    elif pizzas_c % 2 == 0 and teams % 2 != 0:
        prev_piz = pizzas_c
        prev_four = four_t_c
        pizzas_c = pizzas
        two_t_c = two_t
        three_t_c = three_t
        four_t_c = four_t

        two_t_c -= 1
        pizzas_c -= 2
        teams_to_deliver.append(2)
        three_t_c -= 1
        pizzas_c -= 3
        teams_to_deliver.append(3)

        for _ in range(int(prev_piz + (four_t - prev_four))):
            four_t_c -= 1
            pizzas_c -= 4
            teams_to_deliver.append(4)

        while two_t_c - 1 >= 0 and pizzas_c - 2 >= 0:
            two_t_c -= 1
            pizzas_c -= 2
            teams_to_deliver.append(2)
        while three_t_c - 1 >= 0 and pizzas_c - 3 >= 0:
            three_t_c -= 1
            pizzas_c -= 3
            teams_to_deliver.append(3)
        while four_t_c - 1 >= 0 and pizzas_c - 4 >= 0:
            four_t_c -= 1
            pizzas_c -= 4
            teams_to_deliver.append(4)

    print(pizzas_c, two_t_c, three_t_c, four_t_c)
    return teams_to_deliver
