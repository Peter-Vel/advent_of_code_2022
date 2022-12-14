# %% [markdown]
# # Part One

# %%
import operator

# %%
file = open('./Input/Day1_Input.txt', 'r')

contents = file.read()
data = contents.split("\n")

# %%
elf_num = 1
elfs = {}

for i in data:
    if i != '':
        # check if a key for the current elf already exists
        if elf_num not in elfs.keys():
            # Add a new elf and the current value
            elfs[elf_num] = [i]
        else:
            # Append the current value to the current elf
            elfs[elf_num].append(i)
    else:
        elf_num = elf_num + 1

# %%
elf_num = 1
elf_cals = {}

for e in elfs.keys(): # 'e' for ELF!
    # Add up the elf's cals
    cals_to_int = [int(i) for i in elfs[e]]
    cals = sum(cals_to_int)
    
    elf_cals[elf_num] = cals
    elf_num = elf_num + 1

elf_w_most_cals = max(elf_cals.items(), key=operator.itemgetter(1))[0]

print(f"Elf with most calories: {elf_w_most_cals} -- Value: {elf_cals[elf_w_most_cals]}")

# %% [markdown]
# # Part Two

# %%
top_three = sorted(elf_cals, key=elf_cals.get, reverse=True)[:3]
top_three_cals = 0

print('Top three:')

for e in top_three:
    print(f"Elf: {e}, Value: {elf_cals[e]}")
    top_three_cals = top_three_cals + elf_cals[e]

print(f"\nTop three total: {top_three_cals}")


