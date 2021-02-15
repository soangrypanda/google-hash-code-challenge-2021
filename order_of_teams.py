# THIS MODULE IS APPLIED TO THE LIST OF ALL TEAMS

# This module is calculating all the unique permutations of teams possible. 
# If there are multiple teams with equivalent number of members, there would be similar permutations. 
# We take only one of such similar permutations as we are interested in unique teams' orders.


def do_teams_orders(inp_teams, permutation, orders_of_teams):
    if len(inp_teams) == 0:
        orders_of_teams.add(tuple(permutation))
        print(orders_of_teams)
    else:
        for i in range(0, len(inp_teams)):
            teams = inp_teams.copy()
            perm = permutation.copy()
            team = teams.pop(i)
            perm.append(team)
            print(teams, perm)
            do_teams_orders(teams, perm, orders_of_teams)


def give_all_teams_orders(teams):
    orders_of_teams = set()
    permutation = list()
    do_teams_orders(teams, permutation, orders_of_teams)
    return orders_of_teams
