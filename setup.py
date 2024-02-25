import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="duckduckgo-search-api",
    version="0.1.1",
    author="giaco8020",
    description="Easy, Fast, Lightweight module for searching on https://duckduckgo.com",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/giaco8020/DuckDuckGo-Search-Api",
    packages=setuptools.find_packages(),
    install_requires=[
        "requests >= 2.24.0",
        "beautifulsoup4 >= 4.9.3",
    ],
    extras_require={
        "dev": [
            "pytest >= 3.7",
        ]
    },
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
)
