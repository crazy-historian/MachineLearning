import numpy as np


class DataArray:

    def __init__(self):
        self.type = np.dtype([('name', np.unicode, 16), ('parameters', np.float32, 4)])
        self.array = np.array([], dtype=self.type)
        self.index = -1

    def read_file(self, file_name):
        try:
            file = open(file_name, 'r')
            file.readline()
            while True:
                line = file.readline()
                if not line:
                    file.close()
                    break
                data = line.split(',')
                new_iris = np.array([(data[4], (data[:4]))], dtype=self.type)
                self.array = np.append(self.array, new_iris)
        except IOError:
            print('C файлом что-то не так')

    def metrics(self, list_a, list_b):
        summary = np.float32(0.0)
        for a, b in zip(list_a, list_b):
            summary += (a - b) ** 2
        return np.sqrt(summary)

    def __repr__(self):
        print(self.array)

    def __iter__(self):
        return self

    def __next__(self):
        if self.index < self.array.__len__()-1:
            self.index += 1
            return self.array[self.index]
        else:
            raise StopIteration


if __name__ == "__main__":
    iris_array = DataArray()
    iris_array.read_file('iris.csv')
    for iris in iris_array:
        print(iris)
