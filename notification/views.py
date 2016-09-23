from django.shortcuts import render
from django.http import HttpResponseRedirect, HttpResponse, Http404
from .models import Notification
from .forms import notificationForm
from django.shortcuts import redirect



def current_datetime(request):

    now = datetime.datetime.now()
    html = "<html><body> it is now : %s.</body></html>" % now
    return HttpResponse(html)


def show_notification(request, notification_id):

    n = Notification.objects.get(id=notification_id)
    if n.user == request.user:
        context = {'notification': n}
    else:
        return HttpResponseRedirect('/admin/')

    return render(request, 'notification/notification.html', context)


def delete_notification(request, notification_id):
    n = Notification.objects.get(id=notification_id)
    n.viewed = True
    n.save()
    return HttpResponseRedirect('/admin/')

def popupform(request):

    return render(request, 'notification/popupform.html')


def loggedin(request):
    
    notification = Notification.objects.filter(user=request.user, viewed=False)

    #try:
     #   offset = int(offset)
    # except ValueError:
     #   raise Http404()
    

    #dt = datetime.datetime.now() + datetime.timedelta(hours=offset)

   # now = " In : %s hours(s), it will be : %s" %(offset, dt) 
    # assert False to triger the error page

    context = {'notifications': notification,}

    return render(request, 'notification/loggedin.html', context )

    

def addnote(request):

    if request.method == "POST":

        form = notificationForm(request.POST)
        if form.is_valid():
            notificationss = form.save()
        
            return redirect('/notification/loggedin')
    else:
        form = notificationForm()

    return render(request, 'notification/addnote.html', {'form': form})




   
















