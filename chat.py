import matplotlib.pyplot as plt
import pandas as pd
import numpy as np

# Generate sample age data
np.random.seed(0)
ages = np.random.normal(loc=35, scale=10, size=1000).astype(int)  # Ages around 35

# Create a histogram
plt.hist(ages, bins=20, color='skyblue', edgecolor='black')
plt.title('Age Distribution')
plt.xlabel('Age')
plt.ylabel('Frequency')
plt.grid(True)
plt.tight_layout()
plt.show()
