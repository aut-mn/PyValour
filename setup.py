from setuptools import setup, find_packages

setup(
    name="PyValour",
    version="0.0.1",
    author="aut-mn",
    author_email="autumn@autmn.net",
    description="A python-based SDK for Valour",
    long_description="",
    long_description_content_type="text/markdown",
    package_dir={"": "src"},
    packages=find_packages(where="src"),
    python_requires=">=3.6"
)
