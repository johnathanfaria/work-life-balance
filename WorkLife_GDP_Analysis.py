
import pandas as pd
import matplotlib.pyplot as plt

# Data
data = {
    "Country": [
        "New Zealand", "Ireland", "Belgium", "Denmark", "Canada", "Germany", "Finland", "Australia", "Norway",
        "Spain", "Netherlands", "Portugal", "France", "Sweden", "United Kingdom", "Czech Republic", "Poland",
        "Austria", "Argentina", "Greece", "Romania", "Hungary", "Italy", "Japan", "Brazil", "Singapore",
        "Switzerland", "Taiwan", "Saudi Arabia", "Peru"
    ],
    "Rank Difference": [
        -23, 0, -13, -6, -13, -13, -10, -3, 5, -26, -1, -31, -12, -1, -8, -26, -37, 4, -55, -29,
        -39, -30, -5, -14, -57, 21, 24, -6, -10, -61
    ]
}

df_difference = pd.DataFrame(data)

fig, ax = plt.subplots(figsize=(14, 8))
ax.bar(df_difference['Country'], df_difference['Rank Difference'], color='purple')
ax.set_xlabel('Country')
ax.set_ylabel('Rank Difference (Work-Life - GDP)')
ax.set_title('Difference Between Work-Life Balance Rank and GDP Rank by Country')
ax.set_xticklabels(df_difference['Country'], rotation=90)
plt.grid(axis='y', linestyle='--', alpha=0.7)
plt.tight_layout()
plt.show()
