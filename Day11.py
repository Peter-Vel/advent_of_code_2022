# %% [markdown]
# # Part One

# %%
import yaml
import math

# %%
with open('./Input/Day11_Input_Test.yml', 'r') as file:
    monkeys = yaml.safe_load(file)

# %%
items = {}

for m in monkeys.keys():
    starting_items = str(monkeys[m]['Starting items'])

    if ',' in starting_items:
        starting_items = starting_items.split(',')
        for s in starting_items: s.strip()
    else:
        starting_items = [starting_items]

    item_ct = len(starting_items)
    items[m] = {'Items Inspected': 0, 'Item Count': item_ct, 'Worry Levels': starting_items}

# %%
def inspect_item(m, wl, op, part):
    equation = op.replace('new = ', '').replace('old', wl)
    
    if part == 'one':
        new = math.floor(eval(equation) / 3)
    else:
        new = math.floor(eval(equation))
    
    inspected = items[m]['Items Inspected']
    inspected = inspected + 1
    items[m]['Items Inspected'] = inspected

    return new

def test_item(wl, v):
    if wl % v == 0:
        result = True
    else:
        result = False

    return result

def pass_item(wl, src_m, m):
    # Pass
    del items[src_m]['Worry Levels'][0]
    items[src_m]['Item Count'] = len(items[src_m]['Worry Levels'])
    
    # Catch
    items[m]['Worry Levels'].append(wl)
    items[m]['Item Count'] = len(items[m]['Worry Levels'])

def get_top_two(t, get_two = False):
    top_one = max(t)

    if t.count(top_one) == 1:
        t.remove(top_one)
        top_two = max(t)
    else:
        # Top two #s are the same
        top_two = top_one

    return top_one, top_two

def start_rounds(rnds, part = 'one'):
    rnd = 1

    while rnd <= rnds:
        for k, v in monkeys.items():
            monkey = k
            operation = v['Operation']
            test_value = int(v['Test'].split(' ')[2])
            if_true = v['If true'].split(' ')
            if_true = f"{if_true[2].capitalize()} {if_true[3]}"
            if_false = v['If false'].split(' ')
            if_false = f"{if_false[2].capitalize()} {if_false[3]}"
            orig_item_ct = items[monkey]['Item Count']
            turn = 0
        
            while turn <= orig_item_ct:
                worry_lvl = items[monkey]['Worry Levels']
                
                if worry_lvl:
                    worry_lvl = worry_lvl[0]
                    worry_lvl = worry_lvl.strip()
                else:
                    break # End turn because they have no more items

                new = inspect_item(monkey, worry_lvl, operation, part)
                test_result = test_item(new, test_value)
                pass_item(str(new), monkey, if_false) if test_result == False else pass_item(str(new), monkey, if_true)

                turn = turn + 1
            
        rnd = rnd + 1

# %%
start_rounds(20)

total_inspected = []

for k, v in items.items():
    num_inspected = v['Items Inspected']
    total_inspected.append(num_inspected)
    
    print(f"{k} inspected {num_inspected} pieces!")

top_one, top_two = get_top_two(total_inspected)
monkey_biz = top_one * top_two

print(f"\nAnswer (part one) - Total level of monkey business: {monkey_biz}")

# %% [markdown]
# # Part Two

# %%
start_rounds(10000, 'two')


