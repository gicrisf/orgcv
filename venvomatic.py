parent_dir=".venvs"
new_dir="cv-venv"
import virtualenv
import os
import subprocess

# Where we want to put our virtual environment
if parent_dir:
    venvs_dir = os.path.join(os.path.expanduser("~"), parent_dir)
else:
    venvs_dir = os.path.join(os.path.expanduser("~"), ".venvs")

# Make the parent directory if it doesn't exists
if not os.path.exists(venvs_dir):
    os.makedirs(venvs_dir)
    print("{} not found; made it.".format(venvs_dir))

# Choose a specific directory to be made
if new_dir:
    cv_venv_dir = os.path.join(venvs_dir, new_dir)
else:
    cv_venv_dir = os.path.join(venvs_dir, "cv-venv")

# Make the parent directory if it doesn't exists
if not os.path.exists(cv_venv_dir):
    os.makedirs(cv_venv_dir)
    print("{} not found; made it.".format(cv_venv_dir))

# Create the new venv
# virtualenv.create_environment(cv_venv_dir) # deprecated
print("creating the new venv...")
subprocess.run(["python", "-m", "venv", cv_venv_dir]) # use venv instead
print("done.")

# Find the new executable
py_binary = os.path.join(cv_venv_dir, "bin")

os.chdir(cv_venv_dir)

# Install requirements
print("installing requirements...")
subprocess.Popen(["./python", "-m", "pip", "install", "-U", "Jinja2", "Babel", "git+https://github.com/jlumpe/pyorg#egg=pyorg", "python-emacs"], cwd=py_binary)
print("done.")
print("now exiting.")
