from setuptools import setup, find_packages

setup(
    name='calctree_client',
    version='0.1.0',
    packages=find_packages(where="src"),
    package_dir={'': 'src'},
    install_requires=[],
    author='CalcTree',
    description='Python client for the CalcTree API',
    url='https://github.com/calctree/calctree-python-client',
)
