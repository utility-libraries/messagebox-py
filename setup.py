import setuptools

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()


__author__ = "PlayerG9"
__version_info__ = (0,1,0)
__version__ = '.'.join(str(i) for i in __version_info__)


setuptools.setup(
    name="messagebox",
    version=__version__,
    author=__author__,
    # author_email="author@example.com",
    description="display messageboxes without library dependency like tkinter",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/PlayerG9/PyMessageBox",
    project_urls={
        "Author Github": "https://github.com/PlayerG9",
        "Bug Tracker": "https://github.com/PlayerG9/PyMessageBox/issues",
    },
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    package_dir={"": "src"},
    packages=setuptools.find_packages(where="src"),
    python_requires=">=3.6",
)
