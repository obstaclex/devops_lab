from setuptools import setup, find_packages

INSTALL_REQUIREMENTS = [
    'psutil>=4.2.0, <6.0.0'
]


def do_setup():
    setup(
        name='Snapshot_system_params',
        version='1.0',
        packages=find_packages(),
        entry_points={
            'console_scripts':
            ['snapshot = collect_info.main:main']
        },
        author="Ilya_Melnik1",
        author_email="Ilya_Melnik1@epam.com",
        description="Script for collect system metrics",
        install_requires=INSTALL_REQUIREMENTS
    )


if __name__ == "__main__":
    do_setup()
