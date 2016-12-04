from django.shortcuts import render,redirect,render_to_response,RequestContext,HttpResponse
from django.template.loader import get_template
from django.core.mail import EmailMessage
from django.template import Context
from django.conf import settings
from django.core.mail import send_mail
from .forms import ContactEmailForm,ContactEmailForm_Popup
from django.shortcuts import render
from django.template.loader import get_template
from django.core.mail import EmailMessage
from django.template import Context
from mysite.models import *
from reportlab.pdfgen import canvas
import os
from wsgiref.util import FileWrapper
from django.http import FileResponse, Http404
from django.contrib.auth.decorators import login_required
from mysite.forms import Pop_Up_Form


#@login_required(login_url="/accounts/login/")
def some_view(request):
    # file = open(r'C:/Python27/Scripts/src/documents/djangobook.pdf', "w+b")
    #path = os.path(r'C:/Python27/Scripts/src/documents/djangobook.pdf')
    try:
        return FileResponse(open(r'C:/Python27/Scripts/src/documents/CSS3.pdf', 'rb'), content_type='application/pdf')
    except :
        raise Http404()



def my_fun(request):
    return HttpResponse("hello django")


def Pop_Up_view(request):
    if request.method == 'POST':
        name=request.POST['name']
        print '******************************************',name
        course=request.POST['course']
        Course_Popup_Window.objects.create(
            name=name,
            course=course
        )
        return HttpResponse('')



def Contact_View(request):
    form =ContactEmailForm(request.POST or None)

    if form.is_valid():

        email=form.cleaned_data.get('email')
        name=form.cleaned_data.get('name')
        phone=form.cleaned_data.get('phone')
        course=form.cleaned_data.get('course')
        message=form.cleaned_data.get('message')
        subject='site contact form message'
        from_email=settings.EMAIL_HOST_USER
        to_email=[from_email]
        contact_message='Email: %s\n Name:%s\n Course: %s\n Phone:%s\n Message: %s  ' %(email,name,course,phone,message)
        send_mail(subject,
                  contact_message,
                  from_email,
                  to_email,
                  fail_silently=False)

        return redirect('/contact/')

    context={'form':form}
    return render(request,'Bootup/contact.html',context)


def Contact_View_Popup(request):
    form =ContactEmailForm_Popup(request.POST or None)
    if form.is_valid():
        name=form.cleaned_data.get('name')
        course=form.cleaned_data.get('course')
        contact_message = 'Name:%s\n Course: %s  ' % (name, course)
        from_email = settings.EMAIL_HOST_USER
        to_email = [from_email]
        subject = 'site contact form message'
        send_mail (subject,
                   contact_message,
                   from_email,
                   to_email,
                   fail_silently=False)
    return HttpResponse('')


    # context = {'form': form}
    # return render(request, 'testmail.html', context)

def course_index(request):
    context={}
    return render(request,'Bootup/my_course.html',context)


def myhome(request):
    context={}
    return render(request,'Bootup/home.html',context)


def courses(request):
    context={}
    return render(request,'Bootup/course.html',context)


def aboutus(request):
	context={}
	return render(request,'Bootup/about-us.html',context)

# services page
def services(request):
    return render(request,'services/services1.html',{})


def embeded(request):
    context={}
    return render(request,'courses/embeded.html',context)


# Main page for Telecom

def telecom(request):
    context={}
    return render(request,'courses/telecom.html',context)

# Details for Telecome course content subtabs - read more

def LTEPD(request):
    property = [Ltepd_Course_Schedule.objects.last()]
    context={'property': property}
    return render(request,'courses/Telecome/LTEPD.html',context, 
        context_instance=RequestContext(request))
    


def LTEPT(request):
    property = [Ltept_Course_Schedule.objects.last()]
    context={'property': property}
    return render(request,'courses/Telecome/LTEPT.html',context)


def VOIP_SIP_IMS_PD(request):
    property = [Voip_Sip_Ims_Pd_Course_Schedule.objects.last()]
    context={'property': property}
    return render(request,'courses/Telecome/VOIP_SIP_IMS_PD.html',context)


def VOIP_SIP_IMS_PT(request):
    property = [Voip_Sip_Ims_Pt_Course_Schedule.objects.last()]
    context={'property': property}
    return render(request,'courses/Telecome/VOIP_SIP_IMS_PT.html',context)


#Main Page for Datacom

def datacom(request):
    context={}
    return render(request,'courses/datacom.html',context)

# Details for Datacom courses content subtabs - read more

def l2l3dev(request):
    property= [L2_L3_Pd_Course_Schedule.objects.last()]
    context={'property': property}
    return render(request,'courses/Datacom/L2_L3_Dev.html',context)

def l2l3test(request):
    property = [L2_L3_Pt_Course_Schedule.objects.last()]
    context={'property': property}
    return render(request, 'courses/Datacom/L2_L3_Test.html',context,
        context_instance=RequestContext(request))




# Main page for scripting

def scripting(request):
    context={}
    return render(request,'courses/scripting.html',context)

# Detail for scripting course Content subtabs - read more.

def python(request):
    property = [Python_Course_Schedule.objects.last()]
    context={'property': property}
    return render(request,'courses/scripting/python.html',context, context_instance=RequestContext(request))

def pandas(request):
    context={}
    return render(request,'courses/scripting/pandas.html',context)

def perl(request):
    context={}
    return render(request,'courses/scripting/perl.html',context)

def ttcn3(request):
    context={}
    return render(request,'courses/scripting/ttcn3.html',context)

def flask(request):
    context={}
    return render(request,'courses/scripting/flask.html',context)

def django(request):
    property = [Django_Course_Schedule.objects.last()]
    #property1 = Django_Subject_Details.objects.order_by('topic')
    itemin = {'property': property}
    return render_to_response('courses/scripting/django.html', itemin, context_instance=RequestContext(request))



# main views for cloud

def cloud(request):
    context={}
    return render(request,'courses/cloud.html',context)

#Detiled view for openstack and readmore
def openstack(request):
    property = [Openstack_Course_Schedule.objects.last()]
    context={'property': property}
    return render(request,'courses/Cloud/Openstack.html',context)

#Detailed view for Amazon Web Services and readmore
def aws(request):
    property = [Aws_Course_Schedule.objects.last()]
    context={'property': property}
    return render(request,'courses/Cloud/AWS.html',context)

# main Page for Embeded

def embeded(request):
    context={}
    return render(request,'courses/embeded.html',context)

# Detailed page for Internet of Things:
def iot(request):
    property = [Iot_Course_Schedule.objects.last()]
    context={'property': property}
    return render(request,'courses/Embeded/IOT.html',context)



# main Page for Devops

def devops(request):
    context={}
    return render(request,'courses/devops.html',context)

# Detailed page for Ansibel:
def ansibel(request):
    property = [Ansibel_Course_Schedule.objects.last()]
    context={'property': property}
    return render(request,'courses/Devops/Ansibel.html',context)

# Detailed page for Dockers:
def dockers(request):
    property = [Dockers_Course_Schedule.objects.last()]
    context={'property': property}
    return render(request,'courses/Devops/Dockers.html',context)

# Detailed page for Chef:
def chef(request):
    property = [Chef_Course_Schedule.objects.last()]
    context={'property': property}
    return render(request,'courses/Devops/Chef.html',context)

# Detailed page for Chef:
def nagios(request):
    property = [Nagios_Course_Schedule.objects.last()]
    context={'property': property}
    return render(request,'courses/Devops/Nagios.html',context)

# Detailed page for GIT:
def git(request):
    property = [Git_Course_Schedule.objects.last()]
    context={'property': property}
    return render(request,'courses/Devops/Git.html',context)

# Detailed page for Jenkins:
def jenkins(request):
    property = [Jenkins_Course_Schedule.objects.last()]
    context={'property': property}
    return render(request,'courses/Devops/Jenkins.html',context)









