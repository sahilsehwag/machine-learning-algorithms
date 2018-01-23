import numpy as np
import sys
import pprint
import matplotlib.pyplot as plt

#KMEANS
class KMeans:
	#CONSTRUCTOR
	def __init__(self, k, tolerance=0.001, max_iterations=300):
		self.k = k
		self.tolerance = tolerance
		self.max_iterations = max_iterations
	#CONSTRUCTOR

	#PRIVATE CONSTRUCTOR
	@property
	def _centroids(self):
		return np.array(list(self.centroids.values()))

	@property
	def _clusters(self):
		for i in self.clusters:
			self.clusters[i] = np.array(self.clusters[i])
		return self.clusters
	#PRIVATE CONSTRUCTOR

	#METHODS
	def train(self, points):
		self.centroids = {}

		# initially setting centroids as first "k" points(feature sets)
		for i in range(self.k):
			self.centroids[i] = points[i]

		self.clusters = {}
		for _ in range(self.max_iterations):
			for i in range(self.k):
				self.clusters[i] = []

			# iterating over points and adding it to closest cluster point belongs
			for point in points:
				# computing eucledian distances of current point from each centroid
				distances = [np.linalg.norm(self.centroids[centroid]-point) for centroid in self.centroids]

				# getting index of closest cluster
				index = np.argmin(distances)

				# appending point(feature set) to list of cluster it belongs to
				self.clusters[index].append(point)

			old_centroids = dict(self.centroids)
			for i in self.clusters:
				# computing new centroid by taking mean of all points in current cluster
				centroid = np.average(self.clusters[i], axis=0)

				self.centroids[i] = centroid

			bools = [True if np.array_equal(self.centroids[k], old_centroids[k]) else False for k in range(self.k)]
			if all(bools):
				break


	def predict(self, point):
		# computing  eucledian distances between given point and centroids
		distances = [np.linalg.norm(centroid-point) for centroid in self.centroids]

		# return cendroid with minimum distance
		return distances.argmin()


	def plot(self):
		colors = ['g', 'r', 'b', 'y', 'm']

		# plotting clusters
		for i in self._clusters:
			plt.scatter(self._clusters[i][:,0], self._clusters[i][:,1], s=25, color=colors[i%5])

		# plotting centroids
		plt.scatter(self._centroids[:,0], self._centroids[:,1], marker='x', color='pink')
		plt.show()
	#METHODS
#KMEANS
