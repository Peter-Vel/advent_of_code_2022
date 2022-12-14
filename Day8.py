# %% [markdown]
# # Part One & Two

# %%
file = open('./Input/Day8_Input.txt', 'r')

contents = file.read()
data = contents.split("\n")
scenic_scores = []

# %%
def get_edge_tree_ct(row_ct):
    edge_tree_ct = 0
    ct = 0
    
    while ct < row_ct:
        if (ct == 1) or (ct == row_ct - 1): # First or last row of trees
            edge_tree_ct = edge_tree_ct + len(data[ct])
        else:
            edge_tree_ct = edge_tree_ct + 2

        ct = ct + 1

    return edge_tree_ct

def new_front_back_arr(row_ct, row_ix):
    front_back_row_ixs = []
    ct = 0

    while ct < row_ct:
        if ct != row_ix:
            front_back_row_ixs.append(ct)

        ct = ct + 1

    return front_back_row_ixs

def new_left_right_arr(tree_ct, tree_ix):
    left_right_tree_ixs = []
    ct = 0

    while ct < tree_ct:
        if ct != tree_ix:
            left_right_tree_ixs.append(ct)

        ct = ct + 1

    return left_right_tree_ixs

def get_viewing_distance(tree_ix, row_ix, tree_ct_per_row, row_ct, direction, tree):
    viewing_distance = 0

    if direction == 'left' or direction == 'front':
        increment_ix = tree_ix - 1 if direction == 'left' else row_ix - 1

        if increment_ix >= 0:
            while increment_ix >= 0:
                comp_tree = int(data[row_ix][increment_ix]) if direction == 'left' else int(data[increment_ix][tree_ix])
                viewing_distance = viewing_distance + 1

                if comp_tree >= tree:
                    break
                    
                increment_ix = increment_ix - 1
    else:
        increment_ix = tree_ix + 1 if direction == 'right' else row_ix + 1
        end_ix = tree_ct_per_row - 1 if direction == 'right' else row_ct - 1

        if increment_ix <= end_ix:
            while increment_ix <= end_ix:
                comp_tree = int(data[row_ix][increment_ix]) if direction == 'right' else int(data[increment_ix][tree_ix])
                viewing_distance = viewing_distance + 1

                if comp_tree >= tree:
                    break
                    
                increment_ix = increment_ix + 1

    return viewing_distance

def get_scenic_score(row_ix, tree_ix, tree_ct_per_row, row_ct, tree):
    left_viewing_distance = get_viewing_distance(tree_ix, row_ix, tree_ct_per_row, row_ct, 'left', tree)
    right_viewing_distance = get_viewing_distance(tree_ix, row_ix, tree_ct_per_row, row_ct, 'right', tree)
    front_viewing_distance = get_viewing_distance(tree_ix, row_ix, tree_ct_per_row, row_ct, 'front', tree)
    back_viewing_distance = get_viewing_distance(tree_ix, row_ix, tree_ct_per_row, row_ct, 'back', tree)

    scenic_score = left_viewing_distance * right_viewing_distance * front_viewing_distance * back_viewing_distance

    return scenic_score

def analyze_trees(data):
    row_ct = len(data)
    tree_ct_per_row = len(data[0])
    trees_w_visibility = 0
    row_ix = 1

    edge_tree_ct = get_edge_tree_ct(row_ct)

    while row_ix <= row_ct - 2: # Second-second to last row of trees
        row = data[row_ix]

        # Get all row indexes other than the one we're currently on
        front_back_row_ixs = new_front_back_arr(row_ct, row_ix)

        tree_ix = 1

        while tree_ix <= tree_ct_per_row - 2: # Second-second to last tree within the row
            tree = int(data[row_ix][tree_ix])
            left_right_tree_ixs = new_left_right_arr(tree_ct_per_row, tree_ix)

            # Check left-right tree visibility
            left_visibility = True
            right_visibility = True

            for lr in left_right_tree_ixs:
                compare_ix = int(lr)
                compare_tree = int(data[row_ix][lr])
                
                if compare_ix < tree_ix:
                    # Tree is to the left
                    if compare_tree >= tree:
                        left_visibility = False
                else:
                    # Tree is to the right
                    if compare_tree >= tree:
                        right_visibility = False

            # Check front-back tree visibility
            front_visibility = True
            back_visibility = True

            for fb in front_back_row_ixs:
                compare_ix = int(fb)
                compare_tree = int(data[fb][tree_ix])

                if compare_ix < row_ix:
                    # Tree is in front
                    if compare_tree >= tree:
                        front_visibility = False
                else:
                    # Tree is behind
                    if compare_tree >= tree:
                        back_visibility = False

            # Add current tree if visible from either the front, back, left, or right
            if ((left_visibility == True) or (right_visibility == True) 
                or (front_visibility == True) or (back_visibility == True)):
                trees_w_visibility = trees_w_visibility + 1

            # Get the scenic score for this tree (part two)
            scenic_score = get_scenic_score(row_ix, tree_ix, tree_ct_per_row, row_ct, tree)
            scenic_scores.append(scenic_score)

            tree_ix = tree_ix + 1

        row_ix = row_ix + 1

    visible_trees = trees_w_visibility + edge_tree_ct

    return visible_trees


# %%
visible_trees = analyze_trees(data)

print(f"Answer (part one) - How many trees are visible from outside of the forest: {visible_trees}")
print(f"Answer (part two) - Highest scenic score possible: {max(scenic_scores)}")


