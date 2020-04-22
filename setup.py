from setuptools import setuptools, find_packages

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="flatpak-sync", 
    version="1.0.2",
    author="JJO",
    author_email="jeteokeeffe@yahoo.com",
    description="Automate Installation and Permissions of Flatpak Applications",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/jeteokeeffe/flatpak-sync",
    packages=find_packages(exclude=["tests.*", "tests"]),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: POSIX :: Linux",
    ],
    entry_points={
        "console_scripts": [
            "flatpak-sync=flatpaksync.main:main"
        ]
    },
    python_requires='>=3.6',
    install_requires=['Click']
)
