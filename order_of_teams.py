# THIS MODULE IS APPLIED TO THE LIST OF ALL TEAMS

# This module uses dp to calculate the list of teams that would consume the most number of pizzas possible.
# So we do not need permutations of teams as we can find A best permutation at the outset.
# For description on how dp works see knapsack.py.
# Algorithms are duplicated as there are subtle differences in datastructures - probably will generalize it later.

from copy import deepcopy


def dp_teams(problem, no_of_piz):
    print(f"Entering dp_teams with no of pizzas {no_of_piz}...")

    no_of_teams = len(problem)
    # if no_of_piz < no_of_teams:
    #    sad_return = (list(), 0)
    #    return sad_return

    dp_empty = list()
    for i in range(0, no_of_piz+1):
        dp_empty.append([list(), 0])
    dp_cur = deepcopy(dp_empty)
    dp_prev = deepcopy(dp_empty)

    for i in range(no_of_teams - 1, -1, -1):
        dp_prev.clear()
        dp_prev = deepcopy(dp_cur)
        dp_cur.clear()
        dp_cur = deepcopy(dp_empty)

        for j in range(0, no_of_piz + 1):
            len1 = dp_prev[j][1]

            if j >= problem[i]:
                u_ing = list()
                u_ing.append(problem[i])
                for x in dp_prev[j-problem[i]][0]:
                    u_ing.append(problem[x])

                len2 = len(u_ing)

                if len1 > len2:
                    dp_cur[j][0] = deepcopy(dp_prev[j][0])
                    dp_cur[j][1] = len1
                else:
                    dp_cur[j][0] = deepcopy(dp_prev[j-problem[i]][0])
                    dp_cur[j][0].append(problem[i])
                    dp_cur[j][1] = len2

            else:
                dp_cur[j][0] = deepcopy(dp_prev[j][0])
                dp_cur[j][1] = len1

    print("dp_teams is ready to return!")
    return dp_cur[no_of_piz]


# Below are the functions first written to find all unique permutations of teams.
# Algorithm is naive and, what is more important, over the top as we do not need to find ALL the permutations.


def do_teams_orders(inp_teams, permutation, orders_of_teams):
    if len(inp_teams) == 0:
        orders_of_teams.add(tuple(permutation))
    else:
        for i in range(0, len(inp_teams)):
            teams = inp_teams.copy()
            perm = permutation.copy()
            team = teams.pop(i)
            perm.append(team)
            do_teams_orders(teams, perm, orders_of_teams)


def give_all_teams_orders(teams):
    print("Entering give_all_team_orders...")
    orders_of_teams = set()
    permutation = list()
    do_teams_orders(teams, permutation, orders_of_teams)
    return orders_of_teams
