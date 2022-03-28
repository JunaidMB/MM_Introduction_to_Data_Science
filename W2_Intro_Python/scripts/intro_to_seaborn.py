import seaborn as sns
import pandas as pd
import numpy as np 
import matplotlib.pyplot as plt
plt.style.use('classic')
sns.set()


# Read in diamonds data
diamonds = pd.read_csv("./W2_Intro_Python/data/diamonds.csv")

# Bar Plot
diamonds_grped = diamonds.groupby(['cut'], as_index=False).agg({'price': 'mean'})
sns.barplot(x = 'cut', y = 'price', data = diamonds_grped)
plt.show()
plt.close()

# Line plot
sns.lineplot(x = 'cut', y = 'price', data = diamonds_grped)
plt.show()

# Scatter plot
sns.scatterplot(x = 'price', y = 'carat', data = diamonds)
plt.show()

# Histogram
sns.distplot(diamonds['price'], bins = 70, kde = False)
plt.show()

# Labelling Plots
sns.barplot(x = 'cut', y = 'price', data = diamonds_grped)
plt.xlabel("Mean Price")
plt.ylabel("Diamond Cut")
plt.title("Mean Price by Diamond Cut")
plt.show()

# Save figure
sns.barplot(x = 'cut', y = 'price', data = diamonds_grped)
plt.xlabel("Mean Price")
plt.ylabel("Diamond Cut")
plt.title("Mean Price by Diamond Cut")

plt.savefig("./W2_Intro_Python/saved_plots/diamonds_barplot.png")

# Checkout Seaborn Documentation
# https://seaborn.pydata.org/

# Other Python Visualisation libraries
# 1. Plotly: https://plotly.com/python/
# 2. Bokeh: https://bokeh.org/
# 3. Altair: https://altair-viz.github.io/