import datetime

from django.http import HttpResponse
from django.template import RequestContext
from django.shortcuts import render_to_response

from embedly import Embedly


def home(request):

	client = Embedly('2a50c783d3a84c3ebf95950fa34f6df2')

	url_list = [
			'http://www.shockoe.com/blog/typingcodeout/',
			'http://pkarl.com',
			'http://lostechies.com/derickbailey/2012/12/14/dear-open-source-project-leader-quit-being-a-jerk/',
			'http://blog.alfredapp.com/2012/12/14/v2-sneak-peek-workflows/',
			'http://www.bbc.co.uk/news/uk-20730627',
			'http://pinterest.com',
			'http://ngm.nationalgeographic.com/',
			'http://jpboneyard.com',
			'http://www.jeffvlahos.com',
		]

	url_data = []

	for url in url_list:
		url_data.append(client.oembed(url).__dict__['data'])

	return render_to_response('home.html', {'panels': url_data }, context_instance=RequestContext(request))