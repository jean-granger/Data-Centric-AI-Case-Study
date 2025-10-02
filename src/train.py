import joblib
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import classification_report, accuracy_score

def train_and_eval(X, y, save_model_path=None):
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
    clf = RandomForestClassifier(n_estimators=100, random_state=42)
    clf.fit(X_train, y_train)
    preds = clf.predict(X_test)
    print("Accuracy:", accuracy_score(y_test, preds))
    print(classification_report(y_test, preds))
    if save_model_path:
        joblib.dump(clf, save_model_path)
    return clf, X_test, y_test, preds
