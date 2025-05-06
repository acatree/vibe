from setuptools import setup, find_packages

setup(
    name='vibe-dsl',
    version='0.1.0',
    packages=find_packages(),
    install_requires=[
        'click',  # Add other dependencies as needed
    ],
    entry_points={
        'console_scripts': [
            'vibe = vibe.cli:cli',  # Points to the 'build' command in cli.py
        ],
    },
)
