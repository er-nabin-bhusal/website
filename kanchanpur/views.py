from django.shortcuts import render
from .models import MatchDate,Photos
import datetime

# Create your views here.

def home_view(request):

	template = 'kanchanpur/homepage.html'
	obj = MatchDate.objects.all()
	first = obj.first()
	return render(request,template,{'first':first})
def news_view(request):
	unknown = "No dates and link has been given"
	template = 'kanchanpur/news.html'
	datas = MatchDate.objects.all()
	if datas.count() == 1:
		firstone = datas.first()
		todaydate = datetime.date.today()
		if todaydate == firstone.upcoming_match:
			return render(request,template,{'data':firstone})
		elif todaydate < firstone.upcoming_match:
			return render(request,template,{'weblink':firstone})
		else:
			return render(request,template,{'gone':firstone})

	else:
		return render(request,template,{'unknown':unknown})


def team_view(request):
	template = 'kanchanpur/team.html'
	return render(request,template,{})

def developer_view(request):
	template = 'kanchanpur/developer.html'
	return render(request,template,{})

def ticket_view(request):
	template = 'kanchanpur/ticket.html'
	unknown = "No dates and link has been given"
	datas = MatchDate.objects.all()
	if datas.count() == 1:
		firstone = datas.first()
		todaydate = datetime.date.today()
		if todaydate == firstone.upcoming_match:
			return render(request,template,{'data':firstone})
		elif todaydate < firstone.upcoming_match:
			return render(request,template,{'weblink':firstone})
		else:
			return render(request,template,{'gone':firstone})

	else:
		return render(request,template,{'unknown':unknown})





















