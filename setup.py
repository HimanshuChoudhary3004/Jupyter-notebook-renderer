import setuptools

with open("README.md","r","utf-8") as f:
    long_description=f.read()

__version__="0.0.0"
Repo_name="Jupyter-Notebook-renderer"
author_name="HimanshuChoudhar3004"
author_email="hchoudhary525@gmail.com"
src_repo="Jupyter-Notebook-renderer"


setuptools.setup(
    name=src_repo,
    version=__version__,
    author=author_name,
    author_email=author_email,
    description="A small python package",
    long_description=long_description,
    long_description_content="text/markdown",
    url=f"https://github.com/{author_name}/{Repo_name}"
    project_urls={
        "Bug Tracker":f"https://github.com/{author_name}/{Repo_name}/issues",
    },
    package_dir={"":"src"},
    packages=setuptools.find_packages(where="src")

)

          