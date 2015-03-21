from django.shortcuts import render, redirect
from .models import Item
from .pub_med import search_pub_med

def item_list(request):
	if request.method == 'POST':
		#new_item_query = request.POST['item_query']
		#search_pub_med(new_item_query)
		#return HttpResponseRedirect(reverse(test_result))
		new_item_query = request.POST['item_query']
		Item.objects.create(query=request.POST['item_query'])
		return redirect('/')
	items = Item.objects.all()
	return render(request, 'tool/item_list.html', {'items':items})
