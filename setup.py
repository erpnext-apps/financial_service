from setuptools import setup, find_packages

with open("requirements.txt") as f:
	install_requires = f.read().strip().split("\n")

# get version from __version__ variable in financial_service/__init__.py
from financial_service import __version__ as version

setup(
	name="financial_service",
	version=version,
	description="Manages API Request queuing",
	author="Frappe Technologies Pvt. Ltd. and Contributors",
	author_email="developers@frappe.io",
	packages=find_packages(),
	zip_safe=False,
	include_package_data=True,
	install_requires=install_requires
)
