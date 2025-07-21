import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler, LabelEncoder
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import classification_report, accuracy_score

# Load dataset
df = pd.read_csv("C:/Users/Timon/OneDrive/Documents/R2_Purchase_Prediction.csv")

# Drop non-predictive column
df_model = df.drop(columns=['CUSTOMER_ID']).dropna()

# Encode categorical variables
label_encoders = {}
categorical_cols = ['ModeOfPayment', 'ResidentCity', 'Channel', 'CustomerPropensity']
for col in categorical_cols:
    le = LabelEncoder()
    df_model[col] = le.fit_transform(df_model[col])
    label_encoders[col] = le

# Define features and target
X = df_model.drop(columns='ProductChoice')
y = df_model['ProductChoice']

# Split dataset
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Normalize features
scaler = StandardScaler()
X_train_scaled = scaler.fit_transform(X_train)
X_test_scaled = scaler.transform(X_test)

# Train Random Forest model
model = RandomForestClassifier(random_state=42)
model.fit(X_train_scaled, y_train)

# Evaluate model
y_pred = model.predict(X_test_scaled)
print("Accuracy:", accuracy_score(y_test, y_pred))
print("Classification Report:\n", classification_report(y_test, y_pred))

# Predict on the first 5 samples from the test set
sample_real = X_test.iloc[:5]
sample_real_scaled = scaler.transform(sample_real)
predicted_classes = model.predict(sample_real_scaled)

# Combine predictions with original input
result_real = sample_real.copy()
result_real['Predicted_ProductChoice'] = predicted_classes
print(result_real)
