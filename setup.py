from setuptools import setup, find_packages

VERSION = '0.1.1'
DESCRIPTION = 'Prefix or Suffix file name with combination'

with open("README.md", "r") as fh:
    LONG_DESCRIPTION = fh.read()

# Setting up
setup(
    name="combogen",
    version=VERSION,
    author="byte2code (Mausam Giri)",
    author_email="<mausamkumargiri@proton.me>",
    url="https://github.com/byte2code/combogen",
    description=DESCRIPTION,
    long_description=LONG_DESCRIPTION,
    long_description_content_type="text/markdown",
    packages=find_packages(),
    keywords=['python', 'combination', 'files', 'unique', 'random filename generator', 'unique prefix suffix'],
    classifiers=[
        "Development Status :: 1 - Planning",
        "Intended Audience :: Developers",
        "Programming Language :: Python :: 3",
        "Operating System :: Unix",
        "Operating System :: MacOS :: MacOS X",
        "Operating System :: Microsoft :: Windows",
    ]
)