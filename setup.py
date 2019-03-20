import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

exec(open('./version.py').read())
setuptools.setup(
    name="gasstation-express-oracle",
    version=__version__,
    author="Pillar Project",
    description="gasstation-express-oracle package to jfrog ",
    url="https://pillarproject.jfrog.io/pillarproject/api/pypi/pypi",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
    ],
)
