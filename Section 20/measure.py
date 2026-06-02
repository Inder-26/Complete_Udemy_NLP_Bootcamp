import matplotlib.pyplot as plt
import numpy as np
from scipy import stats
import warnings

# --- 1. The Data (Our Salary Story) ---
# 9 employees and 1 owner
salaries = [30000, 32000, 32000, 34000, 35000, 36000, 38000, 40000, 42000, 500000]

# --- 2. Calculate the "Measures" ---

# MEAN: The "misleading" average.
# Add everyone up (including the owner) and divide by 10.
mean_val = np.mean(salaries)

# MEDIAN: The "honest" middle value.
# Line them up and find the middle.
median_val = np.median(salaries)

# MODE: The "most popular" salary.
# Find the one that appears most often.
# We use keepdims=False to get a simple value
# and .mode to get the number.
try:
    # Modern Scipy (version 1.11+)
    mode_val_result = stats.mode(salaries, keepdims=False)
    mode_val = mode_val_result.mode
except TypeError:
    # Older Scipy
    # Suppress potential warnings from older versions
    with warnings.catch_warnings():
        warnings.simplefilter("ignore", DeprecationWarning)
        mode_val_result = stats.mode(salaries)
        mode_val = mode_val_result[0][0]


# --- 3. Print the Results (The Story in Numbers) ---
print("--- The Cafe Salary Story ---")
print(f"The 10 salaries are: {salaries}")
print("\n")
print(f"1. The MEAN (Misleading Average): ${mean_val:,.2f}")
print(f"   -> This is pulled 'way up by the $500k outlier.")
print("\n")
print(f"2. The MEDIAN (Honest Middle):   ${median_val:,.2f}")
print(f"   -> This is the most 'typical' and robust number.")
print("\n")
print(f"3. The MODE (Most Popular):      ${mode_val:,.2f}")
print(f"   -> This is the most 'common' salary.")


# --- 4. Plot the Data (The Visual Story) ---
plt.figure(figsize=(12, 7))

# Create the histogram.
# 'bins' controls how many bars. We use a lot to see the gap.
plt.hist(salaries, bins=20, alpha=0.7, label='Salary Distribution', color='skyblue', edgecolor='black')

# Add vertical lines to show "what" and "where"
plt.axvline(mean_val, color='red', linestyle='dashed', linewidth=3, 
            label=f'Mean (Misleading): ${mean_val:,.2f}')

plt.axvline(median_val, color='green', linestyle='solid', linewidth=3, 
            label=f'Median (Honest): ${median_val:,.2f}')

plt.axvline(mode_val, color='purple', linestyle='dotted', linewidth=3, 
            label=f'Mode (Most Popular): ${mode_val:,.2f}')

# Add labels and title
plt.title('Why the MEDIAN is often the most "honest" number', fontsize=16)
plt.xlabel('Annual Salary ($)', fontsize=12)
plt.ylabel('Number of People (Frequency)', fontsize=12)
plt.legend(fontsize=11)
plt.grid(axis='y', linestyle='--', alpha=0.7)
plt.tight_layout()

# Show the plot
print("\n--- Showing plot... ---")
plt.show()