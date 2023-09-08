def predict_model(model, X_train, X_val, X_test):
    """
    Generate prediction probabilities for the drafted variable on the training, validation and testing sets
    
    Parameters
    ----------
    model: sklearn.base.BaseEstimator
        Instantiated Sklearn model with set hyperparameters
    X_train: Numpy Arrays
        Features of training dataset
    X_val: Numpy Arrays
        Features of validation dataset
    X_test: Numpy Arrays
        Features of testing dataset

    Returns
    -------
    preds_proba_train: Numpy Arrays
        Prediction probability on the training set
    preds_proba_val: Numpy Arrays
        Prediction probability on the validation set
    preds_proba_test: Numpy Arrays
        Prediction probability on the testing set
    """
    
    preds_proba_train = model.predict_proba(X_train)[:, 1] 
    preds_proba_val = model.predict_proba(X_val)[:, 1] 
    preds_proba_test = model.predict_proba(X_test)[:, 1]
    
    return preds_proba_train, preds_proba_val, preds_proba_test