import os
import subprocess

def run_python_file(working_directory, file_path, args=None):
    abs_work_dir = os.path.abspath(working_directory)
    abs_file_path = os.path.abspath(os.path.join(abs_work_dir, file_path))
    if not abs_file_path.startswith(abs_work_dir):
        return f'Error: Cannot execute "{file_path}" as it is outside the permitted working directory'
    elif not os.path.exists(abs_file_path):
        return f'Error: File "{file_path}" not found.'
    elif not file_path.endswith(".py"):
        return f'Error: "{file_path}" is not a Python file.'
    else:
        try:
            commands = ["python", abs_file_path]
            if args:
                commands.extend(args)
            process = subprocess.run(commands, text=True,  capture_output=True, timeout=30)
            output = []
            if process.stdout:
                output.append(f"STDOUT: \n\t{process.stdout}")
            if process.stderr:
                output.append(f"STDERR: \n\t{process.stderr}")
            if process.returncode != 0:
                output.append(f"Process exitedd with code {process.returncode}")
            
            return "\n".join(output) if output else "No output produced"

        except Exception as e:
            return f"Error: executing Python file: {e}"