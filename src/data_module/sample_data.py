import numpy as np
from typing import Tuple

class DataGenerator:

	""" A class used to generate sample data
	"""

	def __init__(self):
		pass

	def generate_logistic_data(
		self,
		num_points: int = 10,
		num_features: int  = 5
	) -> Tuple[np.ndarray, np.ndarray]:
		""" Create an X and y matrix used to train logistic regression models

		Parameters
		----------
		num_points: int
			The number of data points to generate
		num_features: int
			The number of features to generate per data point
		"""

		X = np.zeros((num_points, num_features))
		y = np.zeros(num_points)

		# set first half of matrix to -1, second half to 1
		X[:num_points // 2, :] = -1.0
		X[num_points // 2:, :] = 1.0

		X += np.random.rand(num_points, num_features)

		y[:num_points // 2] = False
		y[num_points // 2:] = True

		return (X, y)


