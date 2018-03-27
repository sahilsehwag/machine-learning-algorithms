# Overview
This repository contains python implementations of various machine learning algorithms as regular sklearn **estimators**. 
Many famous machine learning algorithms has been implemented and their accuracy is compared with sklearn's inbuilt implementation of these algorithms.
Each custom implementation inherits **BaseEstimator** and **ClassifierMixin** or **RegressionMixin**, and follows sklearn's standards for implementing these estimators.
Since these implementations are implemented as regular sklearn estimators, this gives us full access to sklearn API.
Each jupyter notebook contains a major machine learning algorithm with their common implementations and variations.
<br><br>
The goal of these implementations is to understand the inner workings of these algorithms along with thier mathematics.
Therefore code is well commented and mathematical intituions and equations has been written for better understanding.

# Checklist
Since these algorithm implementations are implemented so that anyone wanting to learn or implement various machine learning algorithms can
easily understand, experiment, explore and refer, each algorithm has a checklist:
<br>
* **sklearn**: *If implemented as an Scikit-Learn estimator/transformer etc...*
* **score comparison**: *If a score/result comparison with sklearn's inbuilt implementations.*
* **notes**: *If notebook contains notes and explanation about the working of algorithm along with its **MATHS**.*
* **commented/documented**: *If code is well documented/commented for easy understanding for someone trying to learn.*
* **visualization**: *If visualization regarding the results/working of the algorithms are provided to aid the learning and exploring process.*


# Algorithms
## Supervised Algorithms


**Linear Regression**
* **Implementations**
	* Simple Linear Regression
	* Multiple Linear Regression
	* SGDRegressor
* **Regularization**
	* Lasso
	* Ridge
	* ElasticNet
* **Checklist**
	* ✓ sklearn
	* ✓ score comparison
> NOTE: An implementation with Stochastic Gradient Descent (SGD) optimization is also implemented.


**Logistic Regression**
* **Implementations**
	* Logistic Regression (*Gradient Descent*)
	* SGDClassifier (*Stochastic Gradient Descent*)
* **Checklist**
	* ✓ sklearn
	* ✓ score comparison


**KNN**
* **Implementations**
	* KNN
	* Weighted KNN (***inverse-distance** function as weights*)
* **Visualization**
	* Results
	* Decision Boundary
	* Voronoi Tesselation
* **Checklist**
	* ✓ sklearn
	* ✓ score comparison
	* ✓ visualization
> NOTE: Both KNN classifiers and regressors are implemented.


**Fuzzy KNN**
* Initialization Techniques
	* Crisp Initialization **@TODO**
	* Fuzzy Initialization
* **Checklist**
	* ✓ sklearn
	* ✓ score comparison


**Naive Bayes**
* **Implementations**
	* Simple NB
	* Gaussian NB
	* Multinomial NB
* **Checklist**
	* ✓ sklearn
	* ✓ score comparison


**Decision Trees**
* DecisionTreeClassifier
	* Splitting Criterion
		* GINI Impurity
		* Gain Ratio **@TODO**
	* **Checklist**
		* ✓ sklearn
		* ✓ score comparison
		* ✓ commented
* DecisionTreeRegressor **@TODO**


## Unsupervised Algorithms
### Flat Clustering


**KMeans**
* **Visualization**
	* Results
	* Decision Boundary
	* Skree Plot
	* Visualizing Sillhouette scores
* **Miscellanous Algorithms**
	* k Estimation using Sillhouette Analysis
* **Checklist**
	* ✓ sklearn
	* ✓ score comparison
	* ✓ visualization


**KMedoids**
* **Implementations**
	* PAM (Partitioning Around Medoids)
* **Visualization**
	* Results
* **Checklist**
	* ✓ sklearn
	* ✓ score comparison


### Heirarchical Clustering
**MeanShift**
* **Checklist**
	* ✓ sklearn
	* ✓ score comparison


### Soft Clustering


## Dimensionality Reduction Algorithms
### Feature Selection
### Feature Extraction
**PCA (Principal Component Analysis)**
* **Checklist**
	* ✓ sklearn
	* ✓ score comparison


## Anomaly/Outlier Detection Algorithms
## Association Rule Mining Algorithms
## Neural Networks
## Miscellanous Algorithms


<br>
###### MORE COMING...
* SVM
* LDA
* Fuzzy CMeans
* Similarity Metrics/Functions
* Gradient Descent (*Momentum*, *ADAM*...)
* MedoidShift
* Softmax Regression
* Local Outlier Factor
* Heirarchical KMeans
* Nearest Centroid Classifier
* Radius Neighbors (Parzen Windows)


# Similar Repositories
* [Senticircle Algorithm](https://github.com/sahilsehwag/Senticircle-Implementation)
* [Fuzzy KNN](https://github.com/sahilsehwag/FuzzyKNN)
* [Python Implementation of Various Data Structures](https://github.com/sahilsehwag/data-structures-python)
* [Python Implementation of Various Algorithms](https://github.com/sahilsehwag/algorithms-python)
