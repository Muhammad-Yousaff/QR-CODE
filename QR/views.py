from django.shortcuts import render
from . froms import QRCodeForm
import qrcode
def generate_qr_code(request):
    if request.method == 'POST':
        form = QRCodeForm(request.POST)
        if form.is_valid():
            restaurant_name = form.cleaned_data['restaurant_name']
            url = form.cleaned_data['url']

           
            qr=qrcode.make(url)
            file.name= res_name.replace(" ",'_') + '_qr.png'
            qr.save(file.name)


    else:
        form = QRCodeForm()
    context = {
        'form': form,
    }
    return render(request, 'generate_qr_code.html', context)
