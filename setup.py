from setuptools import setup, find_packages
from os.path import dirname, join
import project_x


def readfile(filename):
    with open(join(dirname(__file__), filename), 'r') as f:
        return f.read()

setup(
    name="py_prod",
    description="stuff for production",
    install_requires=[
        'more_itertools',
    ],
    keywords="notsure",
    long_description=readfile("README.md"),
    url="http://qwa.dk",
    version=ocid.__version__,
    packages=find_packages(),
    maintainer="Jonas Brunsgaard",
    maintainer_email="jonas.brunsgaard@gmail.com",
)
