import os
from setuptools import setup, find_packages

def read_file(filename):
    basepath = os.path.dirname(os.path.dirname(__file__))
    filepath = os.path.join(basepath, filename)
    if os.path.exists(filepath):
        return open(filepath).read()
    else:
        return ''

setup(
    name='norilog',
    version='1.0.0',
    description='The NoriLog web application.',
    long_description=read_file('README-en.rst'),
    author='BeProud',
    author_email='project@beproud.jp',
    url='https://github.com/beproud/norilog/',
    classifiers=[
        'Development Status :: 4 - Beta',
        'Framework :: Flask',
        'License :: OSI Approved :: BSD License',
        'Programming Language :: Python',
        'Programming Language :: Python :: 3.6',
    ],
    python_requires=">=3.6",
    packages=find_packages(),
    include_package_data=True,
    keywords=['web', 'norilog'],
    license='BSD License',
    install_requires=[
        'Flask',
    ],
    entry_points="""
        [console_scripts]
        norilog = norilog:main
    """,
)

