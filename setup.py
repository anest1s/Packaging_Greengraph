from setuptools import setup, find_packages

'''
install this code with with cmd: python setup.py install
'''

setup(
    name="Greengraph",
    version="1.0",
    packages=find_packages(exclude=['*test']),
    scripts=['scripts/greengraph.py'],
    install_requires=['argparse', 'requests', 'numpy', 'matplotlib', 'geopy']
)