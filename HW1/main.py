import csv 
import math
from statistics import median, mean, mode, variance, stdev

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
    cement_data = read_column(filename, 'Cement (component 1)(kg in a m^3 mixture)')
    strength_data = read_column(filename, '"Concrete compressive strength(MPa, megapascals) "')

    # Find the median, mean, and mode of the water data (PART A)
    print(f'PART A: Water Component Median = {median(water_data)} kg/m^3 mixture')
    print(f'PART A: Water Component Mean = {mean(water_data)} kg/m^3 mixture')
    print(f'PART A: Water Component Mode = {mode(water_data)} kg/m^3 mixture\n')

    # Find the range, variance, and stdev of the fine aggregate component (PART B)
    print(f'PART B: Range of Fine Aggregate Component = {max(fine_ag_data) - min(fine_ag_data)} kg/m^3 mixture')
    print(f'PART B: Variance of Fine Aggregate Component = {variance(fine_ag_data)} kg/m^3 mixture')
    print(f'PART B: Standard Deviation of Fine Aggregate Component = {stdev(fine_ag_data)} kg/m^3 mixture\n')

    # Find the mean and standard error of the cement component (PART C)
    print(f'PART C: Mean of Cement Component = {mean(cement_data)} kg/m^3 mixture')
    print(f'PART C: Standard Error of Cement Component = {stdev(cement_data) / math.sqrt(len(cement_data))} kg/m^3 mixture\n')

    # Find the mean and standard error of the concrete compressive strength (PART D)
    print(f'PART D: Mean of Concrete Compressive Strength = {mean(strength_data)} MPa')
    print(f'PART D: Standard Error of Concrete Compressive Strength = {stdev(strength_data) / math.sqrt(len(strength_data))} MPa')

# entry point
if __name__ == "__main__":
    main()