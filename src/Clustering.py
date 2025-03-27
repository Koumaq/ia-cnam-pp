import matplotlib.pyplot as plt
import pandas as pd
from sklearn.cluster import KMeans
from sklearn.preprocessing import StandardScaler

data = pd.read_csv("../datasets/customer_train.csv")

scaler = StandardScaler()
features_scaled = scaler.fit_transform(data)
features_scaled_df = pd.DataFrame(features_scaled, columns=data.columns)

k = 3
model = KMeans(n_clusters=k, random_state=42)
data["cluster"] = model.fit_predict(features_scaled)

# Create scatter plots for different feature combinations
fig = plt.figure(figsize=(15, 5))

# Income vs Spending Score
plt.subplot(1, 3, 1)
plt.scatter(data["annual_income"], data["spending_score"], c=data["cluster"])
plt.xlabel("Annual Income")
plt.ylabel("Spending Score")
plt.title("Income vs Spending Score")


# Age vs Spending Score
plt.subplot(1, 3, 2)
plt.scatter(data["age"], data["spending_score"], c=data["cluster"])
plt.xlabel("Age")
plt.ylabel("Spending Score")
plt.title("Age vs Spending Score")


# Age vs Income
plt.subplot(1, 3, 3)
plt.scatter(data["age"], data["annual_income"], c=data["cluster"])
plt.xlabel("Age")
plt.ylabel("Annual Income")
plt.title("Age vs Income")

plt.tight_layout()
plt.show()
