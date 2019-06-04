import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="hiking_project_client",
    version="0.0.1",
    author="Michael Henry",
    author_email="michael@michaelhenry.me",
    description="A python client for the Hiking Project Data API",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/lexmono/hiking_project_client",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
)
