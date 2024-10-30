import pandas as pd
import matplotlib.pyplot as plt

# Creating a DataFrame with a categorical column
data = {
    'Category': pd.Series(['A', 'B', 'A', 'C', 'B', 'A', 'C', None], dtype="category"),
    'Value': [10, None, 30, 40, None, 60, None, None]
}
df = pd.DataFrame(data)

# Grouping by 'Category' and using size() to get counts of each category
category_counts = df.groupby('Category').size()

# Plotting the categorical data
#category_counts.index represents the categories ('A', 'B', 'C') on the x-axis of the bar chart.
#category_counts.values are the counts for each category, which we use as the y-axis values for the bars.
plt.bar(category_counts.index, category_counts.values, color='skyblue')
plt.xlabel('Category')
plt.ylabel('Frequency')
plt.title('Frequency of Categories')
plt.show()

