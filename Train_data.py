# # Python
# import pandas as pd
# from sklearn.model_selection import train_test_split
# from sklearn.ensemble import RandomForestClassifier
# from sklearn.metrics import accuracy_score

# # Load data
# data = pd.read_csv('sample_data.csv')

# # Features and target
# X = data[['files_changed', 'test_pass_rate', 'build_time_sec']]
# y = data['deploy_success']

# # Split data into training and testing sets
# X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# # Train RandomForestClassifier
# model = RandomForestClassifier(random_state=42)
# model.fit(X_train, y_train)

# # Predict and evaluate
# y_pred = model.predict(X_test)
# accuracy = accuracy_score(y_test, y_pred)
# print(f"Accuracy: {accuracy:.2f}")



import pandas as pd
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import train_test_split
import joblib
# Load Data
df = pd.read_csv('sample_data.csv')
X = df[['files_changed', 'test_pass_rate', 'build_time_sec']]
y = df['deploy_success']
# Train-Test Split
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2)
# Train Model
model = RandomForestClassifier()
model.fit(X_train, y_train)
# Save Model
joblib.dump(model, 'deploy_predictor.pkl')