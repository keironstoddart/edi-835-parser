import setuptools

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

install_requires = [
    'pandas'
]

tests_require = [
    'pytest'
]

setuptools.setup(
    name="edi-835-parser",
    version="1.1.1",
    author="Keiron Stoddart",
    author_email="keiron.stoddart@gmail.com",
    description="A simple EDI 835 file format parser.",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/keironstoddart/edi-835-parser",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3.9",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    install_requires=install_requires,
    tests_require=tests_require,
    python_requires='>=3.9',
)