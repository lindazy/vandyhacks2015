from Bio import Entrez
from Bio import Medline
import numpy as np
import scipy
from sklearn.cluster import KMeans
from collections import defaultdict

def search_pub_med(term): 
	MAX_COUNT = 20
	TERM = term #'Tuberculosis'
	 
	print 'Getting %d publications containing %s' % (MAX_COUNT, TERM)
	Entrez.email = 'A.N.Other@example.com'
	h = Entrez.esearch(db='pubmed', retmax=MAX_COUNT, sort='relevance', term=TERM)
	result = Entrez.read(h)
	print 'Total number of publications containing %s: %s' %(TERM, result['Count'])
	ids = result['IdList']
	h = Entrez.efetch(db='pubmed', id=ids, rettype='medline', retmode='text')
	records = Medline.parse(h)
	print records
	 
	data = []
	for record in records:
		title = record.get('TI','?')
		abstract = record.get('AB','No abstract given.')
		mesh = record.get('MH','')
		data.append((title,abstract,mesh))
	return data

class KMeansCluster:
	def __init__(self, n, data):
		self.clustered_data = defaultdict(list)
		self.k_means = KMeans(n_clusters = n)
		self.find_cluster(n, data)

	def find_cluster(self, n, data):
		self.k_means.fit(data)
		clusters = self.k_means.predict(data)

		for i in xrange(data.shape[0]):
			self.clustered_data[clusters[i]].append(i)

	def get_cluster(self):
		return self.clustered_data

if __name__=='__main__':
	query = raw_input('Enter query.\n')
	data = search_pub_med(query)
	for record in data:
		print record
