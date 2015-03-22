from django.shortcuts import render, redirect
from .models import Item, Paper, Mesh, ListField
from .pub_med import search_pub_med, KMeansCluster
import numpy as np
import scipy

MESH_CATEGORY = ['A','B','C','D','E','F','G','H','I','J','K','L','M','N','V','Z']
N_CLUSTERS = 3

def item_list(request):
	if Mesh.objects.count() < 1:
		with open('tool/terms.txt','rb') as f:
			data = f.readlines()
		for term in data:
			t = term.rstrip().split('\t')
			Mesh.objects.create(term=t[0], category=t[1])

	if request.method == 'POST':
		new_item_query = request.POST['item_query']
		Item.objects.create(query=request.POST['item_query'])
		results = search_pub_med(new_item_query)
		for i in xrange(len(results)):
			mesh_list = Mesh.objects.filter(term__in=results[i][2])
			mesh_bin = [0]*len(MESH_CATEGORY)
			for c in mesh_list:
				mesh_bin[MESH_CATEGORY.index(c.category)] = 1
			Paper.objects.create(query=new_item_query, title=results[i][0], abstract=results[i][1], mesh=mesh_bin)
		return redirect('/')
	if Item.objects.count() > 0:
		last_query = Item.objects.latest('created_date')
		papers = Paper.objects.filter(query=last_query)

		x = np.zeros((len(papers),len(MESH_CATEGORY)))
		for row in xrange(x.shape[0]):
			for col in xrange(x.shape[1]):
				x[row,col] = papers[row].mesh[col]
		cluster = KMeansCluster(3, x)
		cluster_result = cluster.get_cluster()
		clusters = []
		for c in cluster_result:
			clusters.append([(c,papers[x]) for x in cluster_result[c]])
		return render(request, 'tool/item_list.html', {'clusters':clusters,'last_item':last_query})
	return render(request, 'tool/item_list.html', '')
