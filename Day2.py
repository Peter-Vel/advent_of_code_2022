# %% [markdown]
# # Part One

# %%
file = open('./Input/Day2_Input.txt', 'r')

contents = file.read()
data = contents.split("\n")

# %%
opp_dict = {'A': 'Rock', 'B': 'Paper', 'C': 'Scissors'}
me_dict = {'X': 'Rock', 'Y': 'Paper', 'Z': 'Scissors'}
base_score_dict = {'Rock': 1, 'Paper': 2, 'Scissors': 3}

# %%
def get_round_outcome(opp_ansr, my_ansr):
    if opp_ansr == my_ansr:
        outcome = 'Draw'
    else:
        if opp_ansr == 'Rock':
            if my_ansr == 'Paper':
                outcome = 'Win'
            else:                
                outcome = 'Loss'
        elif opp_ansr == 'Paper':
            if my_ansr == 'Scissors':
                outcome = 'Win'
            else:
                outcome = 'Loss'
        else:
            if my_ansr == 'Rock':
                outcome = 'Win'
            else:
                outcome = 'Loss'

    return outcome


# %%
total_score = 0

for r in data:
    round = r.split(' ')
    opp = round[0]
    me = round[1]

    opp_ansr = opp_dict[opp]
    my_ansr = me_dict[me]
    outcome = get_round_outcome(opp_ansr, my_ansr)
    
    shape_score = base_score_dict[my_ansr]
    outcome_score = 0 if outcome == 'Loss' else 3 if outcome == 'Draw' else 6
    round_score = shape_score + outcome_score
    total_score = total_score + round_score

print(f"My total (part one) score: {total_score}")


# %% [markdown]
# # Part Two

# %%
def get_shape(opp_ansr, outcome):
    if outcome == 'Loss':
        if opp_ansr == 'Rock':
            shape = 'Scissors'
        elif opp_ansr == 'Paper':
            shape = 'Rock'
        else:
            shape = 'Paper'
    elif outcome == 'Draw':
        shape = opp_ansr
    else:
        if opp_ansr == 'Rock':
            shape = 'Paper'
        elif opp_ansr == 'Paper':
            shape = 'Scissors'
        else:
            shape = 'Rock'

    return shape

# %%
total_score = 0

for r in data:
    round = r.split(' ')
    opp = round[0]
    me = round[1]

    if me == 'X':
        outcome = 'Loss'
        outcome_score = 0
    elif me == 'Y':
        outcome = 'Draw'
        outcome_score = 3
    else:
        outcome = 'Win'
        outcome_score = 6

    opp_ansr = opp_dict[opp]
    
    shape = get_shape(opp_ansr, outcome)
    
    shape_score = base_score_dict[shape]
    round_score = shape_score + outcome_score
    total_score = total_score + round_score

print(f"My total (part two) score: {total_score}")



