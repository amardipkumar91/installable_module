from setuptools import setup, find_packages
# setup(
#     name='my_package',
#     version='1.0.0',
#     author='Amardip Kumar',
#     author_email='kumar.amardip8@gmail.com',
#     description='Description of your package',
#     long_description=open('README.md').read(),
#     long_description_content_type='text/markdown',
#     url='https://github.com/amardipkumar91/installable_module',
#     packages=find_packages(),
#     install_requires=[
#         # List dependencies here if your package requires any
#     ],
#     classifiers=[
#         'Programming Language :: Python :: 3',
#         # Add more classifiers as needed
#     ],
# )


from setuptools import setup, find_packages

setup(
    name='myfiletest',  # Replace with your package name
    version='0.1.2',
    packages=find_packages(),
    author='Amardip Kumar',
    author_email='kumar.amardip8@gmail.com',
    description='all about test',
    long_description=open('README.md').read(),
    long_description_content_type='text/markdown',
    # url='https://github.com/your_username/your_package',  # Replace with your GitHub URL
    classifiers=[
        'Programming Language :: Python :: 3',
        # Add more classifiers as needed
    ],
    install_requires=[
        # Add any dependencies required by your package
    ],
)