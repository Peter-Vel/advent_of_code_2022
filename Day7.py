# %% [markdown]
# # Part One

# %%
import json
import os

# %%
file = open('./Input/Day7_Input.txt', 'r')

contents = file.read()
data = contents.split("\n")

file_structure = {
    '/': {
        'type': 'dir'
    }
}

line_ix = 1
current_dir = file_structure['/']
breadcrumb = ['/']
dir_sizes = []

# %%
def get_contents(data, ix):
    ix = ix + 1
    data_len = len(data)
    item = data[ix]
    contents = []

    while '$ cd' not in item:
        contents.append(item)
        ix = ix + 1

        if ix != data_len:
            item = data[ix]
        else:
            break

    return contents, ix

def add_contents(file_structure, current_dir, contents):
    if 'contents' not in current_dir.keys():
        current_dir['contents'] = {}

    for i in contents:
        if 'dir' in i:
            dir_name = i.split(' ')[1]
            current_dir['contents'][dir_name] = {'type': 'dir'}
        else:
            file = i.split(' ')
            name = file[1]
            size = file[0]
            current_dir['contents'][name] = {'type': 'file', 'size': size}

def change_dir(line, file_structure, current_dir, breadcrumb):
    loc = line.split(' ')[2]
    
    if loc == '..':
        breadcrumb.pop()
        current_dir = file_structure

        for c in breadcrumb:
            if c == '/':
                current_dir = current_dir[c]
            else:
                current_dir = current_dir['contents'][c]
    else:
        if loc in current_dir['contents'].keys():
            new_loc = current_dir['contents'][loc]
            current_dir = new_loc
            breadcrumb.append(loc)

    return current_dir, breadcrumb

def recurse_dict(d, dir_name, size = 0):
    dict_ct = 0
    dir_size = 0

    for k, v in d.items():        
        if (isinstance(v, dict) and len(v) != 0 
            and v['type'] == 'dir'):
            dict_ct = dict_ct + 1
        elif (isinstance(v, dict) and len(v) != 0
              and v['type'] == 'file'):
            dir_size = dir_size + int(v['size'])

    if dict_ct > 0:
        for k, v in d.items():
            if isinstance(v, dict) and len(v) != 0 and v['type'] == 'dir':
                size = recurse_dict(v['contents'], k)
                dir_size = dir_size + size
    
    dir_sizes.append(f"{dir_size} {dir_name}")
    
    return dir_size

# %%
# Build structure
while line_ix < len(data):
    line = data[line_ix]

    if line == '$ ls':
        contents, line_ix = get_contents(data, line_ix)
        add_contents(file_structure, current_dir, contents)
    elif '$ cd' in line:
        current_dir, breadcrumb = change_dir(line, file_structure, current_dir, breadcrumb)
        line_ix = line_ix + 1

# %%
# Display structure
structure_view = json.dumps(file_structure, indent=4)
print(structure_view)

# %%
# Calculate dir sizes
recurse_dict(file_structure['/']['contents'], '/')

# %%
final_size = 0

# Used for part 2 #
file_system_size = 70000000
free_space_target = 30000000
###################

for i in dir_sizes:
    dir = i.split(' ')
    name = dir[1]
    size = int(dir[0])

    # Used for part 2 #
    if name == '/':
        space_used = file_system_size - size
        space_to_clear = free_space_target - space_used
    ###################

    if size <= 100000:
        final_size = final_size + size

print(f"Answer (part one) - Find any dirs with a size <= 100000 and sum all of their sizes: {final_size}")

# %% [markdown]
# # Part Two

# %%
file_system_size = 70000000
free_space_target = 30000000
final_sizes = []

print(f"Total space used: {space_used}")
print(f"Amount of space to clear = {space_to_clear}")

for i in dir_sizes:
    dir = i.split(' ')
    size = int(dir[0])

    if size >= space_to_clear:
        final_sizes.append(size)

print(f"Answer (part two) - Size of dir to delete: {min(final_sizes)}")


