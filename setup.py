import os
from setuptools import setup, find_packages
from portlets import __version__

version = __version__

here = os.path.abspath(os.path.dirname(__file__))
README = open(os.path.join(here, 'README.txt')).read()

setup(
    name='django-portlets',
    version=version,
    description='Generic portlets for Django.',
    long_description=README,
    classifiers=[
        'Development Status :: 5 - Production/Stable',
        'Environment :: Web Environment',
        'Framework :: Django',
        'License :: OSI Approved :: BSD License',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
    ],
    keywords='django portlets',
    author='Kai Diefenbach',
    author_email='kai.diefenbach@iqpp.de',
    url='https://github.com/diefenbach/django-portlets',
    license='BSD',
    packages=find_packages(exclude=['ez_setup']),
    include_package_data=True,
    zip_safe=False,
    install_requires=[
        'setuptools',
    ],
)
