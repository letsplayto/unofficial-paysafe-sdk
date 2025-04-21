from setuptools import setup, find_packages

setup(
    name='unofficial-paysafe-sdk',
    version='0.1.0',
    description='Unofficial Python SDK for Paysafe API (Card Payments)',
    author='letsplayto',
    author_email='letsplayto001@gmail.com',
    packages=find_packages(),
    install_requires=['requests', 'aiohttp'],
    python_requires='>=3.7',
    classifiers=[
        'Programming Language :: Python :: 3',
        'Operating System :: OS Independent',
        'License :: OSI Approved :: MIT License',
    ],
)
