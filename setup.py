from setuptools import setup, find_packages


setup( 
    name='finsHt', 
    version='0.0.1',
    packages=['finsHt'],
    author='Maysam & Roger', 
    description= 'Fin and tube heat transfer', 
    long_description=open("README.md","r", encoding="utf-8").read(),
    #install_requires=['CoolProp'],
)
