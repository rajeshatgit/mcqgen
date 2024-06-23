from setuptools import find_packages, setup
from setuptools.command.egg_info import egg_info as _egg_info

class egg_info(_egg_info):
    def find_sources(self):
        _egg_info.find_sources(self)
        with open(self.egg_info + '/top_level.txt', 'w') as f:
            f.write('src\n')

setup(
    name='mcqgenerator',
    version='0.0.1',
    author='rajesh',
    author_email='rjmaverick69@gmail.com',
    package_dir={'': 'src'},
    packages=find_packages(where='src'),
    install_requires=['openai', 'langchain', 'streamlit', 'python-dotenv', 'PyPDF2'],
    cmdclass={'egg_info': egg_info}
)


