from setuptools import find_packages, setup
from typing import List

HYPEN_E_DOT = '-e .'

def get_requirements(file_path: str) -> List[str]:
    """
    This function returns the list of requirements.
    """
    requirements = []
    try:
        with open(file_path, 'r') as file_obj:
            requirements = file_obj.readlines()
            requirements = [req.strip() for req in requirements]

            if HYPEN_E_DOT in requirements:
                requirements.remove(HYPEN_E_DOT)
    except FileNotFoundError:
        print(f"Error: {file_path} not found.")
    
    return requirements

setup(
    name='mlproject',
    version='0.0.1',
    author='IBRAR',
    author_email='ibrar.ali69.ia@gmail.com',
    description='A machine learning project template.',
    packages=find_packages(),
    install_requires=get_requirements('requirements.txt'),

)