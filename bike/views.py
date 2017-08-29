from django.shortcuts import render
from bike.forms import  ImageForm
from bike.FileUtils import handle_uploaded_file
def index(request):
    return render(request,'bike/index.html')

def image(request):
    image_form = ImageForm()
    return render(request,'bike/image.html',{'imageForm':image_form})

def imageSubmit(request):
    if request.method =='POST':
        form = ImageForm(request.POST, request.FILES)
        if form.is_valid():
            fileInfo =handle_uploaded_file(request.FILES['file'])
            new_image = form.save(commit=False)
            new_image.fileName = fileInfo.name
            new_image.size = fileInfo.size
            new_image.path = fileInfo.path
            new_image.type = fileInfo.type
            new_image.save()
    return  render(request,'bike/imageSubmit.html',{'msg':'success'})
# f2c0ebf2525fac21f6e40f8793a38592dae2eb8e