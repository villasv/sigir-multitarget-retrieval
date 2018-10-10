from setuptools import setup, find_packages

VERSION = '0.0.1'

setup(
    name='germs',
    version=VERSION,
    description='Generalized retrieval metrics for ranking evaluation',
    long_description=open('README.rst', 'r').read(),
    author='Victor Villas',
    author_email='villasv@outlook.com',
    download_url='https://github.com/villasv/germs',
    license='Apache License 2.0',
    install_requires=[
        'numpy',
    ],
    extras_require={
        'dev': [
            'pytest'
        ],
    },
    keywords='information retrieval, evaluation metrics, learning to rank',
    classifiers=[
        'Programming Language :: Python :: 3',
    ],
    packages=find_packages(),
)
