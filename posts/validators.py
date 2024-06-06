import os
# import magic
from django.core.exceptions import ValidationError

def unvalidate_file_extension(file):
    # unvalid_mime_types = ['application/png']
    # file_mime_type = magic.from_buffer(file.read(1024), mime=True)
    # if file_mime_type in unvalid_mime_types:
    #     raise ValidationError('Unsupported file type.')
    ext = os.path.splitext(file.name)[1]  # [0] returns path+filename
    unvalid_extensions = ['.png']
    if ext.lower() in unvalid_extensions:
        raise ValidationError('Unsupported file extension.')