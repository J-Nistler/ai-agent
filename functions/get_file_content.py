from os import path
import config

def get_file_content(working_directory, file_path):

    abs_working_dir = path.abspath(working_directory)
    abs_file_path = path.abspath(path.join(working_directory, file_path))

    if not abs_file_path.startswith(abs_working_dir):
        return f'{file_path} is not in the working dir'
    
    if not path.isfile(abs_file_path):
        return f'{file_path} is not a file'

    file_content_string = ""
    
    try:
        with open (abs_file_path, "r") as f:
            file_content_string = f.read(config.MAX_CHARS)
            if len(file_content_string) >= config.MAX_CHARS:
                    file_content_string += (f'[...File "{file_path}" truncated at 10000 characters]')
            return file_content_string
    except Exception as e:
         return f"Exception reading file: {e}"
