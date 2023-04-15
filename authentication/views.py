from django.shortcuts import render
from django.views.generic import View
from django.http import HttpResponse	
# Create your views here.


class SignUpView(View):
	# template_name=''
	def get(self, request, *args, **kwargs):
		return render(request, template_name)

	def post(self, request, *args, **kwargs):
		pass
