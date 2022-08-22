from sklearn.preprocessing import StandardScaler

# Create an instance of the StandardScaler
std = StandardScaler()

# Compute the statistics used by the StandardScaler
# based on the training data
std.fit(X_train)

# Transform the training and test data:

X_train_std = std.transform(X_train)
X_test_std = std.transform(X_test)

# Create and train an SGDClassifier
sgd_clf_std = SGDClassifier(random_state=20)
sgd_clf_std.fit(X_train_std, y_train)

# Compute the cross validation predictions on the training set
y_train_std_pred = cross_val_predict(sgd_clf, X_train_std, y_train, cv=5)

# Print the accuracy
print(f'The accuracy computed from cross validation is: {accuracy_score(y_train, y_train_std_pred)}')

# Print the confusion matrix
cm_std = confusion_matrix(y_train, y_train_std_pred)
print(f'Confusion matrix: \n {cm_std}')

# Print the F1 score
print(f'The F1 score is: {f1_score(y_train, y_train_std_pred)}')