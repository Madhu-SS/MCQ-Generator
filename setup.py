# for instaling local pakages in virtual envirornment
from setuptools import find_packages,setup

setup(
    name='mcqgenrator',
    version='0.0.1',
    author='madhu s s',
    author_email='madhugowda426@gmail.com',
    install_requires=["openai","langchain","streamlit","python-dotenv","PyPDF2"],
    packages=find_packages()
)