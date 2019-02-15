from setuptools import setup, find_packages

setup(
    name='bip44',
    version='1.0.0',
    description='Python code to generate Ethereum addresses from a hierarchical deterministic wallet according to the BIP44 standard.',
    author='Michail Brynard',
    packages=find_packages(),
    install_requires=[
        'rlp==1.1.0',
        'eth-utils==1.4.1',
        'two1==3.10.9',
        'pycrypto==2.6.1',
        'pycryptodome==3.7.3',
    ],
)