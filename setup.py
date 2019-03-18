from setuptools import setup, find_packages

setup(
    name='arrayOperation',
    version='0.1',
    packages=find_packages(exclude=['tests*']),
    license='MIT',
    description='Array operations package',
    long_description=open('README.md').read(),
    install_requires=['numpy'],
    url='https://github.com/cooljayza/array-manipulation-package.git',
    author='Jacob Khoza',
    author_email='jacobmbeestokhoza@gmail.com'
)
