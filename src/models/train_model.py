def train_randomforest(model, X_train, y_train):
    """
    Train model
    
    Parameters
    ----------
    model: sklearn.base.BaseEstimator
        Instantiated Sklearn model with set hyperparameters
    X_train: Numpy Arrays
        Features of training dataset
    y_train: Numpy Arrays
        Target variable of training dataset

    Returns
    -------
    sklearn.base.BaseEstimator
        Trained model
    """
    
    model.fit(X_train, y_train.values.ravel())
    
    return model