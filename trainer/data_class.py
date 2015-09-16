from re 	import compile as re_compile
from sys	import exit

class Data:
	def __init__(self, file_name):
		self.data_set = []
		self.file_name = file_name
		self.theta0 = 0.0
		self.theta1 = 0.0
		self.scale = 1.0
		self.scaled_min = 0.0
		self.data_names = ""
		
		self._parse()

	def _h(self, mileage):
		return (self.theta1 * mileage + self.theta0)

	def _parse(self):
		try:
			fd = open(self.file_name, 'r')
		except IOError:
			print('Could not open file!')
			exit()
		datas = list(fd)
		self.data_names = datas[0]
		for line in datas[1:]:
			line = line.replace('\n', '')
			splitted_line = line.split(',')
			self.data_set.append((float(splitted_line[0]), float(splitted_line[1])))
		fd.close()

	def _feature_scaling(self):
		x_set = [x[0] for x in self.data_set]
		min_x = min(x_set)
		max_x = max(x_set)
		self.scale = max_x - min_x
		self.scaled_min = min_x / self.scale
		self.data_set = [((x[0] - min_x) / self.scale, x[1]) for x in self.data_set]

	def guess_thetas(self):
		self._feature_scaling()
		tmp_theta0 = 1.0
		tmp_theta1 = 1.0
		learning_rate = 0.1
		while(abs(tmp_theta0) > 0.001 and abs(tmp_theta1) > 0.001):
			sum_theta_0 = sum([self._h(self.data_set[i][0] + self.scaled_min) - self.data_set[i][1] for i in range(len(self.data_set))])
			sum_theta_1 = sum([(self._h(self.data_set[i][0] + self.scaled_min) - self.data_set[i][1]) * self.data_set[i][0] for i in range(len(self.data_set))])
			tmp_theta0 = learning_rate * sum_theta_0 / len(self.data_set)
			tmp_theta1 = learning_rate * sum_theta_1 / len(self.data_set)
			self.theta0 -= tmp_theta0
			self.theta1 -= tmp_theta1
		self.theta1 /= self.scale

	def save(self):
		regex = re_compile('(.+)\.csv$')
		new_name = regex.sub('\\1_thetas.csv', self.file_name)
		fd = open(new_name, 'w')
		new_data = self.data_names + str(self.theta0) + ',' + str(self.theta1)
		fd.write(new_data)
		fd.close()
