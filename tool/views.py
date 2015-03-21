from django.shortcuts import render

def item_list(request):
	return render(request, 'tool/item_list.html', {})
