# HW1: Descriptive Statistics and Measurement Error
The data for this assignment was sourced from the UC Irvine Machine Learning Repository, and was provided by Dr. Elms. 
You can find the repository [here](https://archive.ics.uci.edu/).

## Components
This assignment was split into four components, each serving to find statistics for a different data column. I've outlined the components below.

1. Find the median, mean, and mode of the water component data.
2. Find the range, variance, and standard deviation of the fine aggregate component data.
3. Find the mean and standard error of the cement component data. 
4. Find the mean and standard error of the concrete compressive strength data.

## Some Notes
1. I'm not sure if it's because of a CSV extension I have in VSCode, but the last column has a set of double quotes in the header for me that doesn't show up on other preview tools. This caused me some confusion when trying to match the dictionary key for that column, so this was commented in the code, but it could be an issue with my VSCode instance misleading me as to the true header vals. 
2. TAMU typically doesn't teach the entry point concept where we evaluate dunder name == dunder main, but I prefer to reinforce this as a habit in all Python code I write. If you were to write libraries, the presence of the dunder main entry point indicates this file should be ran. It also safeguards from early execution if it were ever imported. It even can afford some performance benefits due to how Python's interpreter handles the execution logic, particularly on projects that get converted to C with cython. These don't really matter for something minor like this, but I prefer to keep a consistent pattern across my code to stay in the habit of using a main guard. 