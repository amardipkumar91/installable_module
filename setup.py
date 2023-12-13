from setuptools import setup, find_packages
setup(
    name='my_package',
    version='1.0.0',
    author='Amardip Kumar',
    author_email='kumar.amardip8@gmail.com',
    description='Description of your package',
    long_description=open('README.md').read(),
    long_description_content_type='text/markdown',
    # url='https://github.com/your_username/my_package',
    packages=find_packages(),
    install_requires=[
        # List dependencies here if your package requires any
    ],
    classifiers=[
        'Programming Language :: Python :: 3',
        # Add more classifiers as needed
    ],
)
