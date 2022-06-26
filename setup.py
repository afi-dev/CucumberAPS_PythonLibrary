# /*!
#  * CucumberAPS_PythonLibrary | V.0.1
#  * (c) 2022 Afi
#  * Released under the MIT License.
#  */

from setuptools import setup, find_packages
import pathlib

long_description = (pathlib.Path(__file__).parent.resolve() / "README.md").read_text(encoding="utf-8")

print("""

   _____                           _                      _____   _____  _____       _      _ _                          
  / ____|                         | |               /\   |  __ \ / ____||  __ \     | |    (_) |                         
 | |    _   _  ___ _   _ _ __ ___ | |__   ___ _ __ /  \  | |__) | (___  | |__) |   _| |     _| |__  _ __ __ _ _ __ _   _ 
 | |   | | | |/ __| | | | '_ ` _ \| '_ \ / _ \ '__/ /\ \ |  ___/ \___ \ |  ___/ | | | |    | | '_ \| '__/ _` | '__| | | |
 | |___| |_| | (__| |_| | | | | | | |_) |  __/ | / ____ \| |     ____) || |   | |_| | |____| | |_) | | | (_| | |  | |_| |
  \_____\__,_|\___|\__,_|_| |_| |_|_.__/ \___|_|/_/    \_\_|    |_____/ |_|    \__, |______|_|_.__/|_|  \__,_|_|   \__, |
                                                                    ______      __/ |                               __/ |
                                                                   |______|    |___/                               |___/ 
""")

setup(
    name="cucumberaps",
    version="0.5",
    description="An unofficial library to manage CucumberAPS licenses in python",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/afi-dev/CucumberAPS_PythonLibrary",
    author="Afi",
    author_email="aconique@gmail.com",
    classifiers=[
        "Operating System :: OS Independent",
        "License :: OSI Approved :: MIT License",
        "Development Status :: 5 - Production/Stable",
        "Intended Audience :: Developers",
        "Topic :: Software Development :: Libraries",
    ],
    keywords="Lib Library CucumberAPS Licenses",
    package_dir={
	"": "src"
    },
    packages=find_packages(where="src"),
    include_package_data=True,
    scripts=[],
    extras_require={},
    zip_safe=False,
    python_requires=">=3",
    project_urls={
        "Issues": "https://github.com/afi-dev/CucumberAPS_PythonLibrary/issues",
        "Ko-fi": "https://ko-fi.com/afidev",
        "Buy me a coffee": "https://www.buymeacoffee.com/afidev",
        "Documentation": "https://github.com/afi-dev/CucumberAPS_PythonLibrary/wiki",
        "Source": "https://github.com/afi-dev/CucumberAPS_PythonLibrary",
    },
)
