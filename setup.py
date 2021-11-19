import pathlib
from setuptools import find_packages, setup

HERE = pathlib.Path(__file__).parent

VERSION = '0.0.1' # Versioning
PACKAGE_NAME = 'Warehouse' # Match with Package Name
AUTHOR = 'Juan Pablo Prina' 
AUTHOR_EMAIL = 'jpprina@gmail.com' 
URL = 'https://github.com/jpprina-dev' 

LICENSE = None #Tipo de licencia
DESCRIPTION = 'This is a Library with easy-to-use tools to work when you are working with data. Specially working with images.' # Short Description
LONG_DESCRIPTION = (HERE / "README.md").read_text(encoding='utf-8') # README
LONG_DESC_TYPE = "text/markdown"


# Addintional Packages
INSTALL_REQUIRES = [
    'numpy',
    'matplotlib',
    'opencv-contrib-python'
    ]

setup(
    name=PACKAGE_NAME,
    version=VERSION,
    description=DESCRIPTION,
    long_description=LONG_DESCRIPTION,
    long_description_content_type=LONG_DESC_TYPE,
    author=AUTHOR,
    author_email=AUTHOR_EMAIL,
    url=URL,
    install_requires=INSTALL_REQUIRES,
    license=LICENSE,
    packages=find_packages(),
    include_package_data=True
)