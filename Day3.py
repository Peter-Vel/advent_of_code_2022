# %% [markdown]
# # Part One

# %%
import string

# %%
file = open('./Input/Day3_Input.txt', 'r')

contents = file.read()
data = contents.split("\n")

# %%
def get_priority_dict(abc_list, case):
    priority_start = 1 if case == 'lower' else 27
    priority_counter = priority_start
    priority_dict = {}

    for l in abc_list:
        priority_dict[l] = priority_counter

        priority_counter = priority_counter + 1

    return priority_dict

# %%
lower_abc = list(string.ascii_lowercase)
upper_abc = list(string.ascii_uppercase)

lower_priorities = get_priority_dict(lower_abc, 'lower')
upper_priorities = get_priority_dict(upper_abc, 'upper')

# %%
total_priority = 0

for r in data:
    comp_len = int(len(r) / 2)
    comp_one = r[0:comp_len]
    comp_two = r[-comp_len:]
    common = list(set(comp_one) & set(comp_two))[0]
    priority = lower_priorities[common] if common in lower_abc else upper_priorities[common]
    total_priority = total_priority + priority

print(f"Total (part one) priority: {total_priority}")

# %% [markdown]
# # Part Two

# %%
grp_index = 0
elf_grps = []

while grp_index < len(data):
    elf_grp = data[grp_index], data[grp_index + 1], data[grp_index + 2]
    elf_grps.append(elf_grp)
    grp_index = grp_index + 3

total_priority = 0

for grp in elf_grps:
    elf_one = grp[0]
    elf_two = grp[1]
    elf_three = grp[2]
    group_letter = list(set(elf_one) & set(elf_two) & set(elf_three))[0]
    priority = lower_priorities[group_letter] if group_letter in lower_abc else upper_priorities[group_letter]
    total_priority = total_priority + priority

print(f"Total (part two) priority: {total_priority}")


