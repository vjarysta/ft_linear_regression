import matplotlib.pyplot as plt

def display(data):
	x_set = [(x[0] + data.scaled_min) * data.scale for x in data.data_set]
	y_set = [y[1] for y in data.data_set]
	plt.plot(x_set, y_set, 'ro')
	min_x = int(min(x_set))
	max_x = int(max(x_set))
	data_set = range(min_x, max_x)
	plt.plot(data_set, [data._h(x) for x in data_set], 'b')
	plt.show()
