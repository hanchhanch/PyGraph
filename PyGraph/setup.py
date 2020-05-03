
import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="PyGraph", # Replace with your own username
    version="0.0.1",
    author="Hanoch Rahimi",
    author_email="hanoch.rahimi@gmail.com",
    description="Graphs infrastructure library",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/pypa/sampleproject",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.5',
)