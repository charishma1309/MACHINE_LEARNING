import numpy as np
from sklearn.linear_model import LinearRegression
from veh_counting import*

np.random.seed(42)
vehicle_count = np.random.randint(50, 200, 100)
signal_time = 5 * vehicle_count + np.random.normal(scale=50, size=100)
# Reshape the data for a single feature
X = vehicle_count.reshape(-1, 1)
y = signal_time

# Create and train a linear regression model
model = LinearRegression()
model.fit(X, y)
print(model)
# Example: Predict signal time for a new vehicle count
new_vehicle_count = vc.dvc()  # Replace this with your actual vehicle count
predicted_signal_time = model.predict([[new_vehicle_count]])

# Display the result
print(f'Predicted Signal Time for {new_vehicle_count} vehicles: {predicted_signal_time[0]} seconds')