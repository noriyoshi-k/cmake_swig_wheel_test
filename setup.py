# coding:utf-8
from setuptools import setup, Distribution
from os.path import *
from os import makedirs
from shutil import copyfile
class BinaryDistribution(Distribution):
    def is_pure(self):
        return False

package_name="test"
extension_dir="build"

if not exists(package_name):
    makedirs(package_name)

extension_script_name=join(extension_dir,package_name+'.py')
extension_name="_"+package_name+".so"

copyfile(extension_script_name,join(package_name,"__init__.py"))
copyfile(join(extension_dir,extension_name),
         join(package_name,extension_name))

setup(
    name=package_name,
    version='1.0',
    description='Test Library',
    packages=[package_name,],
    package_data={
        package_name: [extension_name],
    },
    distclass=BinaryDistribution
)
