
import functions as fn



# Input the player's strategy, and number of simulations
strategy = 5

attempts = 50000

# This defines the folder in which data will be stored and retrieved for analysis
datafile = f'KINO_Results/KINO_{strategy}_results.txt'



# The KINO simulations

p_n_l, num_found = fn.draw_outcome(strategy, attempts)


print(f"Profit after {attempts} tries: {p_n_l}")

print(f"Numbers found: 1:{num_found.count(1)}, 2:{num_found.count(2)}, 3:{num_found.count(3)}, 4:{num_found.count(4)},"
      f" 5:{num_found.count(5)}, 6:{num_found.count(6)}, 7:{num_found.count(7)}, 8:{num_found.count(8)}, 9:{num_found.count(9)},"
      f" 10:{num_found.count(10)}, 11:{num_found.count(11)}, 12:{num_found.count(12)}")

# Retrieve previous results
prev_results = fn.append_results(datafile)

print(f"Prev_res: {prev_results}")
p_n_l = [float(p_n_l)]

# Append with latest result
prev_results.extend(p_n_l)

print(f"All results: {prev_results}")
print(f"Sum: {sum(prev_results)}")

# Save new data
prev_results = str(prev_results)



fn.write_results(datafile, prev_results)

