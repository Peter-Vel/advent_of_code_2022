# %% [markdown]
# # Part One

# %%
import string

# %%
file = open('./Input/Day6_Input.txt', 'r')

contents = file.read()
data = contents.split("\n")
data = data[0]

# %%
def get_marker(data, starting_ix, ending_ix):
    marker_found = False

    while marker_found == False:
        letters = data[starting_ix:ending_ix]
        letters_ux = set(letters)

        if len(letters) == len(letters_ux):
            marker_found = True
        else:
            starting_ix = starting_ix + 1
            ending_ix = ending_ix + 1

    return ending_ix

# %%
chars = get_marker(data, 0, 4)

print(f"Marker found after {chars} characters!")

# %% [markdown]
# # Part Two

# %%
chars = get_marker(data, 0, 14)

print(f"Message found after {chars} characters!")


