from setuptools import setup, find_packages

setup(
    name="msuliot.data.loaders",
    version="0.2.0",
    author="Michael Suliot",
    author_email="michael@suliot.com",
    description="Some basic helper functions for AI projects",
    long_description=open('README.md').read(),
    url="https://github.com/msuliot/package.data.loaders.git",
    packages=find_packages(),
    install_requires=[
        'python-docx',
        'PyPDF2',
        'openpyxl',
        'python-pptx',
        'xlrd',
        'pandas',
        'PyMuPDF',
        'nltk',
        'numpy',
        'requests',
        'beautifulsoup4'
    ],
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.12',
)
