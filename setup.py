from setuptools import setup, find_packages

setup(
    name='planner',
    version='0.1',
    packages=find_packages(),
    install_requires=[
        'kivy',
        'matplotlib',
        # inne zależności, które są w requirements.txt
    ],
    entry_points={
        'console_scripts': [
            'planner = main:main',  # jeśli chcesz uruchamiać aplikację z linii komend
        ],
    },
)