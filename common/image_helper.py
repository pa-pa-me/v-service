import tempfile
import base64

__all__ = ['save_base64_image_to_tmp']

def save_base64_image_to_tmp(base64_encoded_string):
    flag = 'data:image/jpeg;base64,'

    if base64_encoded_string.startswith(flag):
        base64_encoded_string = base64_encoded_string.split(flag)[1]

    with tempfile.NamedTemporaryFile(dir='/tmp', delete=False) as temp_image_file:
        temp_file_name = temp_image_file.name
        with open(temp_file_name, 'wb') as temp_wb:
            temp_wb.write(base64.decodestring(base64_encoded_string))

    return temp_file_name
