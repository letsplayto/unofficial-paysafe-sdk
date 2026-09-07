from setuptools import setup, find_packages

setup(
    name="unofficial-paysafe-sdk",
    version="0.1.1",
    description="Unofficial Python SDK for Paysafe API (Card Payments)",
    author="letsplayto",
    author_email="letsplayto001@gmail.com",
    packages=find_packages(),
    install_requires=["requests", "aiohttp"],
    python_requires=">=3.8",
    entry_points={
        "console_scripts": [
            "paysafe=paysafe.cli:main",
        ],
    },
    extras_require={
        "dev": [
            "pytest>=7.0",
            "pytest-asyncio>=0.21",
            "responses>=0.25",
            "aioresponses>=0.7",
            "pytest-cov",
            "ruff",
        ],
    },
    classifiers=[
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",
        "Programming Language :: Python :: 3.11",
        "Programming Language :: Python :: 3.12",
        "Operating System :: OS Independent",
        "License :: OSI Approved :: MIT License",
        "Development Status :: 3 - Alpha",
        "Intended Audience :: Developers",
        "Topic :: Software Development :: Libraries :: Python Modules",
    ],
)
