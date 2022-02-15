import numpy as np

from src.data_module.sample_data import DataGenerator

class TestDataGenerator:
	def test_data_generation(self):

		num_rows = 10
		num_cols = 3

		data_generator = DataGenerator()

		actual_X, actual_y = data_generator.generate_logistic_data(num_points=num_rows, num_features=num_cols)

		assert actual_X.shape == (num_rows, num_cols)
		assert actual_y.shape == (num_rows, )