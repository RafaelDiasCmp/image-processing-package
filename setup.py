from setuptools import setup, find_packages

with open("README.md", "r") as f:
    page_description = f.read()

with open("requirements.txt") as f:
    requirements = f.read().splitlines()

setup(
    name="image_processing-rafael-dias-campos",
    version="0.0.1",
    author="Rafael Dias Campos",
    author_email="raffaeldiascampos@gmail.com",
    description="Image processing Package using Skimage",
    long_description=page_description,
    long_description_content_type="text/markdown",
    url="https://github.com/RafaelDiasCmp/image-processing-package/tree/master",
    packages=find_packages(),
    install_requires=requirements,
    python_requires='>=3.8',
)
