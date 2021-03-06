"""
Created on 24/gen/2014

@author: Marco Pompili
"""

import os
from setuptools import setup

README = open(os.path.join(os.path.dirname(__file__), 'README.rst')).read()

os.chdir(os.path.normpath(os.path.join(os.path.abspath(__file__), os.pardir)))

setup(
    name=str('django-facebook-social-plugins'),
    version='0.1',
    packages=['django_fbplugins', 'django_fbplugins.templatetags'],
    include_package_data=True,
    license=str('MIT License'),
    description=str('Django wrapper tags on facebook social plugins.'),
    long_description=README,
    url=str('https://github.com/marcopompili/django-facebook-social-plugins'),
    author=str('Marco Pompili'),
    author_email=str('django@emarcs.org'),
    install_requires = ['django'],
    classifiers=[
        'Environment :: Web Environment',
        'Framework :: Django',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Programming Language :: Python :: 2.6',
        'Programming Language :: Python :: 2.7',
        'Topic :: Internet :: WWW/HTTP',
        'Topic :: Internet :: WWW/HTTP :: Dynamic Content',
    ],
)