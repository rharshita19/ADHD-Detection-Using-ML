import matplotlib.pyplot as plt
import pandas as pd

# Load the CSV file
data = pd.read_csv("/Users/harshitarai/Downloads/patient_info (1).csv", delimiter=';')

# Optional: Strip spaces in column names (just in case)
data.columns = data.columns.str.strip()

# Check counts in the 'ADHD' column
group_counts = data['ADHD'].value_counts().sort_index()

# Label 0 = Control, 1 = ADHD
group_labels = ['Control', 'ADHD']

# Plotting
plt.figure(figsize=(8, 5))
plt.bar(group_labels, group_counts.values, color=['orange', 'blue'])
plt.title('Number of Patients in Each Group')
plt.xlabel('Group')
plt.ylabel('Number of Patients')
plt.grid(axis='y', linestyle='--', alpha=0.6)
plt.tight_layout()
plt.show()
print(data.shape)
