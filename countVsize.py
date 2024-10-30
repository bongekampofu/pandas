import  matplotlib.pyplot as plt
import pandas as pd

# Sample data
df = pd.DataFrame({
    'Pclass': [1, 2, 2, 3, 3, 3],
    'Age': [22, 38, None, 26, None, None]
})

# Using count
count_df = df.groupby("Pclass")["Age"].count()
print("Using count:\n", count_df)

# Using size
size_df = df.groupby("Pclass").size()
print("\nUsing size:\n", size_df)
