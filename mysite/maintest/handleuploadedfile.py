
def handle_uploaded_file(f):
    with open('./uploads/CAR_SAMPLE.CSV', 'wb+') as destination:
        for chunk in f.chunks():
            destination.write(chunk)