# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render



def index(request):
	tienda = {'name':'Tienda numero uno'}

	template_name = "browser/index.html"
	context = {'tienda': tienda}

	return render(request = request, template_name = template_name, context = context)