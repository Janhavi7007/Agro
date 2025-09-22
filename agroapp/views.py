from django.http import QueryDict
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.apps import apps
from django.conf import settings

from .forms import SignUpForm
from django.shortcuts import render

def home(request):
     return render(request, 'home.html' )

def about(request):
    return render(request, 'about.html') 

def contact(request):
    return render(request, 'contact.html') 






def signup_view(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')
    else:
        form = SignUpForm()
    return render(request, 'signup.html', {'form': form})

from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from .forms import LoginForm

def login_view(request):
    form = LoginForm(request, data=request.POST or None)

    if request.method == 'POST':
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            return redirect('user_dashboard')  # Or your user_dashboard/homepage

    return render(request, 'login.html', {'form': form})

@login_required
def  user_dashboard(request):
    return render(request, 'user_dashboard.html')

def logout_view(request):
    logout(request)
    return redirect('login')

from django.shortcuts import render
from django.contrib.auth.decorators import login_required


from django.shortcuts import render
from .models import GovernmentScheme

def schemes(request):
    return render(request, 'schemes.html', {'schemes': schemes, 'query': QueryDict})


@login_required
def scheduling(request):
    return render(request, 'scheduling.html')

@login_required
def organic(request):
    return render(request, 'organic.html')

@login_required
def disease(request):
    return render(request, 'disease.html')

from django.shortcuts import render
import os

from django.conf import settings

@login_required
def weather(request):
    context = {
        'api_key': settings.WEATHER_API_KEY  # should be 74bd...
    }
    return render(request, 'weather.html', context)


CustomUser = apps.get_model(settings.AUTH_USER_MODEL)

def is_admin(user):
    return user.is_superuser

from django.http import JsonResponse
from .models import GovernmentScheme

def get_state_schemes(request, state):
    schemes = GovernmentScheme.objects.filter(state=state)
    schemes_data = [
        {
            'title': scheme.title,
            'description': scheme.description,
            'apply_link': scheme.apply_link
        }
        for scheme in schemes
    ]
    return JsonResponse(schemes_data, safe=False)


import requests
from django.shortcuts import render

def agriculture_news(request):
    api_key = 'your-API-Key'
    url = f'https://newsapi.org/v2/everything?q=agriculture+india&sortBy=publishedAt&language=en&apiKey={api_key}'

    response = requests.get(url)
    data = response.json()
    
    print("DEBUG: API Response Data >>>", data)

    articles = data.get('articles', [])

    return render(request, 'agriculture_news.html', {'articles': articles})

from django.shortcuts import render
from django.http import JsonResponse
import requests

def marketplace_view(request):
    return render(request, 'marketplace.html')

def get_nearby_markets(request):
    lat = request.GET.get('lat')
    lon = request.GET.get('lon')

    PLACES_API_KEY = 'your api key'
    DISTANCE_API_KEY = 'your api key'

    try:
        # Fetch nearby places (supermarkets) from Google Places API
        places_url = f"https://maps.googleapis.com/maps/api/place/nearbysearch/json?location={lat},{lon}&radius=5000&type=supermarket&key={PLACES_API_KEY}"
        places_res = requests.get(places_url)
        places_res.raise_for_status()  # Handle any HTTP errors
        places_data = places_res.json()
        print("DEBUG: Places Data >>>", places_data)

        nearby_markets = []

        for place in places_data.get("results", [])[:15]:  # Limit to 5 results
            name = place["name"]
            dest_lat = place["geometry"]["location"]["lat"]
            dest_lon = place["geometry"]["location"]["lng"]

            # Fetch distance and duration using the Distance Matrix API
            distance_url = f"https://maps.googleapis.com/maps/api/distancematrix/json?origins={lat},{lon}&destinations={dest_lat},{dest_lon}&key={DISTANCE_API_KEY}"
            distance_res = requests.get(distance_url)
            distance_res.raise_for_status()
            distance_data = distance_res.json()
            print("DEBUG: Distance Data >>>", distance_data)

            # Extract distance and duration information
            distance = distance_data['rows'][0]['elements'][0]['distance']['text']
            duration = distance_data['rows'][0]['elements'][0]['duration']['text']

            nearby_markets.append({
                'name': name,
                'distance': distance,
                'duration': duration
            })

        return JsonResponse(nearby_markets, safe=False)

    except requests.exceptions.RequestException as e:
        print(f"Error fetching market data: {e}")
        return JsonResponse({'error': 'Failed to fetch data from APIs'}, status=500)



from django.shortcuts import render, get_object_or_404
from .models import AgroBusiness

def agro_business_list(request):
    agro_businesses = AgroBusiness.objects.all()  # All Agro Business Entries
    return render(request, 'agro_business_list.html', {'agro_businesses': agro_businesses})
from django.http import JsonResponse, Http404
from .models import AgroBusiness

def agro_business_detail(request, id):
    try:
        agro = AgroBusiness.objects.get(pk=id)
        data = {
            'title': agro.title,
            'description': agro.description,
            'cost_to_implement': agro.cost_to_implement,
            'profit': agro.profit,
            'loss': agro.loss,
            'benefits': agro.benefits,
            'side_business': agro.side_business,
        }
        return JsonResponse(data, json_dumps_params={'ensure_ascii': False})
    except AgroBusiness.DoesNotExist:
        raise Http404("Agro Business not found")



from django.shortcuts import redirect
from .forms import AgroBusinessForm

def agro_business_create(request):
    if request.method == 'POST':
        form = AgroBusinessForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('agro_business_list')
    else:
        form = AgroBusinessForm()
    return render(request, 'agro/agro_business_form.html', {'form': form, 'action': 'Add'})

def agro_business_update(request, pk):
    business = get_object_or_404(AgroBusiness, pk=pk)
    if request.method == 'POST':
        form = AgroBusinessForm(request.POST, request.FILES, instance=business)
        if form.is_valid():
            form.save()
            return redirect('agro_business_detail', pk=pk)
    else:
        form = AgroBusinessForm(instance=business)
    return render(request, 'agro/agro_business_form.html', {'form': form, 'action': 'Update'})

def agro_business_delete(request, pk):
    business = get_object_or_404(AgroBusiness, pk=pk)
    if request.method == 'POST':
        business.delete()
        return redirect('agro_business_list')
    return render(request, 'agro/agro_business_confirm_delete.html', {'business': business})


from django.shortcuts import render
from django.http import JsonResponse
from .models import OrganicFarmingCategory

def get_farming_category(request, category_slug):
    try:
        category = OrganicFarmingCategory.objects.get(slug=category_slug)
        return JsonResponse({
            'title': category.title,
            'description': category.description,
            'image_url': category.image.url if category.image else '',
            'benefits': category.benefits,
        })
    except OrganicFarmingCategory.DoesNotExist:
        return JsonResponse({'error': 'Category not found'}, status=404)

def organic(request):
    categories = OrganicFarmingCategory.objects.all()
    return render(request, 'organic.html', {'categories': categories})


from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.shortcuts import redirect
from .models import CustomUser

@login_required
def update_email(request):
    if request.method == "POST":
        new_email = request.POST.get("new_email")
        request.user.email = new_email
        request.user.save()
        messages.success(request, "Email updated successfully!")
    return redirect('user_dashboard')

@login_required
def update_password(request):
    if request.method == "POST":
        current = request.POST.get("current_password")
        new = request.POST.get("new_password")
        if request.user.check_password(current):
            request.user.set_password(new)
            request.user.save()
            messages.success(request, "Password updated successfully!")
        else:
            messages.error(request, "Current password is incorrect.")
    return redirect('user_dashboard')

@login_required
def update_phone(request):
    if request.method == "POST":
        new_phone = request.POST.get("new_phone")
        request.user.phone_number = new_phone
        request.user.save()
        messages.success(request, "Phone number updated successfully!")
    return redirect('user_dashboard')


from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .forms import FeedbackForm

from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .forms import FeedbackForm

from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from .forms import FeedbackForm

@login_required
def submit_feedback(request):
    if request.method == 'POST':
        form = FeedbackForm(request.POST)
        if form.is_valid():
            feedback = form.save(commit=False)
            feedback.user = request.user  # Link feedback to logged-in user
            feedback.save()  # Save feedback to database
            messages.success(request, "Thank you for your feedback!")
            return redirect('submit_feedback')  # Redirect to the same form or user dashboard
        else:
            print("❌ Form Errors:", form.errors)  # Debug form errors
    else:
        form = FeedbackForm()

    return render(request, 'feedback_form.html', {'form': form})


from django.contrib.auth.decorators import login_required
from .models import Feedback

@login_required
def user_profile(request):
    feedbacks = Feedback.objects.filter(
        user=request.user,
        admin_reply__isnull=False
    ).exclude(admin_reply='').order_by('-submitted_at')
    
    return render(request, 'user_profile.html', {'feedbacks': feedbacks})

    
from django.shortcuts import render, redirect
from django.contrib import messages
from .models import ContactMessage

def contact(request):
    return render(request, 'contact.html')

def submit_contact(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        email = request.POST.get('email')
        subject = request.POST.get('subject')
        message = request.POST.get('message')

        # Save to DB
        ContactMessage.objects.create(
            name=name,
            email=email,
            subject=subject,
            message=message
        )

        messages.success(request, "Thank you for contacting us!")
        return redirect('contact')
    else:
        return redirect('contact')
