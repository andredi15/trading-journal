from django.shortcuts import render, redirect
from django.http import HttpResponseRedirect
from django.views import View
from .forms import EntryForm
from .models import Entry

# Create your views here.

class EntryView(View):
  def get(self, request):
    entries = Entry.objects.all().order_by("entered_date")
    form = EntryForm()
    return render(request, "entries.html", {"form":form, "entries":entries})
  
  def post(self, request):
    form = EntryForm(request.POST)
    if form.is_valid():
      form.save() 
      return redirect("/")
    else:
      return render(request, "entries.html", {"form":form})
    
class SingleEntryView(View):
  def get(self, request, id):
    entry = Entry.objects.get(id=id)
    context={
      "entered_date":entry.entered_date,
      "ticker":entry.ticker,
      "strategy":entry.strategy,
      "result":entry.result,
      "comments":entry.comments,
      "image":entry.image
    }
    return render(request, "single-entry.html", context)

# def single_entry(request, id): Old method, not using class-based views.
    