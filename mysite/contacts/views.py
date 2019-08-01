# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from contacts.models import Address
from django.http import HttpResponseRedirect, HttpResponse
from contacts.forms import AddressForm #AddressPickerForm
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.contrib.auth.decorators import login_required


from contacts.tasks import call
# Create your views here.

def create(request):
    form = AddressForm()
    if request.method == 'POST':
        form = AddressForm(request.POST)
        if form.is_valid():
            profile = form.save(commit=False)
            profile.user = request.user
            profile.save()
            t = "You have succesfully added your contact details" 
            return HttpResponseRedirect('/contact')
    return render(request, 'address.html', {'form': form})  

@login_required
def home(request):
    #obj = Address.objects.all()
    username = request.user.username
    obj = request.user.address_set.all()
    page = request.GET.get('page', 1)
    paginator = Paginator(obj, 10) 
    #form = AddressPickerForm()

    try:
        contacts = paginator.page(page)
    except PageNotAnInteger:
        contacts = paginator.page(1)
    except EmptyPage:
        contacts = paginator.page(paginator.num_pages)

    return render(request, 'index.html', { 'contacts': contacts, 'user':username })
    
def delete_contact(request, id):
    obj=Address.objects.get(id=id)
    obj.delete()
    return HttpResponseRedirect('/contact/')
    context={
    'username': Address.objects.get(id=id).name,
    'address': Address.objects.get(id=id).address,
    'email': Address.objects.get(id=id).email_id,
    'phone_number': Address.objects.get(id=id).phone_number, 'addr_id': obj}     
    return render(request, 'update.html', context)

def update_contact(request,id):
    obj= Address.objects.get(id = id)
    form = AddressForm(instance=obj)
    print(form.instance.id)
    if request.method == 'POST':
        form = AddressForm(request.POST, instance=obj)
        if form.is_valid():
            form.user = request.user
            print(form)
            form.save()
            return HttpResponseRedirect('/contact/')
        else:
            print(form.errors)
    context={'form':form}     
    return render(request, 'update.html', context)
    
def update_page(request, id):
    if request.method == 'POST':
        form = AddressForm(request.POST)
        if form.is_valid():
            post = form.save()
            saveLogs(request,"You updated your contact address")
            return HttpResponseRedirect('/contact')
        else:
            print(form.errors)


def main_view(request):
    queue = []
    x = request.POST.getlist('checks[]')
    for i in x:
        status=call(i)
        queue.append(status)
    #print(x)


    return render(request, 'main.html', {'data': zip(x, queue)})

# def home(request):
#     qs = Address.objects.all()
#     if request.method=='POST':
#         form = TargetMembers(qs, request.POST)
#         if form.is_valid():
#             profile = form.save(commit=False)
#             profile.user = request.user
#             profile.save()
#             form.save_m2m() # needed since using commit=False
#         else:
#             form = TargetMembers()

#     #return render_to_response(template_name, {"profile_form": form}, context_instance=RequestContext(request))
#     return render(request, 'index.html', { 'contacts': form })


