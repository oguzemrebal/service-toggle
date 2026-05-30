from setuptools import setup, find_packages

setup(
    name="service-toggle",
    version="1.0.0",
    description="GTK4 panel to toggle background services and CPU cores",
    long_description=open("README.md").read(),
    long_description_content_type="text/markdown",
    author="oguzemrebal",
    license="GPL-3.0-or-later",
    packages=find_packages(),
    python_requires=">=3.10",
    entry_points={
        "console_scripts": [
            "service-toggle=service_toggle.__main__:main",
        ],
    },
    data_files=[
        ("share/applications",  ["data/service-toggle.desktop"]),
        ("share/icons/hicolor/scalable/apps", ["data/icons/service-toggle.svg"]),
    ],
    classifiers=[
        "License :: OSI Approved :: GNU General Public License v3 (GPLv3)",
        "Programming Language :: Python :: 3",
        "Environment :: X11 Applications :: GTK",
        "Topic :: System :: Systems Administration",
    ],
)
