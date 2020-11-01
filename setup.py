from setuptools import setup
from setuptools import setup, find_packages

with open("README.md", "r") as readme_file:
    readme = readme_file.read()

requirements = ["matplotlib>=3",
                "speedtest-cli>=2.1",
                "requests>=2.24"]

setup(
    name="internet-monitor",
    version="0.0.1",
    author="Andy Byers",
    author_email="a@ajb.app",
    url="https://github.com/andybyers21/internet-monitor"
    description="Monitor your internet speeds & produce visulisations",
    long_description=readme,
    long_description_content_type="text/markdown",
    url="https://github.com/",
    packages=find_packages(),
    install_requires=requirements,
    classifiers=[
        "Programming Language :: Python :: 3.8",
        "License :: OSI Approved"],
)
