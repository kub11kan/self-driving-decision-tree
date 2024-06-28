import pandas as pd
from sklearn.tree import DecisionTreeClassifier
from sklearn.metrics import accuracy_score
from sklearn import tree

# File paths for training and validation data
train_file1 = "labels_train.csv"
val_file = "labels_val.csv"

# Read the CSV files into DataFrames
df_train = pd.read_csv(train_file1)
df_val = pd.read_csv(val_file)

# Check column names to ensure the target column exists
print("Columns in training DataFrame:", df_train.columns)
print("Columns in validation DataFrame:", df_val.columns)

# Define the correct target column name
target_column = 'class_id'

# Ensure the target column exists before proceeding
if target_column not in df_train.columns or target_column not in df_val.columns:
    raise KeyError(f"Column '{target_column}' not found in one of the DataFrames")

# Define features and target variables
features = ['xmin', 'xmax', 'ymin', 'ymax']
X_train = df_train[features]
y_train = df_train[target_column]
X_val = df_val[features]
y_val = df_val[target_column]

# Initialize and train the Decision Tree Classifier
model = DecisionTreeClassifier()
model.fit(X_train, y_train)

# Make predictions on the training set
train_predictions = model.predict(X_train)

# Calculate training accuracy
train_accuracy = accuracy_score(y_train, train_predictions)
print(f"Training Accuracy: {train_accuracy}")

# Validate the model on the validation set
val_accuracy = model.score(X_val, y_val)
print(f"Validation Accuracy: {val_accuracy}")

# Export the decision tree to a .dot file for visualization
tree.export_graphviz(
    model,
    out_file="Self_Driving_Car_Predictions.dot",
    feature_names=features,
    class_names=sorted(y_train.unique().astype(str)),
    label="all",
    rounded=True,
    filled=True
)

# Print the shapes of each DataFrame for verification
print("Shape of training DataFrame:", df_train.shape)
print("Shape of validation DataFrame:", df_val.shape)
