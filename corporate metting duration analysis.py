# ==========================================
# Corporate Meeting Duration Analysis
# Minor 1 – Pandas | Medium Difficulty
# ==========================================

import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

sns.set(style="whitegrid")

# ------------------------------------------
# Load CSV Data
# ------------------------------------------
df = pd.read_csv("meetings.csv")
print("Dataset Loaded Successfully\n")
print(df.head())

# ------------------------------------------
# Dataset Information
# ------------------------------------------
print("\nDataset Info:")
print(df.info())

print("\nMissing Values:")
print(df.isnull().sum())

# ------------------------------------------
# Summary Statistics
# ------------------------------------------
print("\nSummary Statistics:")
print(df.describe())

# ------------------------------------------
# Categorize Meeting Duration
# ------------------------------------------
def duration_category(minutes):
    if minutes < 30:
        return "Short"
    elif minutes <= 60:
        return "Medium"
    else:
        return "Long"

df["Duration_Category"] = df["Duration_Minutes"].apply(duration_category)

# ------------------------------------------
# Productivity Analysis
# ------------------------------------------
print("\nAverage Productivity by Duration:")
print(df.groupby("Duration_Category")["Productivity_Score"].mean())

print("\nAverage Productivity by Meeting Type:")
print(df.groupby("Meeting_Type")["Productivity_Score"].mean())

# ------------------------------------------
# Visualizations (Histograms)
# ------------------------------------------

# Histogram – Meeting Duration
plt.figure(figsize=(8,5))
plt.hist(df["Duration_Minutes"], bins=8, color="skyblue", edgecolor="black")
plt.title("Histogram of Meeting Duration")
plt.xlabel("Duration (Minutes)")
plt.ylabel("Frequency")
plt.show()

# Histogram – Productivity Score
plt.figure(figsize=(8,5))
plt.hist(df["Productivity_Score"], bins=6, color="lightgreen", edgecolor="black")
plt.title("Histogram of Productivity Score")
plt.xlabel("Productivity Score")
plt.ylabel("Frequency")
plt.show()

# Box Plot – Duration vs Productivity
plt.figure(figsize=(8,5))
sns.boxplot(x="Duration_Category", y="Productivity_Score", data=df)
plt.title("Meeting Duration vs Productivity")
plt.show()

# ------------------------------------------
# Correlation Analysis
# ------------------------------------------
correlation = df[
    ["Duration_Minutes", "Number_of_Attendees", "Productivity_Score"]
].corr()

print("\nCorrelation Matrix:")
print(correlation)

sns.heatmap(correlation, annot=True, cmap="coolwarm")
plt.title("Correlation Heatmap")
plt.show()

# ------------------------------------------
# Conclusion
# ------------------------------------------
print("\nConclusion:")
print("Short and medium meetings are more productive.")
print("Long meetings and higher attendance reduce efficiency.")
print("Optimizing meeting duration improves productivity.")
