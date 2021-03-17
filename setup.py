from setuptools import setup, find_packages
with open('README.md', 'r') as f:
    description = f.read()

setup(
    name='easy_tbot',
    version='1.0.6',
    packages=find_packages(),
    include_package_data=True,
    entry_points={'console_scripts':['create-tbot=easy_tbot.cookiecutters.create_project:create']},
    
    install_requires=['aiogram~=2.11.2', 'Jinja2~=2.11.2', 'six~=1.15.0','SQLAlchemy~=1.3.19'],
    
    url='https://github.com/Gaspect/easy_tbot',
    license='GNU LESSER GENERAL PUBLIC LICENSE',
    author='Jesús Enrique Fuentes González',
    author_email='jesusefg12@gmail.com',
    description='Mini framework  for data base and other usefull stuff integration with Telegram bot api',
    long_description=description,
    long_description_content_type="text/markdown",
    python_requires='>=3.6',
    
    classifiers=[
        "Operating System :: OS Independent",
        "Development Status :: 5 - Production/Stable",
        "Framework :: AsyncIO",
        "License :: OSI Approved :: GNU Lesser General Public License v3 or later (LGPLv3+)",
        "Intended Audience :: Developers",
        "Programming Language :: Python :: 3",
        "Topic :: Communications",
        "Topic :: Software Development :: Libraries :: Application Frameworks"
    ]
)
