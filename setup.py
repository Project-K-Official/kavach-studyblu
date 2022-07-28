from setuptools import setup, find_packages
import pathlib

here = pathlib.Path(__file__).parent.resolve()


VERSION = '0.0.1'
DESCRIPTION = 'Demo version of xedu'
LONG_DESCRIPTION = 'Demo version of xedu - long description'

# Setting up
setup(
    name="xedu",
    version=VERSION,
    author="VIT Bhopal",
    author_email="kabirdhruw24@gmail.com",
    description=DESCRIPTION,
    packages=find_packages(),
    install_requires=['pyautogui', 'pyqt5', 'pandas', 'PyQtWebEngine'],
    keywords=['python', 'video', 'pqt5', 'pyqt', 'education'],
    classifiers=[
        "Development Status :: 3 - Alpha",
        "Intended Audience :: Developers",
        "Programming Language :: Python :: 3",
        "Operating System :: Unix",
        "Operating System :: MacOS :: MacOS X",
        "Operating System :: Microsoft :: Windows",
        ],
        entry_points={
            'console_scripts': ['xedur=xedu.main:main']
        },
        include_package_data=True,
        package_data={'': ['./xedu/quiz/data.json']}
)
