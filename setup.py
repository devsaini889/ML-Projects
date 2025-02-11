from setuptools import find_packages,setup
from typing import List

Hyphen_e_dot = '-e .'

def get_requirements(file_path:str)-> List[str]:
    '''
    This Function returns the list of requirements
    '''
    requirements=[]
    with open(file_path) as file_obj:
        requirements = file_obj.readline()
        requirements = [req.replace("\n","") for req in requirements]

        if Hyphen_e_dot in requirements:
            requirements.remove(Hyphen_e_dot)

setup(
    name='ML Project',
    version='0.0.1',
    author='Dev',
    author_email='ds0752607@gmail.com',
    packages=find_packages(),
    install_requires= get_requirements('requirements.txt')


)