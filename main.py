import numpy as np

filename = 'data/iris.csv'

if __name__ == '__main__':
    data = np.loadtxt(filename, skiprows=1, delimiter=',', usecols=range(3))
    means = np.mean(data, axis=0)
    medians = np.median(data, axis=0)
    stds = np.std(data, axis=0)
    print(f"Array of means of following columns: {means}")
    print(f"Array of medians of following columns: {medians}")
    print(f"Array of stds of following columns: {stds}")

