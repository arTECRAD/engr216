import csv 
import math
from statistics import median, mean, mode, pvariance, pstdev

def read_column(dataset, column):
    '''
    Read in a CSV supplied by param dataset, then
    find all values for param column (string), cast values to floats,
    then return a list of the specified vals.
    '''
    vals = []
    with open(dataset, mode='r', newline='', encoding='utf-8') as csvfile:
        # Read the lines of the CSV and return lines as 
        # dictionaries into reader.
        reader = csv.DictReader(csvfile)

        # I had a difficult time getting the last two columns
        # to find the keys correctly, and when I ran the line below,
        # it turns out they were getting some weird characters in the 
        # column keys. I used the output from this line to set the 
        # column params for each function call.
        print("Field names:", reader.fieldnames) # debug the issue with cement_data keys being off

        # For each 'row' in reader (aka dicts)
        # find the 'column' key/value pairs, cast
        # the value to a float, then append it to 
        # the list of vals.
        for row in reader:
            val = row.get(column).strip()
            
            # CSV reader will probably make all key/value pairs
            # strings, so we want to cast to float for stats
            val = float(val)
            vals.append(val)

    return vals

def main():
    # Hard code the filename
    filename = 'Concrete_Data.csv'

    # Fetch data from the CSV
    water_data = read_column(filename, 'Water  (component 4)(kg in a m^3 mixture)')
    fine_ag_data = read_column(filename, 'Fine Aggregate (component 7)(kg in a m^3 mixture)')
    cement_data = read_column(filename, '\ufeffCement (component 1)(kg in a m^3 mixture)') # see the debug statement at line 22 for how I got this weirdness
    strength_data = read_column(filename, 'Concrete compressive strength(MPa, megapascals) ') # so no quotes here? whatever... line 22 showed me this

    # Find the median, mean, and mode of the water data (PART A)
    print(f'PART A: Water Component Median = {median(water_data)} kg/m^3 mixture')
    print(f'PART A: Water Component Mean = {mean(water_data)} kg/m^3 mixture')
    print(f'PART A: Water Component Mode = {mode(water_data)} kg/m^3 mixture\n')

    # Find the range, variance, and stdev of the fine aggregate component (PART B)
    print(f'PART B: Range of Fine Aggregate Component = {max(fine_ag_data) - min(fine_ag_data)} kg/m^3 mixture')
    print(f'PART B: Variance of Fine Aggregate Component = {pvariance(fine_ag_data)} kg/m^3 mixture')
    print(f'PART B: Standard Deviation of Fine Aggregate Component = {pstdev(fine_ag_data)} kg/m^3 mixture\n')

    # Find the mean and standard error of the cement component (PART C)
    print(f'PART C: Mean of Cement Component = {mean(cement_data)} kg/m^3 mixture')
    print(f'PART C: Standard Error of Cement Component = {pstdev(cement_data) / math.sqrt(len(cement_data))} kg/m^3 mixture\n')

    # Find the mean and standard error of the concrete compressive strength (PART D)
    print(f'PART D: Mean of Concrete Compressive Strength = {mean(strength_data)} MPa')
    print(f'PART D: Standard Error of Concrete Compressive Strength = {pstdev(strength_data) / math.sqrt(len(strength_data))} MPa')

# entry point
if __name__ == "__main__":
    main()