import numpy as np

from src.model_module.simple_model import LogisticRegression

class TestLogisticRegression:
	def test_logistic_regression(self):

		num_rows = 10
		num_cols = 3

		X = np.full((num_rows, num_cols), 0.0) + np.random.rand(num_rows, num_cols)
		y = np.full(num_rows, False)

		model = LogisticRegression()

		actual = model.fit(X, y).predict(X)

		assert actual.shape == y.shape