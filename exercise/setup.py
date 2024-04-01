from setuptools import find_packages, setup

# Package meta-data.
NAME = "reportinput"
VERSION = "0.0.1"
AUTHOR = "James Westfall"
EMAIL = "james.westfall@neat.no"
DESCRIPTION = "Works out the parameters for your report"
REQUIRES_PYTHON = ">=3.10"

INSTALL_REQUIRES = [
    "pytest"
    ]

about = {}
about["__version__"] = VERSION

setup(
   name=NAME,
    version=about["__version__"],
    description=DESCRIPTION,
    author=AUTHOR,
    author_email=EMAIL,
    install_requires=INSTALL_REQUIRES,
    packages=find_packages(exclude=["tests", "*.tests", "*.tests.*", "tests.*"]),
)
