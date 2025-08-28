from setuptools import setup, find_packages

setup(
    name="fyze-logger",
    version="1.0.0",
    description="A stylish Python terminal logger with fyze branding",
    author="Fyze",
    packages=find_packages(),
    install_requires=["colorama"],
    python_requires=">=3.8",
)
