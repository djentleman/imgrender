import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="imgrender",
    version="0.0.1",
    author="Todd Perry",
    author_email="todd.perry@myport.ac.uk",
    description="Python terminal image renderer",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/djentleman/imgrender",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: Linux/OSX",
    ],
    entry_points={
        'console_scripts': [
            'imgrender = imgrender:main',
        ],
    },
    python_requires='>=3.6',
)
