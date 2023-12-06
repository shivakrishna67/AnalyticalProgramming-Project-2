from distutils.core import setup

setup(
    name='Motor_vehicle_collisions',
    version='0.2.1',
    description='Classes for technical analysis of building dataset.',
    author='Shivakrishna Macha',
    author_email='smacha@mail.yu.edu',
    license='MIT',
    url='https://github.com/shivakrishna67/AnalyticalProgramming-Project-3',
    packages=['Motor_vehicle_collisions'],
    install_requires=[
        'matplotlib>=3.7.1',
        'numpy>=1.24.3',
        'pandas>=1.5.3',
        'seaborn>=0.12.2',
    ],
)
