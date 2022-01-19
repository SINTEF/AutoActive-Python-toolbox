from setuptools import setup, find_packages
from pathlib import Path

src_folder = Path(__file__).parent
long_des_fname = Path.joinpath(src_folder, "README").with_suffix(".md")
long_description = long_des_fname.read_text()


setup(
    name="autoactive",
    version="0.2.0",
    description="Module for reading and writing aaz files",
    long_description = long_description,
    long_description_content_type='text/markdown',
    url="https://github.com/SINTEF/AutoActive-Python-toolbox.git",
    author="Kasper Botker",
    author_email="kasper.botker@sintef.no",
    license="Apache License Version 2.0",
    packages=find_packages(),
    python_requires=">=3.8",
    install_requires=["numpy", "pandas", "pyarrow"],
    classifiers=[
        "Development Status :: 3 - Alpha",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",
    ],
)
