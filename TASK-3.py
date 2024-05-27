
# Imported pandas , Numpy , Matplotlib , seaborn and finally datetime for data visulation

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from datetime import datetime


# Read CSV File and store it in data
# Displayed data in tabular form

data = pd.read_csv('C:/Users/anony/Documents/householdtask3.csv')
data

# Displayed the first 10 rows of data in tabular form 

display(data.head(10))


# Displayed scatter plot of year and own

plt.scatter(data['year'],data['own'])

# Taken own as y axis and year as x axis
# Displayed title scatter plot
# Displayed the plot

plt.title("Scatter Plot")
plt.xlabel('year')
plt.ylabel('own')
plt.show()

# Displayed scatter plot of year and own with colorbar

plt.scatter(data['year'],data['own'])
plt.title("Scatter Plot")
plt.xlabel('year')
plt.ylabel('own')
plt.colorbar()
plt.show()

# Displayed Line Chart of year and own
# Taken own as y axis and year as x axis
# Displayed title Line Chart
# Displayed the line chart

plt.plot(data['year'])
plt.plot(data['own'])
plt.title('Line Chart')
plt.xlabel('year')
plt.ylabel('own')
plt.show()

# Displayed Bar Chart of year and own
# Taken own as y axis and year as x axis
# Displayed title Bar Chart
# Displayed the bar chart

plt.bar(data['year'],data['own'])
plt.title('Bar Chart')
plt.xlabel('year')
plt.ylabel('own')
plt.show()

# Displayed Histogram of income

plt.hist(data['income'])
plt.title('Histogram')
plt.show()


