#BEFORE HINT

#Question Pattern : 0 / 1 Knapsack Probles
#Solution : Dynamic Programming
def smallest_sufficient_team(skills_required, people):

    def dp(skills_rem, i): 
        #Base Case 1 
        if not skills_rem: 
            return 0 
        if i == len(people): 
            return float('inf')
        
        person_skill = people[i]
        #Case 1. people[i] joins the team 
        join_team = 1 + dp(skills_rem.difference(person_skill), i + 1)
        #Case 2. Don't join
        dont_join_team = dp(skills_rem, i + 1)

        return min(join_team, dont_join_team)

    return dp(skills_required, 0)

    res = dp(skills_required, 0)
    team_not_possible = res == float('inf')
    if team_not_possible: 
        return -1 
    else: 
        return res 