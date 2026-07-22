from setuptools import setup, find_packages

setup(
    name="rigby-launcher",
    version="1.0.0",
    description="Rigby Launcher - Among Us game launcher with integrated Itch Login Fixer",
    packages=find_packages(),
    python_requires=">=3.8",
    entry_points={
        "console_scripts": [
            "rigby-launcher=rigby_launcher.__main__:main",
        ],
    },
)
