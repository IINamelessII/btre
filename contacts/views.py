from django.shortcuts import redirect, render
from django.contrib import messages
from django.core.mail import EmailMessage
from contacts.models import Contact


def contact(request):
    if request.method == 'POST':
        listing_id = request.POST['listing_id']
        listing = request.POST['listing']
        name = request.POST['name']
        phone = request.POST['phone']
        email = request.POST['email']
        message = request.POST['message']
        user_id = request.POST['user_id']
        realtor_email = request.POST['realtor_email']

        # Check if user has made inquiry already
        if request.user.is_authenticated:
            #user_id = request.user.id
            has_contacted = Contact.objects.filter(listing_id=listing_id, user_id=user_id).exists()
            if has_contacted:
                messages.error(request, 'You have already made an inquiry for this listing.')
                return redirect('/listings/' + listing_id)

        contact = Contact(listing=listing, listing_id=listing_id, name=name,
        email=email, phone=phone, message=message, user_id=user_id)
        contact.save()

        # Send email
        email = EmailMessage(
            'Property Listing Inquiry {} | BT Real Estate'.format(listing),
            'There has been inquiry for {} from {}.\n'.format(listing, name,) + ('He/she leaves message: {}\n'.format(message) if message else '') + 'Ask him/her via {} or {}.'.format(phone, email),
            to=[realtor_email,]
        )
        email.send()


        messages.success(request, 'Your request has been submitted, a realtor \
        will get back to you soon.')
        return redirect('/listings/' + listing_id)