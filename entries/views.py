from django.forms.models import BaseModelForm
from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse, HttpResponseRedirect
from django.views import View
from django.contrib import messages
from django.urls import reverse_lazy
from .forms import EntryForm, CreateUserForm, LoginForm
from .models import Entry
from django.views.generic.edit import DeleteView, FormView
# Authentication models and functions
from django.contrib.auth.views import LoginView, LogoutView
#this is to ensure that even after you have your login setup, a user can't just manually type in the URL
from django.contrib.auth.mixins import LoginRequiredMixin


# Create your views here. 

class EntryView(LoginRequiredMixin, View):
  login_url = 'login'
  def get(self, request):
    logged_in_user = request.user.id
    entries = Entry.objects.filter(trader_id=logged_in_user).order_by("entered_date") #trader"_" id instead of .id is just django syntax
    #entries = Entry.objects.all()
    form = EntryForm()
    return render(request, "entries.html", {"form":form, "entries":entries, "user":logged_in_user})
  
  def post(self, request):
    form = EntryForm(request.POST, request.FILES) #must add request.FILES for uploads
    if form.is_valid():
      form.save()
      messages.success(request, "Entry created!")
      return redirect("/")
    else:
      messages.error(request, "Please correct the errors below.")
      return render(request, "entries.html", {"form":form})

    
def SingleEntryView(request, pk):
    entry = Entry.objects.get(pk=pk)

    if request.method == 'POST':
        # Initialize the form with the existing Entry data
        form = EntryForm(request.POST, request.FILES, instance=entry)
        if form.is_valid():
            # Set the user and save the updated data
            form.instance.user = request.user
            form.save()
            # Redirect to a success page (e.g., 'index')
    else:
        # Initialize the form with the existing Entry data
        form = EntryForm(instance=entry)
    context = {'form': form, 'entry': entry}
    return render(request, "single_entry.html", context)
  
class SingleEntryDeleteView(LoginRequiredMixin, DeleteView): 
  template_name = "single_entry.html"
  model = Entry
  success_url = reverse_lazy("index")
  success_message = "Entry has been deleted."

  def delete(self, request):
    messages.success(self.request, "Successfully deleted.")
    return super().delete()

def register(request):
    form = CreateUserForm()

    if request.method == "POST":
       form = CreateUserForm(request.POST)
       if form.is_valid():
          print("User data created")
          form.instance.user = request.user
          form.save()
          return redirect("/") 
    
    else:
       form = CreateUserForm()

    context = {'registerform':form}
    return render(request, "register.html", context)   
  
# class RegisterFormView(FormView):
#    form = CreateUserForm
#    template_name = "register.html"
#    success_url = "/"

#    def form_valid(self, form):
#       form.save()
#       return super().form_valid(form)

class LoginUserView(LoginView):
   form = LoginForm
   redirect_authenticated_user = True
   template_name = "login.html"
   next_page = "/"
   authentication_form = LoginForm
   context = {'form':form}

   def form_invalid(self, form):
      messages.error(self.request, 'Invalid usename or password')
      return self.render_to_response(self.get_context_data(form=form))

