import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from scipy.stats import entropy  # Import entropy function from SciPy

# Load dataset
df = pd.read_csv("winequality-red.csv", delimiter=";")

# Compute Statistical Measures
stats_df = pd.DataFrame({
    'Mean': df.mean(),
    'Variance': df.var(),
    'Skewness': df.skew(),
    'Entropy': df.apply(lambda x: entropy(np.histogram(x, bins=10)[0]), axis=0)
})

# Display the computed statistics
print(stats_df)

# 🔹 Visualizing Importance of Statistics
plt.figure(figsize=(12, 6))
sns.heatmap(stats_df.corr(), annot=True, cmap="coolwarm", fmt=".2f")
plt.title("Correlation Between Statistical Measures")
plt.show()

# 🔹 Which Statistical Measure Predicts Wine Quality?
corr_with_quality = stats_df.corrwith(df['quality'])
print("Correlation of statistical measures with wine quality:")
print(corr_with_quality)

# 🔹 Impact of High Entropy on Classification
high_entropy_features = stats_df[stats_df['Entropy'] > stats_df['Entropy'].median()].index
low_entropy_features = stats_df[stats_df['Entropy'] <= stats_df['Entropy'].median()].index

print(f"High Entropy Features: {list(high_entropy_features)}")
print(f"Low Entropy Features: {list(low_entropy_features)}")

# 🔹 Effect of Dropping High Variance Features
high_variance_features = stats_df[stats_df['Variance'] > stats_df['Variance'].median()].index
df_reduced = df.drop(columns=high_variance_features)

print(f"Dropped High Variance Features: {list(high_variance_features)}")
print(f"New dataset shape after dropping high-variance features: {df_reduced.shape}")
