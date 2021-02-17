# THIS MODULE IS APPLIED TO THE LIST OF ALL TEAMS

# This module is calculating all the unique permutations of teams possible.
# If there are multiple teams with equivalent number of members, there would be similar permutations.
# We take only one of such similar permutations as we are interested in unique teams' orders.


def do_teams_orders(inp_teams, permutation, orders_of_teams):
    if len(inp_teams) == 0:
        orders_of_teams.add(tuple(permutation))
        #  print(orders_of_teams)
    else:
        for i in range(0, len(inp_teams)):
            teams = inp_teams.copy()
            perm = permutation.copy()
            team = teams.pop(i)
            perm.append(team)
            #  print(teams, perm)
            do_teams_orders(teams, perm, orders_of_teams)


def give_all_teams_orders(teams):
    print("enter team orders mod")
    orders_of_teams = set()
    permutation = list()
    do_teams_orders(teams, permutation, orders_of_teams)
    return orders_of_teams


def dp_teams(problem, no_of_piz):
    no_of_teams = len(problem)
    # print(f"len of problem is {no_of_teams}")
    # print(f"team_len is {no_of_piz}")
    if no_of_piz < no_of_teams:
        sad_return = (list(), 0)
        return sad_return

    dp = []
    for i in range(0, no_of_teams+1):
        line = []
        for j in range(0, no_of_piz+1):
            line.append([list(), 0])
        dp.append(line)

    for i in range(no_of_teams - 1, -1, -1):
        for j in range(0, no_of_piz + 1):
            len1 = dp[i + 1][j][1]
            if j >= problem[i]:
                u_ing = list()
                u_ing.append(problem[i])
                for x in dp[i+1][j-problem[i]][0]:
                    u_ing.append(problem[x])
                len2 = len(u_ing)
                if len1 > len2:
                    dp[i][j][0] = dp[i+1][j][0].copy()
                    dp[i][j][1] = len1
                else:
                    dp[i][j][0] = dp[i+1][j-problem[i]][0].copy()
                    dp[i][j][0].append(problem[i])
                    dp[i][j][1] = len2
            else:
                dp[i][j][0] = dp[i + 1][j][0].copy()
                dp[i][j][1] = len1
    return dp[0][no_of_piz]
