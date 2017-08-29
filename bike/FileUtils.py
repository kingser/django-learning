import os,time
def handle_uploaded_file(f):
    path = "media/editor" + time.strftime('/%Y/%m/%d/')
    if not os.path.exists(path):
        os.makedirs(path)
    file_name = path + f.name
    destination = open(file_name, 'wb+')
    for chunk in f.chunks():
        destination.write(chunk)
    destination.close()
    f.path = file_name.lower()
    f.type = f.name[f.name.rfind('.')+1:].lower()
    return f