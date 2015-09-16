from sys import exit, argv
from re import findall

def estimate_price(value, theta_0, theta_1):
	return (theta_1 * value + theta_0)

def open_file(file_name):
	try:
		fd = open(argv[1])
	except IOError:
		print('Could not open file!')
		exit()
	return fd

def get_input(data_name):
	try:
		value = float(input('Enter your value (%s)\n' % data_name))
	except ValueError:
		print('Wrong format!')
		exit()
	return value

def main():
	if (len(argv) != 2):
		print('Usage: %s [thetas_file.csv]' % argv[0])
		exit()
	datas = list(open_file(argv[1]))
	data_names = datas[0].replace('\n', '').split(',')
	thetas = datas[1].replace('\n', '').split(',')
	value = get_input(data_names[0])
	price = int(estimate_price(value, float(thetas[0]), float(thetas[1])))
	print('Result: %d (%s).' % (price, data_names[1]))
