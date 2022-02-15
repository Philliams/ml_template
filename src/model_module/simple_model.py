import numpy as np
import math

class LogisticRegression:

	""" Fits a logistic regression model to binary classification data

	Args:
		use_bias: bool
			A flag to enable or disable a bias term in the regression
	"""

	def __init__(self, use_bias: bool=True):
		self.use_bias = use_bias
		self.weights = None

	def augment_matrix(self, X: np.ndarray) -> np.ndarray:
		""" Augment a matrix with a dummy feature to include a bias term in the regression

		Parameters
		----------
		X: np.ndarray
			numpy array corresponding to the feature matrix. Each row is a data point
			each column is a feature/variable
		"""

		# create a matrix full of 1's with one more column than X
		augmented_X = np.full((X.shape[0], X.shape[1] + 1), 1.0)
		# copy X over the first N column of the new matrix, preserving the last 1's column
		augmented_X[:, :-1] = X

		return augmented_X

	def fit(self, X: np.ndarray, y: np.ndarray):
		"""Will fit a logistic regression model on an input matrix X and
		a target vector y

		Parameters
		----------
		X: np.ndarray
			numpy array corresponding to the feature matrix. Each row is a data point
			each column is a feature/variable
		y: np.ndarray
			numpy array corresponding to the 1D target vector
		"""

		if self.use_bias:
			X = self.augment_matrix(X)

		# create a vector of 0's of the same size as the target
		# will be used to convert True/False classification into
		# a numerical target for OLS
		y_inverted = np.zeros(y.shape[0])

		# True/False values are converted to 1 and 0
		# Next, the 1/0 values are converted to 0.9 and 0.1 (see label smoothing for more info)
		# Then, 0.9 and 0.1 are passed through the inverse sigmoid function to obtain a numerical
		# target for OLS linear regression
		true_value = math.log(0.9 / (1 - 0.9))
		false_value = math.log(0.1 / (1 - 0.1))

		# set true labels to true value
		y_inverted[y == True] = true_value
		# set false labels to false value
		y_inverted[y == False] = false_value

		# compute matrices for OLS regression
		gram_matrix = np.matmul(X.transpose(), X)
		moment_matrix = np.matmul(X.transpose(), y_inverted)

		# compute weights of linear model
		self.weights = np.matmul(np.linalg.inv(gram_matrix), moment_matrix)

		return self


	def predict(self, X: np.ndarray) -> np.ndarray:
		""" Classify a matrix using the trained Logistic model

		Parameters
		----------
		X: np.ndarray
			numpy array corresponding to the feature matrix. Each row is a data point
			each column is a feature/variable

		Returns
		----------
		predictions: np.ndarray
			a numpy array corresponding to the prediction vector
		"""

		if self.use_bias:
			X = self.augment_matrix(X)

		raw_predictions = np.matmul(X, self.weights)

		# use logistic equation to get true/false score
		return 1.0 / (1.0 + np.exp(-raw_predictions))