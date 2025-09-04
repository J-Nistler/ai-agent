from os import path, listdir

def get_files_info(working_directory, directory="."):
    abs_working_dir = path.abspath(working_directory)
    target_dir = path.abspath(path.join(working_directory, directory))
    if not target_dir.startswith(abs_working_dir):
        return f'Error: Cannot list "{directory}" as it is outside the permitted working directory'
    if not path.isdir(target_dir):
        return f'Error: "{directory}" is not a directory'
    try:
        files_info = []
        for filename in listdir(target_dir):
            filepath = path.join(target_dir, filename)
            filesize = 0
            is_dir = path.isdir(filepath)
            filesize = path.getsize(filepath)
            files_info.append(
                f'- {filename}: file_size={filesize} bytes, is_dir={is_dir}'
            )
        return "\n".join(files_info)
    except Exception as e:
        return f"Error listing files: {e}"
