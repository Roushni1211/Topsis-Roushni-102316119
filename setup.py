from setuptools import setup, find_packages

setup(
    name='Topsis-Roushni-102316119',
    version='1.0.0',
    packages=find_packages(),
    install_requires=[
        'pandas',
        'numpy'
    ],
    entry_points={
        'console_scripts': [
            'topsis=topsis.topsis:main'
        ]
    },
    author='Roushni',
    description='TOPSIS Implementation using Python',
)
