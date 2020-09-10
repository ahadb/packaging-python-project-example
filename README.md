# Example - Package Python Project
Look at the tree below, this is basically all you need to setup a Python Package - there are other options available and
you can find more here: [Packaging Python Projects](https://packaging.python.org/tutorials/packaging-projects/)

```bash
├── LICENSE
├── README.md
├── __pycache__ # hidden directory
│   └── setup.cpython-36.pyc
├── data
│   └── dummy_data.json
├── my_pkg
│   └── __init__.py
├── setup.py
├── tests
    ├── __init__.py
    └── test_your_app.py
```

Make sure you have `setuptools` and `wheel` installed

Run this command where `setup.py` is located, these will be used to distribute your awesome stuff:

```bash
python3 setup.py sdist bdist_wheel
```

You should see two generated files in the dist directory:

```bash
dist/
  yourpkg-0.0.1.tar.gz
  youryourpkg-0.0.1-py3-none-any.whl
```

After all the above you can finally upload your distribution archives by registering creating a token
and uploading using `twine`. You can read the docs at [Python Packaging Authority](https://www.pypa.io/en/latest/) for all of that

## Your Package (delete above and use below)
This is a placeholder for your project README. You can use: [Github-flavored Markdown](https://guides.github.com/features/mastering-markdown/)
to write your own description about your awesome project.

