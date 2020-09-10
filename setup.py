# Based directly on setuptools
from setuptools import setup, find_packages
import pathlib

curr_dir = pathlib.Path(__file__).parent.resolve()

long_description = (curr_dir / 'README.md').read_text(encoding='utf-8')

"""You can configure more options
See More: https://packaging.python.org/guides/distributing-packages-using-setuptools/
Below are the required ones with a couple of optional that might come in handy
"""

setup(
    name='yourpkg',
    version='0.0.1',
    author='Your name',
    author_email='author@yourdomain.com',
    description="Your sample Python project",
    long_description=long_description,
    long_description_content_type='text/markdown',
    url='https://github.com/user_name/project',
    classifiers=[
        'Development Status :: 3 - Alpha',
        'Intended Audience :: Developers',
        'Topic :: Software Development :: Build Tools',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
        'Programming Language :: Python :: 3 :: Only',
    ],
    keywords='some, keywords, for, your, project, here',
    packages=find_packages(where='src'),
    project_urls={
        'Bug Reports': 'https://github.com/pypa/yourproject/issues',
        'Source': 'https://github.com/user_name/yourproject',
    },
    license='MIT'
)