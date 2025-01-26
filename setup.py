from setuptools import setup, find_packages

setup(
    name="drs-fastapi",
    version="1.4.0",
    description="Data Repository Service (DRS) API implementation using FastAPI.",
    long_description=open("README.md").read(),
    long_description_content_type="text/markdown",
    author="Your Name",
    author_email="your.email@example.com",
    url="https://github.com/<your-username>/drs-fastapi",
    packages=find_packages(where="app"),
    package_dir={"": "app"},
    install_requires=[
        "fastapi>=0.68.0",
        "uvicorn>=0.15.0",
        "pytest>=6.2.0",
        "httpx>=0.18.0",
    ],
    classifiers=[
        "Development Status :: 4 - Beta",
        "Intended Audience :: Developers",
        "License :: OSI Approved :: Apache Software License",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",
        "Operating System :: OS Independent",
    ],
    python_requires=">=3.9",
    entry_points={
        "console_scripts": [
            "drs-api=main:main",
        ],
    },
)