from django.shortcuts import render
from django.http import HttpResponse


# Create your views here.
def university(request):
    context = {
        'atbilde': '',
    }
    if request.method == 'POST':
        student = {}
        for i in request.POST:
            if i == 'csrfmiddlewaretoken':
                continue
            if i != 'full_name' or i != 'csrfmiddlewaretoken':
                student[i] = request.POST[i]
            else:
                student[i] = request.POST[i]
        name_of_lov_rate = 0
        for sekmes in student:
            if sekmes != 'full_name':
                if int(student[sekmes]) < 40:
                    name_of_lov_rate += 1
        if name_of_lov_rate != 0:
            mesage = f'Jūs: <b>{request.POST["full_name"]}</b> nevarat startēt universitāte, jo <b>40</b> punktu ' \
                     f'barjeru nepārsniedz <b>{name_of_lov_rate}</b> priekšmetos!'
            context['atbilde'] = mesage
        else:
            mesage = f'Jūs <b>{request.POST["full_name"]}</b> varat startēt universitāte.'
            context['atbilde'] = mesage
        return HttpResponse(mesage)
    return render(request=request,
                  context=context,
                  template_name='university.html',
                  )
