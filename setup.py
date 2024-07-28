from setuptools import find_packages, setup
from typing import List

HYPEN_E_DOT = '-e.'
def get_requirement(file_path:str)->List[str]:
    '''
    setup for the list of requirement
    '''
    with open(file_path) as file_obj:
        requirements=file_obj.readlines()
        [req.replace("\n"," ") for req in requirements]

        if HYPEN_E_DOT in requirements:
            requirements.remove(HYPEN_E_DOT)
    return requirements
        
setup(
    name='mlproject',
    version = '0.0.1',
    author = 'pravamaya',
    author_email = 'dpravamaya@gmail.com',
    packages = find_packages(),
    install_requires = get_requirement('requiremnt.txt')
)