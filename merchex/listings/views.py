from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404
from django.core.mail import send_mail

from listings.models import Band, Listing, ContactUsDatas
from listings.forms import ContactUsForm, BandForm, ListingForm
from django.shortcuts import redirect 



def band_list(request):
    bands = Band.objects.all()
    return render(request, 'listings/band_list.html', {'bands': bands})


def band_detail(request, band_id):
    band = get_object_or_404(Band, pk=band_id)
    return render(request, 'listings/band_detail.html', {'band': band})


def band_update(request, band_id):
    band = get_object_or_404(Band, pk=band_id)
    if request.method == 'POST':
        form = BandForm(request.POST, instance=band)
        if form.is_valid():
            # mettre à jour le groupe existant dans la base de données
            form.save()
            # rediriger vers la page détaillée du groupe que nous venons de mettre à jour
            return redirect('band-detail', band.id)
    else:
        form = BandForm(instance=band)

    return render(request, 'listings/band_update.html', {'form': form})


def band_create(request):
    if request.method == 'POST':
        form = BandForm(request.POST)
        if form.is_valid():
            # créer une nouvelle « Band » et la sauvegarder dans la db
            band = form.save()
            # redirige vers la page de détail du groupe que nous venons de créer
            # nous pouvons fournir les arguments du motif url comme arguments à la fonction de redirection
            return redirect('band-detail', band.id)

    else:
        form = BandForm()

    return render(request,
            'listings/band_create.html',
            {'form': form})



def about(request):
    return render(request, 'listings/about.html')


def listing_list(request):
    titles = Listing.objects.all()
    return render(request, 'listings/listing_list.html', {'titles': titles})


def listing_detail(request, listing_id):
    listing = get_object_or_404(Listing, pk=listing_id)
    return render(request, 'listings/listing_detail.html', {'listing': listing})


def listing_create(request):
    if request.method == 'POST':
        form = ListingForm(request.POST)
        if form.is_valid():
            # créer un nouveau « Listing » et la sauvegarder dans la db
            listing = form.save()
            # redirige vers la page de détail du groupe que nous venons de créer
            # nous pouvons fournir les arguments du motif url comme arguments à la fonction de redirection
            return redirect('listing-detail', listing.id)

    else:
        form = ListingForm()

    return render(request,
            'listings/listing_create.html',
            {'form': form})






def contact(request):
    if request.method == 'POST':
        form = ContactUsForm(request.POST)
        if form.is_valid():
            datas = ContactUsDatas.objects.create(name=f'Message from {form.cleaned_data["name"] or "anonyme"} via MerchEx Contact Us form',
                                                    email=form.cleaned_data['email'],
                                                    message=form.cleaned_data['message'],)
            send_mail(
                    subject=datas.name,
                    message=datas.message,
                    from_email=datas.email,
                    recipient_list=['admin@merchex.xyz'],
                )
            return redirect('email-sent', contactus_id=datas.id)
        else:
            dummy = 0
        # si le formulaire n'est pas valide, nous laissons l'exécution continuer jusqu'au return
        # ci-dessous et afficher à nouveau le formulaire (avec des erreurs).

    else:
        # ceci doit être une requête GET, donc créer un formulaire vide
        form = ContactUsForm()
    
    return render(request, 'listings/contact.html', {'form': form})


def email_sent(request, contactus_id):
    contactusdatas = get_object_or_404(ContactUsDatas, pk=contactus_id)
    return render(request, 'listings/email_sent.html', {'contactusdatas': contactusdatas})