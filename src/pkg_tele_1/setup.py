from setuptools import setup

package_name = 'pkg_tele_1'

setup(
    name=package_name,
    version='0.0.0',
    packages=[package_name],
    data_files=[
        ('share/ament_index/resource_index/packages',
            ['resource/' + package_name]),
        ('share/' + package_name, ['package.xml']),
        ('share/'+ package_name + '/launch', ['launch/launch_tele_1.py'])
    ],
    install_requires=['setuptools'],
    zip_safe=True,
    maintainer='varzeny',
    maintainer_email='varzeny@gmail.com',
    description='TODO: Package description',
    license='TODO: License declaration',
    tests_require=['pytest'],
    entry_points={
        'console_scripts': [
            'node_keyboard = pkg_tele_1.node_keyboard:main',
            'node_move = pkg_tele_1.node_move:main'

        ],
    },
)
