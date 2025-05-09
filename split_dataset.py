import pandas as pd
from sklearn.model_selection import train_test_split

# Load your original dataset
data = pd.read_csv("data\ADNI_Training_Q3_APOE_CollectionADNI1Complete 1Yr 1.5T_July22.2014.csv")  # Update path to your dataset

# Split into training and test sets (80% train, 20% test)
train_data, test_data = train_test_split(data, test_size=0.2, random_state=42)

# Save the training and test datasets
train_data.to_csv("data/train_data.csv", index=False)
test_data.to_csv("data/test_data.csv", index=False)

print(f"Training dataset saved with {len(train_data)} samples.")
print(f"Test dataset saved with {len(test_data)} samples.")