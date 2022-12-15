# %% [markdown]
# # Part One & Two

# %%
file = open('./Input/Day10_Input.txt', 'r')

contents = file.read()
cmds = contents.split('\n')
crt = [[],[],[],[],[],[]]

for r in crt:
    pxl_ct = 1

    while pxl_ct <= 40:
        r.append('.')

        pxl_ct = pxl_ct + 1

# %%
def process_strength_interval(ct, intervals, addx, strengths):
    if ct in intervals:
        signal_strength = 0

        for num in addx:
            signal_strength = signal_strength + num

        strengths.append(ct * signal_strength)

    return strengths

def move_pixel(ct, row_ix, col_ix, intervals):
    if ct in intervals:
        # Move to next row
        row_ix = row_ix + 1
        col_ix = 0
    else:
        # Move to the right within current row
        col_ix = col_ix + 1

    return row_ix, col_ix

def start_circuit(cmds, crt):
    cmd_ct = len(cmds)
    cmd_ix = 0
    cycle_ct = 0
    cycle_target = 0
    addx_values = [1]
    cycle_wait = False
    signal_intervals = [20, 60, 100, 140, 180, 220]
    signal_strengths = []
    crt_intervals = [40, 80, 120, 160, 200, 240]
    crt_row_ix = 0
    crt_col_ix = 0
    sprite_cntr = 1

    while True:
        cycle_ct = cycle_ct + 1

        left_pxl = sprite_cntr - 1
        right_pxl = sprite_cntr + 1
        sprite = [left_pxl, sprite_cntr, right_pxl]

        if crt_col_ix in sprite:
            # Light up that pixel!
            crt[crt_row_ix][crt_col_ix] = '#'

        if cycle_ct == cycle_target:
            cycle_wait = False

        if cmds[cmd_ix] == 'noop':
            signal_strengths = process_strength_interval(cycle_ct, signal_intervals, addx_values, signal_strengths)

            cmd_ix = cmd_ix + 1
        else:
            signal_strengths = process_strength_interval(cycle_ct, signal_intervals, addx_values, signal_strengths)

            if cycle_target < cycle_ct:
                v = int(cmds[cmd_ix].split(' ')[1])
                cycle_target = cycle_ct + 1
                cycle_wait = True
            else:
                if cycle_wait == False:
                    # Finish addx exec
                    addx_values.append(v)
                    sprite_cntr = sprite_cntr + v
                    cmd_ix = cmd_ix + 1

        if cycle_ct == 240:
            sig_strength_sum = sum(signal_strengths)

            return sig_strength_sum, crt
        else:
            crt_row_ix, crt_col_ix = move_pixel(cycle_ct, crt_row_ix, crt_col_ix, crt_intervals)

# %%
sig_strength_sum, crt = start_circuit(cmds, crt)

print(f"Answer (part one) - The sum of the signal strengths is {sig_strength_sum}\n")

print(f"Answer (part two) - 8 capital letters shown below:")

for r in crt:
    print(r)


