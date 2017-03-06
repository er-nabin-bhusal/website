from django.shortcuts import render
from .models import MatchDate,Photos,Viewers
import datetime

# Create your views here.

def home_view(request):
	# for counting number of views of website only 
	obj1 = Viewers.objects.all()
	if obj1.count() > 0:
		first1 = obj1.first()
		first1.increase()
		
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


def gallary_view(request):
	template = 'kanchanpur/gallary.html'
	return render(request,template,{})

def about_view(request):
	template = 'kanchanpur/about.html'
	return render(request,template,{})

def sponsor_view(request):
	template = 'kanchanpur/sponsor.html'
	return render(request,template,{})




















