#! /usr/bin/env python
from setuptools import find_packages
from distutils.core import setup
import sys
try:
    reload(sys).setdefaultencoding('Utf-8')
except NameError: # fix for python >= 3.4.x
    from importlib import reload
    reload(sys)

setup(
    name='django-social-feeds-parser',
    version='0.5',
    packages=find_packages(),
    include_package_data=True,
    license='BSD License',
    description='A simple Django app to store and display what social media talk about site',
    long_description=open('README.rst').read(),
    url='https://github.com/RevSquare/django-social-feeds-parser',
    author='Tomasz Roszko, Guillaume Pousseo',
    author_email='tomaszroszko@revsquare.com, guillaumepousseo@revsquare.com',
    zip_safe=False,
    classifiers=[
        'Environment :: Web Environment',
        'Framework :: Django',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: BSD License',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Programming Language :: Python :: 2.6',
        'Programming Language :: Python :: 2.7',
        'Topic :: Internet :: WWW/HTTP',
        'Topic :: Internet :: WWW/HTTP :: Dynamic Content',
    ],
    install_requires=[
        'facebook-sdk==1.0.0',
        'python-instagram==1.3.2',
        'tweepy==3.3.0',
        'Pillow'
    ],
    dependency_links=[
        # 'https://github.com/ozgur/python-linkedin.git@master#egg=python-linkedin',
        'https://github.com/BrendanMartin/python-linkedin-v2.git',
    ],
    extras_require={
        'Linkedin':  ["python-linkedin-v2"],
    }
)
