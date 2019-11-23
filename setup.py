from setuptools import setup, find_packages


setup(
    name='tcc2019',
    version="0.0.1",
    packages=find_packages(),
    entry_points={
        'console_scripts': [
            "tgnews = tgnews.main:main",
            "prepare = tgnews.main:prepare_main",
        ],
    },
    python_requires=">=3.7,<3.8",
    install_requires=[
    ],
)
