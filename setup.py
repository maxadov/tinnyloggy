from setuptools import setup, find_packages

setup(
    name='tinnyloggy',
    version='0.1.1',
    packages=find_packages(),
    install_requires=[
        'colorama'
    ],
    author='Aydyn Maxadov',
    description='Lightweight terminal logger with timestamps and optional caller inspection.',
    long_description=open('README.md', encoding='utf-8').read(),
    long_description_content_type='text/markdown',
    url='https://github.com/yourusername/loggerx',  # если есть
    classifiers=[
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
    ],
    python_requires='>=3.6',
)
