import numpy as np
import pandas as pd
from scipy import stats

# PART 1

# The following line of code creates column names
columns_yo = ['Day 1', 'Day 2', 'Day 3', 'Day 4', 'Day 5', 'Day 6', 'Day 7', 'Day 8', 'Day 9', 'Day 10',]

# The following line of code generates an array with 1000 rows and 10 columns
x = np.random.rand(1000,10)

# The following line creates a pandas dataframe from the numpy array
x_pd = pd.DataFrame(x, columns=columns_yo)

# The following line saves the newly created pandas dataframe as a csv file
x_pd.to_csv('x_pd.csv', header = True)

# PART 2

# The following line of code reads the csv file and saves it as a new variable
x_read_w_pandas = pd.read_csv('x_pd.csv')

# print(x_read_w_pandas.describe())
# print(stats.mode(x_read_w_pandas))

# PART 3

# The following line of code computes and stores the modes of the columns in the recently read variable
y = stats.mode(x_read_w_pandas)

# The following line computes the means, standard deviations and medians of the columns of the array.
z = x_read_w_pandas.describe()

# PART 4

# The following line of code creates the summary text file
f = open("project_6.txt", "w+")

# The following line writes the output of the .describe() attribute after it is converted into a string
f.write(z.to_string())
f.write("\n\n\n")
# The following line writes the mode computations into the summary text file after converting the computations into a string
f.write(str(y))
f.write("\n\n\n")
# The following line writes 3 lines from the array into the summary text file
f.write(str(x[:3,:]))

# The following line closes the file.
f.close()
