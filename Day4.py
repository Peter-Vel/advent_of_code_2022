# %% [markdown]
# # Part One

# %%
file = open('./Input/Day4_Input.txt', 'r')

contents = file.read()
data = contents.split("\n")

# %%
def build_section_range(sections):
    begin = int(sections.split('-')[0])
    end = int(sections.split('-')[1])
    section_lst = list(range(begin, end + 1))

    return section_lst

# %%
pairs_to_reconsider = 0

for p in data:
    elf_one = p.split(',')[0]
    elf_two = p.split(',')[1]

    elf_one_sections = build_section_range(elf_one)
    elf_two_sections = build_section_range(elf_two)
    elf_one_overlap_chk = all(s in elf_two_sections for s in elf_one_sections)
    elf_two_overlap_chk = all(s in elf_one_sections for s in elf_two_sections)
    
    if elf_one_overlap_chk == True or elf_two_overlap_chk == True:
        pairs_to_reconsider = pairs_to_reconsider + 1

print(f"Total pairs where one assignment fully contains the other: {pairs_to_reconsider}")

# %% [markdown]
# # Part Two

# %%
pairs_with_overlap = 0

for p in data:
    elf_one = p.split(',')[0]
    elf_two = p.split(',')[1]

    elf_one_sections = build_section_range(elf_one)
    elf_two_sections = build_section_range(elf_two)

    overlap_chk = any(s in elf_one_sections for s in elf_two_sections)

    if overlap_chk == True:
        pairs_with_overlap = pairs_with_overlap + 1

print(f"Pairs with any overlap: {pairs_with_overlap}")


