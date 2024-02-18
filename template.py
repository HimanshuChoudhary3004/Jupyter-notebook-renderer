import os
from pathlib import Path
import logging

logging.basicConfig(
        level=logging.INFO,
        format="[%(asctime)s : %(levelname)s]: %(message)s"
        )

while True:
    project_name= input("Enter Project Name:")
    if project_name!="":
        break

logging.info(f"Creating project by name :{project_name}")

# list of files:
list_of_files=[
        ".github/workflows/.gitkeep",
        f"src/{project_name}/__init__.py",
        f"test/__init__.py",
        f"test/unit/__init__.py",
        f"test/integration/__init__.py",
        "init_setup.sh",
        "requirements.txt",
        "requirements_dev.txt",
        "setup.py",
        "pyproject.toml",
        "setup.cfg",
        "tox.ini"
        ]

for filepath in list_of_files:
    filepath=Path(filepath)
    filedir,filename = os.path.split(filepath)
    if filedir != "":
        os.makedirs(filedir,exist_ok=True)
        logging.info(f"Creating a directory at: {filedir} and file: {"filename"}")

    if (not os.path.exists(filepath)) or (os.path.getsize==0):
        with open(filepath,"w") as f:
            pass
        logging.info(f"creating a new file :{filename} at : {filepath}")
    else:
        logging.info(f"File already present at : {filepath}")

