from sklearn.metrics import confusion_matrix, roc_auc_score
import matplotlib.pyplot as plt

def plot_confusion(y_true, y_pred):
    cm = confusion_matrix(y_true, y_pred)
    plt.imshow(cm, cmap='Blues')
    plt.title("Confusion Matrix")
    plt.colorbar()
    plt.xlabel("Predicted")
    plt.ylabel("Actual")
    plt.show()

def print_roc_auc(clf, X_test, y_test):
    if hasattr(clf, "predict_proba"):
        probs = clf.predict_proba(X_test)[:, 1]
        print("ROC AUC:", roc_auc_score(y_test, probs))
