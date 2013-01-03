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

from models import Board, Link, LinkForm, BoardForm


def home(request):

	linkform = LinkForm()
	boardform = BoardForm()

	panels = []
	[panels.append( ast.literal_eval(panel['data']) ) for panel in Link.objects.all().order_by('-date_created').values('data')]

	boards = []
	for board in Board.objects.all():
		boards.append( { 'name': board.name, 'links': Link.objects.filter(board_id=board.id)[:5] } )

	# assert False

	context = { 
		'linkform': linkform, 
		'boardform': boardform, 
		'panels': panels, 
		'boards': boards,
	}

	return render_to_response('home.html', context , context_instance=RequestContext(request))

def process_link(request):

	f = LinkForm(request.POST)
	f.save()

	return HttpResponseRedirect('/');


def process_board(request):

	f = BoardForm(request.POST)
	f.save()

	return HttpResponseRedirect('/');