from django.shortcuts import render
from listings.models import Listing
from agent.models import Agent
from listings.choices import price_choices, bedroom_choices, state_choices

# Create your views here.
def index(request):
    listings = Listing.objects.order_by('-list_date').filter(is_published=True)[:3]
    context = {
        'listings': listings,
        'state_choices': state_choices,
        'bedroom_choices': bedroom_choices,
        'price_choices': price_choices
    }
    return render(request, 'pages/index.html', context)

def about(request):
    # Get all agent
    agent = Agent.objects.order_by('-hire_date')

    # Get MVP
    mvp_agent = Agent.objects.all().filter(is_mvp=True)

    context = {
        'agent': agent,
        'mvp_agent': mvp_agent
    }

    return render(request, 'pages/about.html', context)