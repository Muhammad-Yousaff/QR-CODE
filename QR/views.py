from django.shortcuts import render
from .forms import QRCodeForm
import qrcode
from django.conf import settings
import os

def generate_qr_code(request):
    if request.method == 'POST':
        form = QRCodeForm(request.POST)
        if form.is_valid():
            restaurant_name = form.cleaned_data['restaurant_name']
            url = form.cleaned_data['url']

            qr = qrcode.make(url)
            filename = restaurant_name.replace(" ", '_') + '_qr.png'
            file_path = os.path.join(settings.MEDIA_ROOT, filename)
            
            # Ensure media directory exists
            os.makedirs(settings.MEDIA_ROOT, exist_ok=True)
            
            qr.save(file_path)
            
            context = {
                'form': form,
                'qr_url': settings.MEDIA_URL + filename
            }
            return render(request, 'generate_qr_code.html', context)

    else:
        form = QRCodeForm()
    
    context = {
        'form': form,
    }
    return render(request, 'generate_qr_code.html', context)
