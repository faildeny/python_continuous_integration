from setuptools import setup

with open("README.md", "r") as f:
    long_description = f.read()

setup(
    name="sample_app",
    version="1.0",
    description="Sample app for continuous integration tests",
    license="MIT",
    long_description=long_description,
    author="Grzegorz Skorupko",
    author_email="grzegorz.skorupko@gmail.com",
    packages=["sample_app"],
    install_requires=["numpy"],
)
