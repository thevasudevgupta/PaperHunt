import setuptools
import os

__version__ = "0.1.1"

with open("README.md", "r", encoding="utf-8") as file:
    long_description = file.read()

with open("requirements.txt", "r", encoding="utf-8") as file:
    install_requires = [p.strip() for p in file]

setuptools.setup(
    name="paperhunt",
    version=__version__,
    author="Vasudev Gupta",
    author_email="7vasudevgupta@gmail.com",
    description="Script for hunting trending papers everyday.",
    long_description=long_description,
    long_description_content_type="text/markdown",
    license="Apache",
    url="https://github.com/VasudevGupta7/paperhunt",
    packages=setuptools.find_packages(),
    install_requires=install_requires,
    entry_points={"console_scripts": ["hunt=paperhunt.paperhunt:main"]},
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: Apache Software License",
        "Operating System :: OS Independent",
        "Topic :: Scientific/Engineering :: Artificial Intelligence"
    ],
    python_requires='>=3.6',
)

os.system("python -m spacy download en_core_web_md")
