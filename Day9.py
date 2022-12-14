# %% [markdown]
# # Part One

# %%
import pandas as pd

# %%
file = open('./Input/Day9_Input.txt', 'r')

contents = file.read()
data = contents.split("\n")

# %%
# Main grid (list of lists) that we'll expand dynamically
grid = [['sht']] # s = Starting point, h = Head, t = tail

# %%
def new_head_destination(head, direction, steps):
    row_ix = head[0]
    col_ix = head[1]
    curr_row_len = len(grid)
    curr_col_len = len(grid[0])

    # Remove 'h' from current position
    grid[row_ix][col_ix] = grid[row_ix][col_ix].replace('h','')

    # Left
    if direction == 'L':
        dest_col_ix = col_ix - steps

        if dest_col_ix < 0:
            # Expand to the left
            amt_of_cols_needed = 0 - (dest_col_ix)
            step_ct = 0

            while step_ct < amt_of_cols_needed:
                for row in grid:
                    row.insert(0, '')

                step_ct = step_ct + 1

            # We had to expand, so we know the column index is the farthest left
            head = [row_ix, 0]
        else:
            # Destination index exists
            head = [row_ix, dest_col_ix]
    # Right
    elif direction == 'R':
        dest_col_ix = col_ix + steps

        if dest_col_ix >= curr_col_len:
            # Expand to the right
            amt_of_cols_needed = (dest_col_ix + 1) - curr_col_len
            step_ct = 0

            while step_ct < amt_of_cols_needed:
                for row in grid:
                    row.append('')

                step_ct = step_ct + 1

        head = [row_ix, dest_col_ix]
    # Up
    elif direction == 'U':
        dest_row_ix = row_ix - steps

        if dest_row_ix < 0:
            # Expand up
            amt_of_cols_needed = 0 - (dest_row_ix)
            step_ct = 0

            while step_ct < amt_of_cols_needed:
                grid.insert(0, [])

                col_ct = 0

                while col_ct < curr_col_len:
                    grid[0].append('')

                    col_ct = col_ct + 1

                step_ct = step_ct + 1

            head = [0, col_ix]
        else:
            head = [dest_row_ix, col_ix]
    # Down
    else:
        dest_row_ix = row_ix + steps

        if dest_row_ix >= curr_row_len:
            # Expand down
            amt_of_cols_needed = (dest_row_ix + 1) - curr_row_len
            step_ct = 0

            while step_ct < amt_of_cols_needed:
                grid.append([])

                col_ct = 0

                while col_ct < curr_col_len:
                    grid[-1].append('')

                    col_ct = col_ct + 1

                step_ct = step_ct + 1

        head = [dest_row_ix, col_ix]

    new_row_ix = head[0]
    new_col_ix = head[1]

    # Add 'h' to new position
    if 'h' not in grid[new_row_ix][new_col_ix]:
        grid[new_row_ix][new_col_ix] = grid[new_row_ix][new_col_ix] + 'h'

    return head

def get_tail_position():
    for r in grid:
        row_ix = grid.index(r)
        for x in r:
            col_ix = r.index(x)
            if 't' in x:
                tail = [row_ix, col_ix]

    return tail

def mark_trail(row_ix, col_ix):
    if '#' not in grid[row_ix][col_ix] and 's' not in grid[row_ix][col_ix]:
        grid[row_ix][col_ix] = grid[row_ix][col_ix] + '#'

def set_tail(row_ix, col_ix):
    if 't' not in grid[row_ix][col_ix]:
        grid[row_ix][col_ix] = grid[row_ix][col_ix] + 't'

def new_tail_destination(head, tail, direction, recurse = False):
    head_row_ix = head[0]
    head_col_ix = head[1]

    tail_row_ix = tail[0]
    tail_col_ix = tail[1]

    # Remove 't' from current position
    grid[tail_row_ix][tail_col_ix] = grid[tail_row_ix][tail_col_ix].replace('t','')

    mark_trail(tail_row_ix, tail_col_ix)

    # Left
    if direction == 'L':
        if head_row_ix == tail_row_ix:
            # 'h' and 't' are on the same row
            target_col_ix = head_col_ix + 1
            steps = tail_col_ix - target_col_ix
            step_ct = 0
            step_ix = tail_col_ix - 1

            while step_ct < steps and step_ix >= target_col_ix:
                mark_trail(tail_row_ix, step_ix)

                step_ix = step_ix - 1
                step_ct = step_ct + 1

            tail = [tail_row_ix, target_col_ix]
        elif head_col_ix < tail_col_ix - 1:
            # 'h' has travelled at least two rows over
            # 't' will jump diagonally into h's row
            mark_trail(tail_row_ix, tail_col_ix)

            target_row_ix = head_row_ix
            tail = [target_row_ix, tail_col_ix - 1]
            new_tail_row_ix = tail[0]
            new_tail_col_ix = tail[1]

            set_tail(new_tail_row_ix, new_tail_col_ix)

            if head_col_ix < new_tail_col_ix:
                tail = new_tail_destination(head, tail, direction, True)
    # Right
    elif direction == 'R':
        if head_row_ix == tail_row_ix:
            target_col_ix = head_col_ix - 1
            steps = tail_col_ix + target_col_ix
            step_ct = 0
            step_ix = tail_col_ix + 1

            while step_ct < steps and step_ix <= target_col_ix:
                mark_trail(tail_row_ix, step_ix)

                step_ix = step_ix + 1
                step_ct = step_ct + 1

            tail = [tail_row_ix, target_col_ix]
        elif head_col_ix > tail_col_ix + 1:
            mark_trail(tail_row_ix, tail_col_ix)

            target_row_ix = head_row_ix
            tail = [target_row_ix, tail_col_ix + 1]
            new_tail_row_ix = tail[0]
            new_tail_col_ix = tail[1]

            set_tail(new_tail_row_ix, new_tail_col_ix)

            if head_col_ix > new_tail_col_ix:
                tail = new_tail_destination(head, tail, direction, True)
    # Up
    elif direction == 'U':
        if head_col_ix == tail_col_ix:
            if recurse:
                # This means 't' came from a diagonal and we fed the new values back into this function
                # We need to start from one row down, due to the step_ix increment below
                tail_row_ix = tail_row_ix + 1

            # 'h' and 't' are on the same column
            target_row_ix = head_row_ix + 1
            steps = tail_row_ix - target_row_ix
            step_ct = 0
            step_ix = tail_row_ix - 1

            while step_ct < steps and step_ix >= target_row_ix:
                mark_trail(step_ix, tail_col_ix)

                step_ix = step_ix - 1
                step_ct = step_ct + 1

            tail = [target_row_ix, tail_col_ix]
        elif head_row_ix < tail_row_ix - 1:
            # 'h' has travelled at least two rows up
            # 't' will jump diagonally into h's column
            mark_trail(tail_row_ix, tail_col_ix)
            
            target_row_ix = tail_row_ix - 1
            tail = [target_row_ix, head_col_ix]
            new_tail_row_ix = tail[0]
            new_tail_col_ix = tail[1]
            
            set_tail(new_tail_row_ix, new_tail_col_ix)

            if head_row_ix < new_tail_row_ix:
                # 'h' and 't' are in the same column now, but 't' may have more to travel
                # Feed this new data back into this same function with recurse = True
                tail = new_tail_destination(head, tail, direction, True)
    # Down
    else:
        if head_col_ix == tail_col_ix:
            if recurse:
                tail_row_ix = tail_row_ix - 1
            target_row_ix = head_row_ix - 1
            steps = target_row_ix - tail_row_ix
            step_ct = 0
            step_ix = tail_row_ix + 1

            while step_ct < steps and step_ix <= target_row_ix:
                mark_trail(step_ix, tail_col_ix)

                step_ix = step_ix + 1
                step_ct = step_ct + 1

            tail = [target_row_ix, tail_col_ix]
        elif head_row_ix > tail_row_ix + 1:
            mark_trail(tail_row_ix, tail_col_ix)

            target_row_ix = tail_row_ix + 1
            tail = [target_row_ix, head_col_ix]
            new_tail_row_ix = tail[0]
            new_tail_col_ix = tail[1]

            set_tail(new_tail_row_ix, new_tail_col_ix)

            if head_row_ix > new_tail_row_ix:
                tail = new_tail_destination(head, tail, direction, True)

    new_tail_row_ix = tail[0]
    new_tail_col_ix = tail[1]

    set_tail(new_tail_row_ix, new_tail_col_ix)

    return tail

# %%
# Default (current) location index points
head = [0, 0]
tail = [0, 0]

for m in data:
    move = m.split(' ')
    direction = move[0]
    steps = int(move[1])

    head = new_head_destination(head, direction, steps)
    tail = get_tail_position()
    
    if head != tail:
        tail = new_tail_destination(head, tail, direction)

grid_rows = len(grid)
grid_cols = len(grid[0])

print(f"The grid has {grid_rows} rows and {grid_cols} columns")
print(f"Head position: {head}")
print(f"Tail position: {tail}")

# %%
df = pd.DataFrame(grid)
pd.set_option('display.max_rows', grid_rows)
pd.set_option('display.max_columns', grid_cols)
pd.set_option('display.width', 1250)
print(df)

# %%
trail_ct = 1 # Starting at 1 because of the 's' (starting) point

for r in grid:
    for c in r:
        if '#' in c:
            trail_ct = trail_ct + 1

print(f"Answer (part one) - The tail of the rope visited a total of {trail_ct} positions at least once")


