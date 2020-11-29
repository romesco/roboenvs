from setuptools import setup, find_packages
import pkg_resources
import pathlib

with pathlib.Path("requirements.txt").open() as requirements_txt:
    install_requires = [
        str(requirement)
        for requirement in pkg_resources.parse_requirements(requirements_txt)
    ]

setup(
    name="robo-envs",
    version="0.1.0",
    packages=find_packages(include=[".*"]),
    author=["Rosario Scalise"],
    author_email=["rosario@cs.uw.edu"],
    url="http://github.com/romesco/roboenvs",
    include_package_data=True,
    install_requires=install_requires,
)

