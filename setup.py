import setuptools, pollo

# Get markdown
with open("README.md") as f:
    long_description = f.read()

setuptools.setup(
    name="pollo",
 
    version=pollo.__version__,
 
    author="Cyclone Communications",
 
    author_email="hello@cyclone.biz",
 
    description="A event driven framework for large scale automation.",

    long_description=long_description,
    long_description_content_type="text/markdown",
 
    url="https://github.com/CycloneBiz/Pollo",
    
    packages=["pollo"],
 
    install_requires=[],
 
    license="CC0",
 
    classifiers=[
        "Programming Language :: Python :: 3",
        "Operating System :: OS Independent"
    ]
)