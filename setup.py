# type: ignore
"""mobile_modem_exporter setup.py for setuptools.

Source code available at https://github.com/tykling/mobile_modem_exporter/
Can be installed from PyPi https://pypi.org/project/mobile_modem_exporter/
Read more at https://mobile-modem-exporter.readthedocs.io/en/latest/
"""
import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="mobile_modem_exporter",
    version="0.1.0",
    author="Thomas Steen Rasmussen",
    author_email="thomas@gibfest.dk",
    description="mobile_modem_exporter is a Prometheus exporter for mobile modems. It uses pySerial and pexpect to speak to the modems and prometheus_client to write to node_exporter textfile_collector path.",
    license="BSD License",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/tykling/mobile_modem_exporter",
    packages=["mobile_modem_exporter"],
    entry_points={
        "console_scripts": [
            "mobile_modem_exporter = mobile_modem_exporter.mobile_modem_exporter:main"
        ]
    },
    classifiers=[
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
        "License :: OSI Approved :: BSD License",
        "Operating System :: OS Independent",
    ],
    python_requires=">=3.7",
    install_requires=["pipeserial", "prometheus_client"],
    include_package_data=True,
)
