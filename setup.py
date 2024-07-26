from setuptools import setup, find_packages
import os


def readme(file_name: str):
    with open(os.path.join(os.path.dirname(__file__), file_name)) as f:
        return f.read()


setup(
    name='libdb',
    version='1.0.3',
    packages=find_packages(),
    install_requires=[],
    test_suite='tests',
    author='Mmdrza',
    author_email='Pymmdrza@gmail.com',
    description='A simple JSON database manager',
    long_description=readme('README.md'),
    long_description_content_type='text/markdown',
    license='MIT',
    url='https://github.com/libdb/libdb',
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
    include_package_data=True

)
