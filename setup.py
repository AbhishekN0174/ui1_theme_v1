from setuptools import setup, find_packages
import re
import ast

with open("requirements.txt") as f:
    install_requires = f.read().strip().split("\n")

# get version from __version__ variable in glass_ui/__init__.py without importing the module
_version_re = re.compile(r"__version__\s+=\s+(.*)")
with open("glass_ui/__init__.py", "rb") as f:
    version = str(ast.literal_eval(_version_re.search(f.read().decode("utf-8")).group(1)))

setup(
    name="glass_ui",
    version=version,
    description="Glass UI Theme for Frappe",
    author="Your Company",
    author_email="info@yourcompany.com",
    packages=find_packages(),
    zip_safe=False,
    include_package_data=True,
    install_requires=install_requires,
)