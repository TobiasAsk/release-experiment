import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="scimatch-tobask",
    author="Tobias Ask",
    use_scm_version=True,
    setup_requires=['setuptools_scm'],
    author_email="tobias.ask.92@gmail.com",
    description="A collection of hamcrest matchers for Numpy and xarray",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/TobiasAsk/release-experiment",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
)
