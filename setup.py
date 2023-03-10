from setuptools import setup, find_packages
import codecs
import os

# here = os.path.abspath(os.path.dirname(__file__))

# with codecs.open(os.path.join(here, "README.md"), encoding="utf-8") as fh:
#     long_description = "\n" + fh.read()

VERSION = '0.0.1'
DESCRIPTION = 'Ty Delargy LibLab Test'

# Setting up
setup(
    name="Ty_Delargy-SDK",
    version=VERSION,
    author="Ty Delargy",
    author_email="tjdelargy@gmail.com",
    description=DESCRIPTION,
    packages=find_packages(),
    install_requires=['pytest', 'requests'],
    keywords=['python', 'lord of the rings'],
    classifiers=[
        "Development Status :: 1 - Testing",
        "Intended Audience :: Developers",
        "Programming Language :: Python :: 3",
        "Operating System :: Unix",
        "Operating System :: MacOS :: MacOS X",
        "Operating System :: Microsoft :: Windows",
    ]
)