from setuptools import find_packages, setup

setup(
    name="ingestion_pipe",
    packages=find_packages(exclude=["ingestion_pipe_tests"]),
    install_requires=[
        "dagster",
        "dagster-cloud"
    ],
    extras_require={"dev": ["dagster-webserver", "pytest"]},
)
