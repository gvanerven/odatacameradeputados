from distutils.core import setup

setup(
    name='odatacameradeputados',
    version='0.0.1',
    packages=['odatacameradeputados'],
    url='https://github.com/gvanerven/odatacameradeputados',
    license="""
    Copyright 2017

    Licensed under the Apache License, Version 2.0 (the "License");
    you may not use this file except in compliance with the License.
    You may obtain a copy of the License at
    
        http://www.apache.org/licenses/LICENSE-2.0
    
    Unless required by applicable law or agreed to in writing, software
    distributed under the License is distributed on an "AS IS" BASIS,
    WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
    See the License for the specific language governing permissions and
    limitations under the License.
            """,
    author='Gustavo van Erven',
    author_email='',
    description='API para acesso aos dados abertos da câmara dos deputados',
    install_requires=[
        'requests',
    ],
    zip_safe=False)
