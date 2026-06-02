import matplotlib.pyplot as plt
import numpy as np
from scipy import stats
import warnings

# Helper function to find modes (can be more than one)
def find_modes(data):
    try:
        # Modern Scipy (version 1.11+)
        mode_result = stats.mode(data, keepdims=False)
        # FIX: Ensure we always return an array/list
        if np.isscalar(mode_result.mode):
            return [mode_result.mode] # Wrap scalar in a list
        else:
            return mode_result.mode # It's already an array
    except TypeError:
        # Older Scipy
        with warnings.catch_warnings():
            warnings.simplefilter("ignore", DeprecationWarning)
            mode_result = stats.mode(data)
            # Handle multiple modes in older versions
            if len(mode_result.mode[0]) > 0:
                return mode_result.mode[0]
            else:
                return [np.nan] # No clear mode
    except Exception:
        return [np.nan]

# --- 1. Symmetrical Distribution (e.g., Test Scores) ---
# Here, all three measures are great!
data_sym = np.random.normal(loc=100, scale=15, size=1000) # 1000 data points centered at 100
mean_sym = np.mean(data_sym)
median_sym = np.median(data_sym)
# Mode is tricky for normal data, so we round to get a clearer value
mode_sym = find_modes(np.round(data_sym))[0]

plt.figure(1, figsize=(10, 6))
plt.hist(data_sym, bins=30, alpha=0.7, label='Data Distribution', color='blue', edgecolor='black')
plt.axvline(mean_sym, color='red', linestyle='dashed', linewidth=2, label=f'Mean: {mean_sym:.2f}')
plt.axvline(median_sym, color='green', linestyle='solid', linewidth=2, label=f'Median: {median_sym:.2f}')
plt.axvline(mode_sym, color='purple', linestyle='dotted', linewidth=2, label=f'Mode: {mode_sym:.2f}')
plt.title('Plot 1: Symmetrical Distribution (e.g., Test Scores)', fontsize=16)
plt.xlabel('Value')
plt.ylabel('Frequency')
plt.legend()
plt.figtext(0.5, 0.01, "In this 'perfect' bell curve, the Mean, Median, and Mode are all the same.\nAny of them is a good description of the 'center'.", 
            ha="center", fontsize=10, bbox={"facecolor":"white", "alpha":0.5, "pad":5})
plt.tight_layout(rect=[0, 0.05, 1, 1])


# --- 2. Left-Skewed Distribution (e.g., Exam Difficulty) ---
# An easy exam where most people did well (high scores), but a few did very badly.
data_left = [40, 50, 80, 82, 85, 88, 89, 90, 91, 92, 92, 94, 95, 96, 98, 100, 100]
mean_left = np.mean(data_left)
median_left = np.median(data_left)
mode_left = find_modes(data_left) # Can be multiple

plt.figure(2, figsize=(10, 6))
plt.hist(data_left, bins=10, alpha=0.7, label='Data Distribution', color='orange', edgecolor='black')
plt.axvline(mean_left, color='red', linestyle='dashed', linewidth=2, label=f'Mean: {mean_left:.2f}')
plt.axvline(median_left, color='green', linestyle='solid', linewidth=2, label=f'Median: {median_left:.2f}')
# Plot all modes if there are multiple
for m in np.atleast_1d(mode_left):
    plt.axvline(m, color='purple', linestyle='dotted', linewidth=2, label=f'Mode: {m:.2f}')
plt.title('Plot 2: Left-Skewed Distribution (Low Outlier)', fontsize=16)
plt.xlabel('Value')
plt.ylabel('Frequency')
plt.legend()
plt.figtext(0.5, 0.01, "Here, the low scores (40, 50) pull the Mean *down*.\nThe Median (91) is a more 'honest' center for how the typical student did.", 
            ha="center", fontsize=10, bbox={"facecolor":"white", "alpha":0.5, "pad":5})
plt.tight_layout(rect=[0, 0.05, 1, 1])


# --- 3. Bimodal Distribution (e.g., Restaurant Rush Hour) ---
# Two separate busy times: lunch and dinner.
lunch_rush = np.random.normal(loc=12, scale=1, size=500)
dinner_rush = np.random.normal(loc=19, scale=1, size=500)
data_bimodal = np.concatenate([lunch_rush, dinner_rush])

mean_bimodal = np.mean(data_bimodal)
median_bimodal = np.median(data_bimodal)
# Find modes by rounding
modes_bimodal = find_modes(np.round(data_bimodal))

plt.figure(3, figsize=(10, 6))
plt.hist(data_bimodal, bins=30, alpha=0.7, label='Data Distribution', color='green', edgecolor='black')
plt.axvline(mean_bimodal, color='red', linestyle='dashed', linewidth=2, label=f'Mean: {mean_bimodal:.2f}')
plt.axvline(median_bimodal, color='green', linestyle='solid', linewidth=2, label=f'Median: {median_bimodal:.2f}')
# Plot all modes
for m in np.atleast_1d(modes_bimodal):
    plt.axvline(m, color='purple', linestyle='dotted', linewidth=2, label=f'Mode: {m:.2f}')
plt.title('Plot 3: Bimodal Distribution (Two Peaks)', fontsize=16)
plt.xlabel('Hour of the Day')
plt.ylabel('Frequency (Customers)')
plt.legend()
plt.figtext(0.5, 0.01, "The Mean and Median fall in the 'valley' between the two peaks (around 3:30 PM).\nThey are useless here. The two *Modes* (12 and 19) are the only useful measure.", 
            ha="center", fontsize=10, bbox={"facecolor":"white", "alpha":0.5, "pad":5})
plt.tight_layout(rect=[0, 0.05, 1, 1])


# Show all plots
print("Showing 3 new plots...")
plt.show()