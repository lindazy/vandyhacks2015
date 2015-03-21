from django.shortcuts import render, redirect
from .models import Item, Paper
from .pub_med import search_pub_med

def item_list(request):
	if request.method == 'POST':
		new_item_query = request.POST['item_query']
		Item.objects.create(query=request.POST['item_query'])
		results = search_pub_med(new_item_query)
		for i in xrange(len(results)):
			Paper.objects.create(query=new_item_query, title=results[i][0], abstract=results[i][1])
		return redirect('/')
		#new_item_query = request.POST['item_query']
		#Item.objects.create(query=request.POST['item_query'])
		#return redirect('/')
	#items = Item.objects.all()
	if Item.objects.count() > 0:
		last_query = Item.objects.latest('created_date')
		papers = Paper.objects.filter(query=last_query)
		return render(request, 'tool/item_list.html', {'papers':papers,'last_item':last_query})
	return render(request, 'tool/item_list.html', '')
