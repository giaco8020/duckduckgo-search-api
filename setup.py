import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="duckduckgo_search_api",
    version="0.1.3",
    author="giaco8020",
    description="A simple and lightweight Python wrapper for DuckDuckGo search.",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/giaco8020/duckduckgo-search-api",
    package_dir={"": "src"},
    packages=setuptools.find_packages(where="src"),
    install_requires=[
        "requests>=2.24.0",
        "beautifulsoup4>=4.9.3",
    ],
    extras_require={
        "dev": [
            "pytest>=3.7",
        ]
    },
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
)
