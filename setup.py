#Purpose:
#  The setup.py file is the heart of any Python project if you plan to distribute,
# install, or treat it like a Python package or module.

# | 🔧 Feature                   | 📘 Description                                                                                                                      |
# | ---------------------------- | ----------------------------------------------------------------------------------------------------------------------------------- |
# | 📦 **Packaging**             | Allows your project to be **converted into a Python package** that can be installed using `pip`.                                    |
# | 🧾 **Metadata Definition**   | Provides important info about your project — name, version, author, email, etc.                                                     |
# | 📂 **Package Discovery**     | Identifies which folders should be included as packages (via `find_packages()`).                                                    |
# | 📥 **Dependency Management** | Lists the external libraries your project depends on (via `install_requires`).                                                      |
# | 🔁 **Editable Installation** | When using `-e .`, you can **install your package in development mode**, so changes in code reflect instantly without reinstalling. |


from setuptools import find_packages, setup
from typing import List

HYPHEN_E_DOT = "-e ."

def get_requirements(file_path: str) -> List[str]:
    """
    This function will return a list of requirements
    from the requirements.txt file.
    """
    requirements = []
    try:
        with open(file_path, "r") as file:
            lines = file.readlines()
            for line in lines:
                requirement = line.strip()
                if requirement and requirement != HYPHEN_E_DOT:
                    requirements.append(requirement)
    except FileNotFoundError:
        print("requirements.txt file not found.")
    return requirements

# Main setup configuration
setup(
    name="network_security",  # Name of your project/package
    version="0.0.1",           # Initial version
    author="Apoorv Sahu",          # Replace with your name
    author_email="apoorvsahu.cse19@chitkarauniversity.edu.in",  # Replace with your email
    packages=find_packages(),  # Automatically finds all packages with __init__.py
    install_requires=get_requirements("requirements.txt"),  # External dependencies
)
