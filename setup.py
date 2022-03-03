from setuptools import setup, find_packages

setup(
    name="learning-python",
    extras_require=dict(tests=['pytest']),
    packages=find_packages(where='src/learning'),
    package_dir={"": "src"},
)
