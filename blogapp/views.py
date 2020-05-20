from django.shortcuts import render

# Create your views here.
from blogapp.models import blogs ,uploadForm
#from blogapp.forms import blogForm


from  django.contrib.auth.decorators import login_required
def home(request):
    return render(request,'blogapp/home.html')
def welcome(request):
    return render(request,'blogapp/welcome.html')

@login_required
def viewallblogs(request):
    blogslist=blogs.objects.all()
    mydict={'blogslist':blogslist}
    return render(request,'blogapp/viewallblogs.html',context=mydict)

@login_required
def uploadForm(request):
    uploadform=uploadForm();
    #mydict={'blogform':blogform}
    if request.method=='POST':
        #DB insert code goes here
        data=uploadForm.save(commit=True)
        data.authodr=request.user
        data.save()
        mydict.update({'msg':'blog post  Successfully'})
    return render(request,'blogapp/postblog.html',context=mydict)

def SignUpPage(request):
    signupform=SignUpForm()
    mydict={'signupform':signupform}
    if request.method=='POST':
        #DB insert code goes here
        signupform=SignUpForm(request.POST);
        user=signupform.save();#insert query
        user.set_password(user.password)
        user.save()# this object save finally
        mydict.update({'msg':'Registered Successfully'})
    return render(request,'blogapp/signup.html',context=mydict)
