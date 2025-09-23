from sklearn import datasets
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier as rfc
import joblib


# Load dataset
iris = datasets.load_iris()
X = iris.data
y = iris.target
# Split dataset into training and testing sets
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Train a RandomForestClassifier
model=rfc(n_estimators=100, random_state=42)
#model.fit(X_train, y_train)
# Save the trained model to a file
#joblib.dump(model, 'iris_model.pkl')
