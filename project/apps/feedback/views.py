
from django.http import JsonResponse
from django.shortcuts import render_to_response

from apps.feedback.models import FeedBack
from apps.feedback.forms import FeedbackForm

from project.exceptions import ProjectException
from project.errorcode import ErrorCode

def feedback(request):
    if request.method == 'GET':
        return render_to_response(
            'test.html',
            {
                'action': request.path,
                'form': FeedbackForm().as_p()
            }
        )


    form = FeedbackForm(request.POST)
    if not form.is_valid():
        raise ProjectException(ErrorCode.REQUEST_ERROR)

    email = form.cleaned_data['email']
    country = form.cleaned_data['country']
    content = form.cleaned_data['content']

    udid = request.session['udid']
    phone = request.session['phone']

    FeedBack.objects.create(
        udid=udid,
        phone=phone,
        email=email,
        country=country,
        content=content
    )

    return JsonResponse({'ret': 0})
