import os
from django.core.exceptions import ValidationError

def unvalidate_file_extension(file):
    ext = os.path.splitext(file.name)[1]  # [0] returns path+filename
    unvalid_extensions = ['.png']
    if ext.lower() in unvalid_extensions:
        raise ValidationError('Unsupported file extension.')