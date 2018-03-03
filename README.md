# Overview
This repository contains python implementations of various machine learning algorithms as regular sklearn **estimators**. 
Many famous machine learning algorithms has been implemented and their accuracy is compared with sklearn's inbuilt implementation of these algorithms.
Each custom implementation inherits **BaseEstimator** and **ClassifierMixin** or **RegressionMixin**, and follows sklearn's standards for implementing these estimators.
Since these implementations are implemented as regular sklearn estimators, this gives us full access to sklearn API.
Each jupyter notebook contains a major machine learning algorithm with their common implementations and variations.
<br><br>
The goal of these implementations is to understand the inner workings of these algorithms along with thier mathematics.
Therefore code is well commented and mathematical intituions and equations has been written for better understanding.

# Algorithms
## Linear Regression
* Lasso
* Ridge
* ElasticNet
* SGDRegressor

> NOTE: An implementation with Stochastic Gradient Descent (SGD) optimization is also implemented.


## KNN
* KNN
* Weighted KNN (inverse-distance function as weights)

> NOTE: Both KNN classifiers and regressors are implemented.

## Fuzzy KNN
## KMeans
## Naive Bayes
* Simple NB
* Gaussian NB

###### MORE COMING...
* Logistic Regression
* MeanShift
* Decision Tree
* SVM

# Similar Repositories
* [Senticircle Algorithm](https://github.com/sahilsehwag/Senticircle-Implementation)
* [Fuzzy KNN](https://github.com/sahilsehwag/FuzzyKNN)
* [Python Implementation of Various Data Structures](https://github.com/sahilsehwag/data-structures-python)
* [Python Implementation of Various Algorithms](https://github.com/sahilsehwag/algorithms-python)
