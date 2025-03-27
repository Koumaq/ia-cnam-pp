import matplotlib.pyplot as plt
import pandas as pd
from sklearn.linear_model import LinearRegression

# Load the data
train_data = pd.read_csv("../datasets/salary_train.csv")
test_data = pd.read_csv("../datasets/salary_test.csv")

# Prepare the data
X_train = train_data.drop("salary", axis=1)
y_train = train_data["salary"]

X_test = test_data.drop("salary", axis=1)
y_test = test_data["salary"]

model = LinearRegression()
model.fit(X_train, y_train)

y_pred = model.predict(X_test)

# Plot the data

plt.scatter(X_test["years_of_experience"], y_test)
plt.plot(X_test["years_of_experience"], y_pred, color="red")
plt.xlabel("Years of experience")
plt.ylabel("Salary")
plt.title("Years of experience vs Salary")
plt.show()
