import numpy as np

np.random.seed(7)

readings = np.random.randint(20, 41, size=(6, 3))

print("Sensor Readings:")
print(readings)

mean = readings.mean(axis=0)
std = readings.std(axis=0)

print("Mean per sensor:", mean)

# Standardize each sensor using broadcasting
normalized = (readings - mean) / std

print("Normalized column means:", normalized.mean(axis=0))

print("Hour of max per sensor:", readings.argmax(axis=0))

# Append the mean row below the sensor readings
new_readings = np.vstack([readings, mean])
print("New shape:", new_readings.shape)

# Generate the same readings again using the same seed
np.random.seed(7)
readings2 = np.random.randint(20, 41, size=(6, 3))

print("Reproducible:", np.array_equal(readings, readings2))

# Print the overall hottest sensor reading
print("Overall hottest reading:", readings.max())