from setuptools import setup, find_packages

with open("requirements.txt", "r") as f:
    install_requires = f.read().strip().split("\n")

setup(
    name="frappe_ui_template",
    version="0.1.0",
    description="Custom UI Template for Frappe ERPNext",
    author="Custom UI",
    author_email="info@example.com",
    packages=find_packages(),
    zip_safe=False,
    include_package_data=True,
    install_requires=install_requires
)
