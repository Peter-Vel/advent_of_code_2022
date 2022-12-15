# %% [markdown]
# # Part One

# %%
file = open('./Input/Day10_Input.txt', 'r')

contents = file.read()
cmds = contents.split("\n")

# %%
cmd_ct = len(cmds)
cmd_ix = 0
cycle_ct = 0
cycle_target = 0
addx_values = [1]
cycle_wait = False
signal_intervals = [20, 60, 100, 140, 180, 220]
signal_strengths = []

# %%
def process_interval(ct, intervals, addx, strengths):
    if ct in intervals:
        signal_strength = 0

        for num in addx:
            signal_strength = signal_strength + num

        strengths.append(ct * signal_strength)

    return strengths

# %%
while True:
    cycle_ct = cycle_ct + 1

    if cycle_ct == cycle_target:
        cycle_wait = False

    if cmds[cmd_ix] == 'noop':
        signal_strengths = process_interval(cycle_ct, signal_intervals, addx_values, signal_strengths)

        cmd_ix = cmd_ix + 1
    else:
        signal_strengths = process_interval(cycle_ct, signal_intervals, addx_values, signal_strengths)

        if cycle_ct == 220:
            break

        if cycle_target < cycle_ct:
            v = int(cmds[cmd_ix].split(' ')[1])
            cycle_target = cycle_ct + 1
            cycle_wait = True
        else:
            if cycle_wait == False:
                # Finish addx exec
                addx_values.append(v)
                cmd_ix = cmd_ix + 1

sig_strength_sum = sum(signal_strengths)

print(f"Answer (part one) - The sum of the signal strengths is {sig_strength_sum}")


