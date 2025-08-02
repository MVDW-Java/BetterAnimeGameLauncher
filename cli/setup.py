from setuptools import setup, find_packages

setup(
    name="bagl-cli",
    version="0.1.0",
    packages=find_packages(),
    install_requires=[
        "bagl-lib>=0.1.0",  # Depend on the library package
    ],
    entry_points={
        'console_scripts': [
            'bagl=bagl_cli.cli:main',
        ],
    },
    python_requires=">=3.6",
    description="Better Anime Game Launcher Library",
    author="MVDW-Java",
)
