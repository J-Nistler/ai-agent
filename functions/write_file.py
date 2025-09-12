from os import path, makedirs

def write_file(working_directory, file_path, content):
    abs_working_dir = path.abspath(working_directory)
    abs_file_path = path.abspath(path.join(working_directory, file_path))

    if not abs_file_path.startswith(abs_working_dir):
        return f'Error: Cannot execute "{file_path}" as it is outside the permitted working directory'
    
    parent_dir = path.dirname(abs_file_path)

    if not path.isdir(parent_dir):
        try:
            makedirs(parent_dir)
        except Exception as e:
            return f'Error: Could not create parent dirs: {parent_dir} = {e}'
        
    try:
        with open(abs_file_path, "w") as f:
            f.write(content)
            return f'Successfully wrote to "{file_path}" ({len(content)} characters written)'
    except Exception as e:
        return f'Error: Failed to write to file: {file_path}, {e}'
    
