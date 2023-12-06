from distutils.core import setup

setup(
    name='my_package',
    version='0.1.0',
    author='Shivakrishna Macha',
    author_email='smacha@mail.yu.edu',
    description="A package for extracting and analyzing web data",
    long_description_content_type="text/markdown",  # Fixed attribute name and added a comma
    url='https://github.com/shivakrishna67/AnalyticalProgramming-Project-2',
    packages=['Motor_vehicle_collisions'],
    install_requires=[
        "requests>=2.25.1",
        "pandas>=1.2.0",
        "beautifulsoup4>=4.9.3",
    ],
)
