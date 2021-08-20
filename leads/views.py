from django.shortcuts import render, redirect, reverse
from django.core.mail import send_mail
from django.contrib.auth.forms import UserCreationForm
from django.http import HttpResponse
from django.views import generic
from .models import Lead, Agent
from .forms import LeadForm, LeadModelForm, CustomUserCreationForm, AssignAgentForm
from django.views.generic import (TemplateView, ListView, 
        DetailView, CreateView, UpdateView, DeleteView)
from django.contrib.auth.mixins import LoginRequiredMixin
from agents.mixins import OrganisorAndLoginRequiedMixin
# Create your views here.
# Templates, such as TemplateView, are used to reduce boilerplate code

# Remember CRUD
# Create, Read, Update, Delete + List


class SignupView(generic.CreateView):
    template_name = 'registration/signup.html'
    form_class = CustomUserCreationForm

    def get_success_url(self):
        return reverse("login")


class LandingPageView(TemplateView):
    template_name = "landing.html"

"""
def landing_page(request):
    return render(request, "landing.html")
"""
class LeadListView(OrganisorAndLoginRequiedMixin, generic.ListView):
    template_name = "leads/lead_list.html"
    context_object_name = "leads"

    def get_queryset(self):
        user = self.request.user

        # initial queryset of leads for the organisation
        if user.is_organiser:
            queryset = Lead.objects.filter(
                organisation=user.userprofile,
                agent__isnull=False
            )
        else:
            queryset = Lead.objects.filter(
                organisation=user.agent.organisation,
                agent__isnull=False
            )
            # filter for the agent that's logged in
            queryset = queryset.filter(agent__user=user)

        return queryset

    def get_context_data(self, **kwargs):
        context = super(LeadListView, self).get_context_data(**kwargs)
        user = self.request.user
        if user.is_organiser:
            queryset = Lead.objects.filter(
                organisation=user.userprofile,
                agent__isnull=True
            )
            context.update({
                "unassigned_leads": queryset
            })
        return context


"""
def lead_list(request):
    leads = Lead.objects.all()
    context = {
        "leads": leads
    }
    return render(request, 'leads/lead_list.html', context)
"""

class LeadDetailView(OrganisorAndLoginRequiedMixin, generic.DetailView):
    template_name="leads/lead_detail.html"
    queryset = Lead.objects.all()
    # Below, DetailView automatically grabs the "lead" object via the Primary Key 
    context_object_name = "lead"

"""
def lead_detail(request, pk):
    lead = Lead.objects.get(id=pk)
    context = {
        "lead": lead
    }
    return render(request, "leads/lead_detail.html", context)
"""

class LeadCreateView(OrganisorAndLoginRequiedMixin, generic.CreateView):
    template_name="leads/lead_create.html"
    form_class = LeadModelForm

    def get_success_url(self):
        return reverse("leads:lead-list")

    # overriding original form_valid function to send an email prior to returning the form 
    def form_valid(self, form):
        #TODO send email
        # expect [Errno 61]
        send_mail(
            subject="A lead has been created",
            message="Go to the site to see the new lead",
            from_email="test@test.com",
            recipient_list=["test2@test.com"]

        )
        return super(LeadCreateView, self).form_valid(form)

"""
def lead_create(request):

    form = LeadModelForm()

    if request.method == "POST":
        form = LeadModelForm(request.POST)
        if form.is_valid():
            # by specifying form, .save does al the work form does without
            # the legwork
            form.save()

            return redirect("/leads")

    context = {
        "form": form
    }
    return render(request, "leads/lead_create.html", context)
"""

# django generic template UpdateView needs a queryset
# filters model similiarly to the DetailView
class LeadUpdateView(LoginRequiredMixin, generic.UpdateView):
    template_name = "leads/lead_update.html"
    form_class = LeadModelForm

    def get_queryset(self):
        user = self.request.user
        # initial queryset of leads for the organisation
        return Lead.objects.filter(organisation=user.agent.organisation)

    def get_success_url(self):
        return reverse("leads:lead-list")

"""
# pass only an instance from LeadModelForm, as only one piece of data 
def lead_update(request, pk):
    lead = Lead.objects.get(id=pk)
    form = LeadModelForm(instance=lead)

    if request.method == "POST":
        form = LeadModelForm(request.POST, instance=lead)
        if form.is_valid():
            form.save()
            return redirect("/leads")
            
    context = {
        "form": form,
        "lead": lead
    }
    return render(request, "leads/lead_update.html", context)
"""

class LeadDeleteView(LoginRequiredMixin, generic.DeleteView):
    template_name = "leads/lead_delete.html"
    queryset = Lead.objects.all()

    def get_queryset(self):
        user = self.request.user
        # initial queryset of leads for the organisation
        return Lead.objects.filter(organisation=user.agent.organisation)

    def get_success_url(self):
        return reverse("leads:lead-list")

class AssignAgentView(OrganisorAndLoginRequiedMixin, generic.FormView):
    template_name = "leads/assign_agent.html"
    form_class = AssignAgentForm

    def get_form_kwargs(self):
        return {
            "request": self.request
        }

    def get_success_url(self):
        return reverse("leads:lead-list")

"""
def lead_delete(request, pk):
    lead = Lead.objects.get(id=pk)
    lead.delete()
    return redirect("/leads")
"""

"""
lead_update with standard forms, NOT ModelForm

def lead_update(request, pk):
    lead = Lead.objects.get(id=pk)
    form = LeadForm()

    if request.method == "POST":
        form = LeadForm(request.POST)
        if form.is_valid():
            first_name = form.cleaned_data['first_name']
            last_name = form.cleaned_data['last_name']
            age = form.cleaned_data['age']
            agent = Agent.objects.first()

            lead.first_name=first_name
            lead.last_name=last_name
            lead.age=age
            lead.agent=agent
            lead.save()

            return redirect("/leads")
            
    context = {
        "form": form,
        "lead": lead
    }
    return render(request, "leads/lead_update.html", context)
"""


"""
lead_create using Django.form.Form, NOT ModelForm

def lead_create(request):

    form = LeadForm()

    if request.method == "POST":
        form = LeadForm(request.POST)
        if form.is_valid():
            first_name = form.cleaned_data['first_name']
            last_name = form.cleaned_data['last_name']
            age = form.cleaned_data['age']
            agent = Agent.objects.first()

            Lead.objects.create(
                first_name=first_name,
                last_name=last_name,
                age=age,
                agent=agent
            )

            return redirect("/leads")

    context = {
        "form": form
    }
    return render(request, "leads/lead_create.html", context)"""