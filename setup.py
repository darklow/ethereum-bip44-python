from setuptools import setup, find_packages

setup(
    name='bip44',
    version='1.0.0',
    description='Python code to generate Ethereum addresses from a hierarchical deterministic wallet according to the BIP44 standard.',
    author='Michail Brynard',
    packages=find_packages(),
    install_requires=[
        'rlp',
        'eth-utils',
        'pycrypto',
        'pycryptodome',
    ],
)