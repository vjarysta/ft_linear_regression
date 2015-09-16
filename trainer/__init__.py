from data_class	import Data
from display	import display
from sys		import argv

def main():
	if (len(argv) != 2):
		print('Usage: %s [data_file.csv]' % argv[0])
		exit()
	data = Data(argv[1])
	data.guess_thetas()
	data.save()
	display(data)
