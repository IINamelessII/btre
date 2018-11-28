from django.shortcuts import get_object_or_404, render
from django.core.paginator import EmptyPage, Paginator, PageNotAnInteger
from listings.choices import price_choices, bedroom_choices, state_choices
from listings.models import Listing


def index(request):
    listings = Listing.objects.filter(is_published=True).order_by('-list_date')
    paginator = Paginator(listings, 6)
    page = request.GET.get('page')
    paged_listings = paginator.get_page(page)
    context = {
        'listings': paged_listings
    }
    return render(request, 'listings/listings.html', context)


def listing(request, listing_id):
    listing = get_object_or_404(Listing, pk=listing_id)
    context = {
        'listing': listing
    }
    return render(request, 'listings/listing.html', context)


def search(request):
    context = {
        'state_choices': state_choices,
        'bedroom_choices': bedroom_choices,
        'price_choices': price_choices
    }
    return render(request, 'listings/search.html', context)