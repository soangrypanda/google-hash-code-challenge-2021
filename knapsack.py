# THIS MODULE IS APPLIED TO EVERY TEAM IN A GIVEN TEAMS' ORDER.

# This module applies the algorithm for finding a maximum value for remaining pizzas given the constraint.
# It also marks the exact pizzas that make the value.
# Value of a combination is the length of a set of ingredients derived from pizzas in the combination.
# Constraint is the number of pizzas we can have in one combination (the number of team members).
# We solve it via dynamic programming voodoo.
# There is a matrix "dp", that holds pizzas' indexes and total value of the indexed pizzas (combination).
# Sub-problems are made of pizzas and weights. Each cell represents a state of a given sub-problem.
# Question for a sub-problem is the max value we can get with:
#           current weight or less and
#           current pizza and, possibly, already seen pizzas.
# On each layer we consider a pizza. We can either take a pizza + previous pizzas of a remaining weight, OR
# Previous pizzas of a current weight, depends on what has a bigger value.
# In case current storage is less than a weight of a pizza, we do nothing.
# What is great is that a weight of any pizza is always 1.

def dp_pizzas(problem, team_len):
    piz_len = len(problem)
    print(f"len of problem is {piz_len}")
    print(f"team_len is {team_len}")
    if piz_len < team_len:
        sad_return = (set(), 0)
        return sad_return
    one_pizza_size = 1

    dp = []
    for i in range(0, piz_len+1):
        line = []
        for j in range(0, team_len+1):
            line.append([set(), 0])
        dp.append(line)

    for i in range(piz_len - 1, -1, -1):
        for j in range(0, team_len + 1):
            len1 = dp[i + 1][j][1]
            if j >= one_pizza_size:
                u_ing = set()
                u_ing.update(problem[i][0])
                for x in dp[i+1][j-one_pizza_size][0]:
                    u_ing.update(problem[x][0])
                len2 = len(u_ing)
                if len1 > len2:
                    dp[i][j][0] = dp[i+1][j][0].copy()
                    dp[i][j][1] = len1
                else:
                    dp[i][j][0] = dp[i+1][j-one_pizza_size][0].copy()
                    dp[i][j][0].add(i)
                    dp[i][j][1] = len2
            else:
                # technically, this branch is redundant in a case of this particular problem as
                # all the cases falling into this branch are initially set to 0.
                # and all these cases are 1) empty suffix and 2) 0 size knapsack.
                dp[i][j][0] = dp[i + 1][j][0].copy()
                dp[i][j][1] = len1
    return dp[0][team_len]
