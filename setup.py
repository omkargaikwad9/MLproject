from setuptools import find_packages,setup
from typing import List

HYPEN_TYPE = '-e .'
def get_requirments(file_path:str)->List[str]:
    '''
    this function will return the list of requirments
    '''
    requirments = []
    with open(file_path) as file_obj:
        requirments = file_obj.readlines()
        requirments = [req.replace("/n","")for req in requirments]
        if HYPEN_TYPE in requirments:
            requirments.remove(HYPEN_TYPE)
    return requirments
        
setup(
name='MLproject',
version='0.0.1',
description='end to end project',
author='omkargaikwad9',
author_email='omigaikwad.og@gmail.com',
packages=find_packages(),
install_requirments  = get_requirments('requirments.txt')
)
    