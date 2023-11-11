from setuptools import setup, find_packages

setup(
    name='codeGrader',
    version='0.1',
    packages=find_packages(),
    entry_points={
        'console_scripts': [
            'grademe = codegrader_pkg.codeGrader:main'
        ]
    }
)
