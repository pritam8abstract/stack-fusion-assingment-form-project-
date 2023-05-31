from django.shortcuts import render, redirect
from django.core.mail import send_mail
from django.conf import settings
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from datetime import datetime, timedelta
from .models import UserForm
from .forms import UserFormForm

def user_form(request):
    if request.method == 'POST':
        form = UserFormForm(request.POST)
        if form.is_valid():
            form.save()
            send_email(form.cleaned_data)
            return redirect('submitted_forms')
    else:
        form = UserFormForm()
    
    return render(request, 'userform/user_form.html', {'form': form})

def submitted_forms(request):
    forms = UserForm.objects.all()
    return render(request, 'userform/submitted_forms.html', {'forms': forms})

@csrf_exempt
def validate_phone_number(request):
    if request.method == 'POST':
        phone_number = request.POST.get('phone_number')
        if validate_phone_number_format(phone_number):
            return JsonResponse({'valid': True})
        else:
            return JsonResponse({'valid': False})

def validate_phone_number_format(phone_number):
    # Implement your phone number validation logic here
    return True  # Return True for now, assuming all phone numbers are valid

def send_email(form_data):
    # Implement email sending logic using Django's send_mail function
    subject = 'User Form Submission'
    message = f"Thank you for submitting the form.\n\nName: {form_data['name']}\nDate of Birth: {form_data['date_of_birth']}\nEmail: {form_data['email']}\nPhone Number: {form_data['phone_number']}"
    from_email = settings.DEFAULT_FROM_EMAIL
    recipient_list = [form_data['email']]
    send_mail(subject, message, from_email, recipient_list, fail_silently=False)
