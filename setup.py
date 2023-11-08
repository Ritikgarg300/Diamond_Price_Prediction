from setuptools import setup,find_packages
from typing import List
 
def get_requirements(file_path:str)->List[str]:
    requirement=[]
    with open(file_path) as file_obj:
        requirement=file_obj.readlines()
        requirement=[req.replace("\n", "") for req in requirement]
        return requirement
 
setup(
    name="DiamondPrediction",
    version='0.0.1',
    author='Ritik',
    author_email='ritik@gmail.com',
    install_requires=get_requirements('requirements.txt'),
    packages=find_packages()
)