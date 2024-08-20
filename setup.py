from setuptools import setup, find_packages

setup(
    name="PyFinOps",
    version="0.1.0",
    author="Anubhav Sharma",
    author_email="anubhav9287@gmail.com",
    description="A comprehensive toolkit for various financial calculations and tools.",
    long_description=open('README.md').read(),
    long_description_content_type="text/markdown",
    url="https://github.com/anubhav9287/PyFinOps",
    packages=find_packages(exclude=["tests"]),
    entry_points={
        "console_scripts": [
            "sip-calculator=pyfinops.scripts:sip_calculator",
            "compound-interest=pyfinops.scripts:compound_interest_calculator",
        ],
    },
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
)
