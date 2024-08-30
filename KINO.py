import random
import random as rn
import ast

strategy = 7
datafile = f'KINO_{strategy}_results.txt'

#My choice
#x = rn.randint(1, 80)

#Draw Results
#winners = random.sample(range(1, 81), 20)

#Kino Bonus
#bonus = random.choice(winners)

all_results = []
num_found = []

p_n_l = 0
a = 1
while a < 50001:
    # My choice
    x = rn.sample(range(1,81), strategy)

    # Draw Results
    winners = random.sample(range(1, 81), 20)

    # Kino Bonus
    # bonus = random.choice(winners)
    successes = 0
    for item in x:
        if item in winners:
            successes = successes + 1
    if successes == 0:
        p_n_l = p_n_l -1
    elif successes == 1:
        p_n_l = p_n_l -1
    elif successes == 2:
        p_n_l = p_n_l -1
    elif successes == 3:
        p_n_l = p_n_l +0
    elif successes == 4:
        p_n_l = p_n_l +2
    elif successes == 5:
        p_n_l = p_n_l +19
    elif successes == 6:
        p_n_l = p_n_l+99
    elif successes == 7:
        p_n_l = p_n_l+4999
    num_found.append(successes)
    a = a + 1

print(f"Profit after {a-1} tries: {p_n_l}")

print(f"Numbers found: 1:{num_found.count(1)}, 2:{num_found.count(2)}, 3:{num_found.count(3)}, 4:{num_found.count(4)}"
      f"5:{num_found.count(5)}, 6:{num_found.count(6)}, 7:{num_found.count(7)}")

with open(datafile, 'r') as filepath:
    for line in filepath:
        stripped_line = line.strip()
    try:
        prev_results = ast.literal_eval(stripped_line)
        if isinstance(prev_results, list) and all(isinstance(num, int) for num in prev_results):
            all_results.append(prev_results)
        else:
            print(f"Line is not a valid list of integers: {stripped_line}")

    except (ValueError, SyntaxError):
        print(f"Skipping invalid line: {stripped_line}")
print(f"Prev_res: {prev_results}")
p_n_l = [int(p_n_l)]
prev_results.extend(p_n_l)

print(f"All results: {prev_results}")
print(f"Sum: {sum(prev_results)}")

prev_results = str(prev_results)



with open(datafile, 'w') as filepath:
    filepath.write(str(prev_results))

