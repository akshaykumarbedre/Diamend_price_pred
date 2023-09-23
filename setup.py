from setuptools import find_packages,setup
from typing import List

HYPEN_E_DOT="-e ."

def get_req(file_path):
    with open(file_path, 'r') as f:
        read_data=f.readlines()
        requirements=[req.replace("\n","") for req in read_data]
        if HYPEN_E_DOT in requirements:
            requirements.remove(HYPEN_E_DOT)
        return requirements

setup(
    name="scr",
    version='0.0.1',
    author='AkshayKumarBM',
    author_email="akshaykumarbedre.bm@gmail.com",
    install_requires=get_req("requirements.txt"),
    packages=find_packages()
)


#python setup.py install 