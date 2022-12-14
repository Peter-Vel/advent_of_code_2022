# %% [markdown]
# # Part One

# %%
import re

# %%
file = open('./Input/Day5_Input.txt', 'r')

contents = file.read()
data = contents.split("\n")

# %%
stacks = {
    1: ['P', 'D', 'Q', 'R', 'V', 'B', 'H', 'F'],
    2: ['V', 'W', 'Q', 'Z', 'D', 'L'],
    3: ['C', 'P', 'R', 'G', 'Q', 'Z', 'L', 'H'],
    4: ['B', 'V', 'J', 'F', 'H', 'D', 'R'],
    5: ['C', 'L', 'W', 'Z'],
    6: ['M', 'V', 'G', 'T', 'N', 'P', 'R', 'J'],
    7: ['S', 'B', 'M', 'V', 'L', 'R', 'J'],
    8: ['J', 'P', 'D'],
    9: ['V', 'W', 'N', 'C', 'D']
}

# %%
def move_crates(amt, src, dest):
    ct = 1

    while ct <= amt:
        src_crate = stacks[src][0]
        del stacks[src][0]
        stacks[dest].insert(0, src_crate)

        ct = ct + 1

# %%
for p in data:
    params = re.findall(r'\d+', f"{p}")
    amt = int(params[0])
    src = int(params[1])
    dest = int(params[2])

    move_crates(amt, src, dest)

# %%
print(f"Crates on top (part one): {stacks[1][0]}{stacks[2][0]}{stacks[3][0]}{stacks[4][0]}{stacks[5][0]}{stacks[6][0]}{stacks[7][0]}{stacks[8][0]}{stacks[9][0]}")

# %% [markdown]
# # Part Two

# %%
stacks = {
    1: ['P', 'D', 'Q', 'R', 'V', 'B', 'H', 'F'],
    2: ['V', 'W', 'Q', 'Z', 'D', 'L'],
    3: ['C', 'P', 'R', 'G', 'Q', 'Z', 'L', 'H'],
    4: ['B', 'V', 'J', 'F', 'H', 'D', 'R'],
    5: ['C', 'L', 'W', 'Z'],
    6: ['M', 'V', 'G', 'T', 'N', 'P', 'R', 'J'],
    7: ['S', 'B', 'M', 'V', 'L', 'R', 'J'],
    8: ['J', 'P', 'D'],
    9: ['V', 'W', 'N', 'C', 'D']
}

# %%
def get_crates_to_move(amt, src):
    ct = 0
    crates_to_move = []

    while ct < amt:
        src_crate = stacks[src][ct]
        crates_to_move.insert(ct, src_crate)

        ct = ct + 1

    return crates_to_move


# %%
for p in data:
    params = re.findall(r'\d+', f"{p}")
    amt = int(params[0])
    src = int(params[1])
    dest = int(params[2])

    crates_to_move = get_crates_to_move(amt, src)
    del stacks[src][0:amt]
    stacks[dest] = crates_to_move + stacks[dest]

# %%
print(f"Crates on top (part two): {stacks[1][0]}{stacks[2][0]}{stacks[3][0]}{stacks[4][0]}{stacks[5][0]}{stacks[6][0]}{stacks[7][0]}{stacks[8][0]}{stacks[9][0]}")


