import pandas as pd
import random as rn
import ast


def get_Jens_data(df:pd.DataFrame) -> pd.DataFrame:
    result = df.loc[df['Name'] == 'Jen', ['Name', 'Age']]
    return(result)

def create_column(col_name, col_values, df):
    df[col_name] = col_values
    return df

def create_txt_files(location):
    with open(location, 'w') as file:
        file.writelines('[]')
    print(f"File created in location: {location}")

"""
This function simulates KINO games and returns the value of winnings assuming each bet is worth 1.
The value of returns for each strategy is given here: https://www.opap.gr/en/kino-pay-table.

    Args:
        strategy (int): Number of guesses the user will make before each draw (between 1 and 12).
        attempts (int): How many game simulations the function will run before calculating net profits.

    Returns:
        float: The net profit/loss after simulations have finished.
"""
def draw_outcome(strategy, attempts):
    num_found = []
    p_n_l = 0
    if strategy == 1:
        a = 0
        while a < attempts:
            # My choice
            x = rn.sample(range(1, 81), strategy)

            # Draw Results
            winners = rn.sample(range(1, 81), 20)

            # Checking for successes
            successes = 0
            for item in x:
                if item in winners:
                    successes = successes + 1
            if successes == 0:
                p_n_l = p_n_l - 1
            elif successes == 1:
                p_n_l = p_n_l + 1.5
            num_found.append(successes)
            a = a + 1
    elif strategy == 2:
        a = 0
        while a < attempts:
            # My choice
            x = rn.sample(range(1, 81), strategy)

            # Draw Results
            winners = rn.sample(range(1, 81), 20)

            # Checking for successes
            successes = 0
            for item in x:
                if item in winners:
                    successes = successes + 1
            if successes == 0:
                p_n_l = p_n_l - 1
            elif successes == 1:
                p_n_l = p_n_l - 0
            elif successes == 2:
                p_n_l = p_n_l + 4
            num_found.append(successes)
            a = a + 1
    elif strategy == 3:
        a = 0
        while a < attempts:
            # My choice
            x = rn.sample(range(1, 81), strategy)

            # Draw Results
            winners = rn.sample(range(1, 81), 20)

            # Checking for successes
            successes = 0
            for item in x:
                if item in winners:
                    successes = successes + 1
            if successes == 0:
                p_n_l = p_n_l - 1
            elif successes == 1:
                p_n_l = p_n_l - 1
            elif successes == 2:
                p_n_l = p_n_l + 1.5
            elif successes == 3:
                p_n_l = p_n_l + 24
            num_found.append(successes)
            a = a + 1
    elif strategy == 4:
        a = 0
        while a < attempts:
            # My choice
            x = rn.sample(range(1, 81), strategy)

            # Draw Results
            winners = rn.sample(range(1, 81), 20)

            # Checking for successes
            successes = 0
            for item in x:
                if item in winners:
                    successes = successes + 1
            if successes == 0:
                p_n_l = p_n_l - 1
            elif successes == 1:
                p_n_l = p_n_l - 1
            elif successes == 2:
                p_n_l = p_n_l - 0
            elif successes == 3:
                p_n_l = p_n_l + 3
            elif successes == 4:
                p_n_l = p_n_l + 99
            num_found.append(successes)
            a = a + 1
    elif strategy == 5:
        a = 0
        while a < attempts:
            # My choice
            x = rn.sample(range(1, 81), strategy)

            # Draw Results
            winners = rn.sample(range(1, 81), 20)

            # Checking for successes
            successes = 0
            for item in x:
                if item in winners:
                    successes = successes + 1
            if successes == 0:
                p_n_l = p_n_l - 1
            elif successes == 1:
                p_n_l = p_n_l - 1
            elif successes == 2:
                p_n_l = p_n_l - 1
            elif successes == 3:
                p_n_l = p_n_l + 1
            elif successes == 4:
                p_n_l = p_n_l + 19
            elif successes == 5:
                p_n_l = p_n_l + 449
            num_found.append(successes)
            a = a + 1
    elif strategy == 6:
        a = 0
        while a < attempts:
            # My choice
            x = rn.sample(range(1, 81), strategy)

            # Draw Results
            winners = rn.sample(range(1, 81), 20)

            # Checking for successes
            successes = 0
            for item in x:
                if item in winners:
                    successes = successes + 1
            if successes == 0:
                p_n_l = p_n_l - 1
            elif successes == 1:
                p_n_l = p_n_l - 1
            elif successes == 2:
                p_n_l = p_n_l - 1
            elif successes == 3:
                p_n_l = p_n_l + 0
            elif successes == 4:
                p_n_l = p_n_l + 6
            elif successes == 5:
                p_n_l = p_n_l + 49
            elif successes == 6:
                p_n_l = p_n_l + 1599
            num_found.append(successes)
            a = a + 1
    elif strategy == 7:
        a = 0
        while a < attempts:
            # My choice
            x = rn.sample(range(1, 81), strategy)

            # Draw Results
            winners = rn.sample(range(1, 81), 20)

            # Checking for successes
            successes = 0
            for item in x:
                if item in winners:
                    successes = successes + 1
            if successes == 0:
                p_n_l = p_n_l - 1
            elif successes == 1:
                p_n_l = p_n_l - 1
            elif successes == 2:
                p_n_l = p_n_l - 1
            elif successes == 3:
                p_n_l = p_n_l + 0
            elif successes == 4:
                p_n_l = p_n_l + 2
            elif successes == 5:
                p_n_l = p_n_l + 19
            elif successes == 6:
                p_n_l = p_n_l + 99
            elif successes == 7:
                p_n_l = p_n_l + 4999
            num_found.append(successes)
            a = a + 1
    elif strategy == 8:
        a = 0
        while a < attempts:
            # My choice
            x = rn.sample(range(1, 81), strategy)

            # Draw Results
            winners = rn.sample(range(1, 81), 20)

            # Checking for successes
            successes = 0
            for item in x:
                if item in winners:
                    successes = successes + 1
            if successes == 0:
                p_n_l = p_n_l - 1
            elif successes == 1:
                p_n_l = p_n_l - 1
            elif successes == 2:
                p_n_l = p_n_l - 1
            elif successes == 3:
                p_n_l = p_n_l - 1
            elif successes == 4:
                p_n_l = p_n_l + 1
            elif successes == 5:
                p_n_l = p_n_l + 9
            elif successes == 6:
                p_n_l = p_n_l + 49
            elif successes == 7:
                p_n_l = p_n_l + 999
            elif successes == 8:
                p_n_l = p_n_l + 14999
            num_found.append(successes)
            a = a + 1
    elif strategy == 9:
        a = 0
        while a < attempts:
            # My choice
            x = rn.sample(range(1, 81), strategy)

            # Draw Results
            winners = rn.sample(range(1, 81), 20)

            # Checking for successes
            successes = 0
            for item in x:
                if item in winners:
                    successes = successes + 1
            if successes == 0:
                p_n_l = p_n_l - 1
            elif successes == 1:
                p_n_l = p_n_l - 1
            elif successes == 2:
                p_n_l = p_n_l - 1
            elif successes == 3:
                p_n_l = p_n_l - 1
            elif successes == 4:
                p_n_l = p_n_l + 0
            elif successes == 5:
                p_n_l = p_n_l + 4
            elif successes == 6:
                p_n_l = p_n_l + 24
            elif successes == 7:
                p_n_l = p_n_l + 199
            elif successes == 8:
                p_n_l = p_n_l + 3999
            elif successes == 9:
                p_n_l = p_n_l + 39999
            num_found.append(successes)
            a = a + 1
    elif strategy == 10:
        a = 0
        while a < attempts:
            # My choice
            x = rn.sample(range(1, 81), strategy)

            # Draw Results
            winners = rn.sample(range(1, 81), 20)

            # Checking for successes
            successes = 0
            for item in x:
                if item in winners:
                    successes = successes + 1
            if successes == 0:
                p_n_l = p_n_l + 1
            elif successes == 1:
                p_n_l = p_n_l - 1
            elif successes == 2:
                p_n_l = p_n_l - 1
            elif successes == 3:
                p_n_l = p_n_l - 1
            elif successes == 4:
                p_n_l = p_n_l - 1
            elif successes == 5:
                p_n_l = p_n_l + 1
            elif successes == 6:
                p_n_l = p_n_l + 19
            elif successes == 7:
                p_n_l = p_n_l + 79
            elif successes == 8:
                p_n_l = p_n_l + 499
            elif successes == 9:
                p_n_l = p_n_l + 9999
            elif successes == 10:
                p_n_l = p_n_l + 99999
            num_found.append(successes)
            a = a + 1
    elif strategy == 11:
        a = 0
        while a < attempts:
            # My choice
            x = rn.sample(range(1, 81), strategy)

            # Draw Results
            winners = rn.sample(range(1, 81), 20)

            # Checking for successes
            successes = 0
            for item in x:
                if item in winners:
                    successes = successes + 1
            if successes == 0:
                p_n_l = p_n_l + 1
            elif successes == 1:
                p_n_l = p_n_l - 1
            elif successes == 2:
                p_n_l = p_n_l - 1
            elif successes == 3:
                p_n_l = p_n_l - 1
            elif successes == 4:
                p_n_l = p_n_l - 1
            elif successes == 5:
                p_n_l = p_n_l + 0
            elif successes == 6:
                p_n_l = p_n_l + 9
            elif successes == 7:
                p_n_l = p_n_l + 49
            elif successes == 8:
                p_n_l = p_n_l + 249
            elif successes == 9:
                p_n_l = p_n_l + 1499
            elif successes == 10:
                p_n_l = p_n_l + 14999
            elif successes == 11:
                p_n_l = p_n_l + 499999
            num_found.append(successes)
            a = a + 1
    elif strategy == 12:
        a = 0
        while a < attempts:
            # My choice
            x = rn.sample(range(1, 81), strategy)

            # Draw Results
            winners = rn.sample(range(1, 81), 20)

            # Checking for successes
            successes = 0
            for item in x:
                if item in winners:
                    successes = successes + 1
            if successes == 0:
                p_n_l = p_n_l + 3
            elif successes == 1:
                p_n_l = p_n_l - 1
            elif successes == 2:
                p_n_l = p_n_l - 1
            elif successes == 3:
                p_n_l = p_n_l - 1
            elif successes == 4:
                p_n_l = p_n_l - 1
            elif successes == 5:
                p_n_l = p_n_l - 1
            elif successes == 6:
                p_n_l = p_n_l + 4
            elif successes == 7:
                p_n_l = p_n_l + 24
            elif successes == 8:
                p_n_l = p_n_l + 149
            elif successes == 9:
                p_n_l = p_n_l + 999
            elif successes == 10:
                p_n_l = p_n_l + 2499
            elif successes == 11:
                p_n_l = p_n_l + 24999
            elif successes == 12:
                p_n_l = p_n_l + 999999
            num_found.append(successes)
            a = a + 1
    else:
        print("Invalid strategy")
    return p_n_l, num_found

def append_results(datafile):
    with open(datafile, 'r') as filepath:
        for line in filepath:
            stripped_line = line.strip()
        try:
            prev_results = ast.literal_eval(stripped_line)
            if isinstance(prev_results, list) and all(isinstance(num, (float, int)) for num in prev_results):
                print(
                    "Below is a list of previous results, the appended list that includes the last simulation, and a Total Profit.")
            else:
                print(f"Line is not a valid list of integers: {stripped_line}")

        except (ValueError, SyntaxError):
            print(f"Skipping invalid line: {stripped_line}")
    return prev_results

def write_results(datafile, results):
    with open(datafile, 'w') as filepath:
        filepath.write(str(results))