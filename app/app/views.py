"""
	I usually organize module imports as follows:

	python core/contrib modules
	3rd party modules
	django core/contrib modules
	django project modules

	...and then shortcuts/etc. if applicable
"""
import datetime, ast

from django.http import HttpResponse, HttpResponseRedirect
from django.template import RequestContext
from django.shortcuts import render_to_response

from django.core.validators import URLValidator
from django.core.exceptions import ValidationError

from models import Link, LinkForm


def home(request):

	# 		'http://www.shockoe.com/blog/typingcodeout/',
	# 		'http://pkarl.com',
	# 		'http://lostechies.com/derickbailey/2012/12/14/dear-open-source-project-leader-quit-being-a-jerk/',
	# 		'http://blog.alfredapp.com/2012/12/14/v2-sneak-peek-workflows/',
	# 		'http://www.bbc.co.uk/news/uk-20730627',
	# 		'http://pinterest.com',
	# 		'http://ngm.nationalgeographic.com/',
	# 		'http://jpboneyard.com',
	# 		'http://www.jeffvlahos.com',

	form = LinkForm()

	panels = []
	[panels.append( ast.literal_eval(panel['data']) ) for panel in Link.objects.all().reverse().values('data')]

	return render_to_response('home.html', { 'form': form, 'panels': panels } , context_instance=RequestContext(request))

def process_url(request):

	f = LinkForm(request.POST)
	link = f.save()

	return HttpResponseRedirect('/');