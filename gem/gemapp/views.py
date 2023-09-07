from django.contrib import messages, auth
from django.contrib.auth import authenticate
from gemapp.models import Enquiry, Admission
from django.shortcuts import render, redirect


# Create your views here.

def index(request):
    return render(request, 'enquiry.html')


def login(request):
    if request.user.is_authenticated:
        if request.user.Username == 'gtec' and request.user.Password == 'gtecperumbavoor':
            return redirect("enquiry.html")
        else:
           messages.info(request, 'invaid credentials')
           return redirect('login/')
    else:
        messages.info(request, 'Invalid user!!!')

     # return render(request, 'login.html')
    # if request.method == 'POST':
    #     username = request.POST['uname']
    #     password = request.POST['password']
    #     user = auth.authenticate(username=username, password=password)
    #
    #     if user is not None:
    #         auth.login(request, user)
    #         return redirect('admission/')
    #         # return render(request, 'enquiry.html')
    #     else:
    #         messages.info(request, 'invaid credentials')
    #         return redirect('login/')
            # return render(request, 'login.html')

def enquiry(request):
    enquiry1 = Enquiry.objects.all()
    if request.method == "POST":
        name = request.POST.get('name', '')
        address = request.POST.get('address', '')
        contact = request.POST.get('contact', '')
        course = request.POST.get('course', '')
        enquiry = Enquiry(name=name, address=address, contact=contact, course=course)
        enquiry.save()
    return render(request, "enquiry.html", {'Enquiry1': enquiry1})


def admission(request):
    reg1 = Admission.objects.all()
    if request.method == "POST":
        gemid = request.POST.get('gem_id', '')
        stud_name = request.POST.get('student_name', '')
        parent_name = request.POST.get('student_parent', '')
        parent_contact = request.POST.get('parent_contact', '')
        stud_address = request.POST.get('student_address', '')
        stud_contact = request.POST.get('student_contact', '')
        qualification = request.POST.get('student_qualification', '')
        dob = request.POST.get('student_dob', '')
        gender = request.POST.get('gender', '')
        course1 = request.POST.get('student_course1', '')
        course2 = request.POST.get('student_course2', '')
        course3 = request.POST.get('student_course3', '')
        course_duration = request.POST.get('course_duration', '')
        scheme = request.POST.get('student_scheme', '')
        fee = request.POST.get('student_fee', '')
        joining_date = request.POST.get('join_date', '')
        exam_date = request.POST.get('exam_date', '')
        certificate_status = request.POST.get('cert_status', '')
        admission = Admission(gemid=gemid, stud_name=stud_name, parent_name=parent_name,
                              parent_contact=parent_contact, stud_address=stud_address,
                              stud_contact=stud_contact, qualification=qualification, dob=dob,
                              gender=gender, course1=course1, course2=course2, course3=course3,
                              course_duration=course_duration, scheme=scheme, fee=fee, joining_date=joining_date,
                              exam_date=exam_date, certificate_status=certificate_status)
        admission.save()
    return render(request, "admission.html", {'reg1': reg1})
