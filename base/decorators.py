from django.http import HttpResponse
from django.shortcuts import redirect

def admin_only(view_func):
	def wrapper_function(request, *args, **kwargs):
		user = request.user
		if user.is_authenticated and user.is_superuser:
			return view_func(request, *args, **kwargs)
		else:
			return HttpResponse('You are not authorized to view this page')
			
	return wrapper_function