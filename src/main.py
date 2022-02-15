from data_module.sample_data import DataGenerator
from model_module.simple_model import LogisticRegression

if __name__ == '__main__':

	num_rows = 25
	num_cols = 5

	X, y = DataGenerator().generate_logistic_data(num_rows, num_cols)

	print("Training X")
	print(X)
	print("Training y")
	print(y)

	model = LogisticRegression().fit(X, y)
	predictions = model.predict(X)

	print("Predictions on X")
	print(predictions)