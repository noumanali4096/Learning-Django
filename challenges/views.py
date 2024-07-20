from django.shortcuts import render
from django.http import HttpResponse, HttpResponseNotFound, HttpResponseRedirect
from django.urls import reverse
# Create your views here.

monthly_challenges = {
  "january": "January challenge accepted",
  "february": "February challenge accepted",
  "march": "March challenge accepted",
  "april": "April challenge accepted",
  "may": "May challenge accepted",
  "june": "June challenge accepted",
  "july": "July challenge accepted",
  "august": "August challenge accepted",
  "september": "September challenge accepted",
  "october": "October challenge accepted",
  "november": "November challenge accepted",
  "december": "December challenge accepted",
}

# def index(request):
#   return HttpResponse("January Challenges!")

# def february_challenges(request):
#   return HttpResponse("February Challenges!")


# def march(request):
#   return HttpResponse("Learn React.js daily for atleast 30 minuts")

def monthly_challenge_by_number(request, month):
  months = list(monthly_challenges.keys())


  if month > len(months):
    return HttpResponseNotFound("Invalid month")
  redirect_month = months[month-1]
  redirect_path = reverse("month_challenge", args=[redirect_month])
  # return HttpResponseRedirect("/challenge/" + redirect_month)
  return HttpResponseRedirect(redirect_path)

# def monthly_challenge(request, month):
#   challenge_text = None
#   if month == "january":
#     challenge_text = "Walk and Run for 45 mints daily!"
#   elif month == "february":
#     challenge_text = "Eat food that contains max protein and less carbs"
#   elif month == "march":
#     challenge_text = "Learn django daily for 30 mints"
#   else:
#     return HttpResponseNotFound("This month is not supported")
#   return HttpResponse(challenge_text)


def monthly_challenge(request, month):
  try:
    challenge_text = monthly_challenges[month]
    return HttpResponse(challenge_text)
  except:
    return HttpResponseNotFound("This month is not supported")
  
