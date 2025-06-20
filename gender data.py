import matplotlib.pyplot as plt
import pandas as pd

# Sample gender data
data = {'gender': ['Male', 'Female', 'Female', 'Male', 'Female', 'Other', 'Male', 'Female', 'Other', 'Male']}
df = pd.DataFrame(data)

# Count the occurrences
gender_counts = df['gender'].value_counts()

# Create a bar chart
gender_counts.plot(kind='bar', color=['blue', 'pink', 'green'])
plt.title('Gender Distribution')
plt.xlabel('Gender')
plt.ylabel('Count')
plt.xticks(rotation=0)
plt.tight_layout()
plt.show()
