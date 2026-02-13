import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

year = np.random.randint(2000, 2026, 10)
runs_kohli = np.random.randint(100, 800, len(year))
runs_dhoni = np.random.randint(100, 800, len(year))
runs_sachin = np.random.randint(100, 800, len(year))

# Get sorted indices
sorted_index = np.argsort(year)

# Sort everything using same index
year = year[sorted_index]
runs_kohli = runs_kohli[sorted_index]
runs_dhoni = runs_dhoni[sorted_index]
runs_sachin = runs_sachin[sorted_index]

# Filtring ? Removing Duplicates

unique_years, unique_index = np.unique(year, return_index=True)

year = year[unique_index]
runs_dhoni = runs_dhoni[unique_index]
runs_kohli = runs_kohli[unique_index]
runs_sachin = runs_sachin[unique_index]


sns.set_theme(style='darkgrid')
x = np.arange(len(year))
width = 0.25

plt.bar(x - width, runs_dhoni, width=width, label='Dhoni',color ='y')
plt.bar(x, runs_kohli, width=width, label='Kohli',color='r')
plt.bar(x + width, runs_sachin, width=width, label='Sachin',color='b')

plt.xlabel('Year')
plt.ylabel('Runs')
plt.title("Run Comparison")
plt.xticks(x, year) # Display Year Instead of Indices
plt.tight_layout()
plt.legend()
plt.savefig('output.png')
plt.show()
v
