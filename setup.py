from setuptools import setup

setup(
    name='terraform-aws-icons',
    version='0.1.0',
    url='https://github.com/github/terraform-aws-icons',
    license='MIT',
    author='TabbedOut',
    author_email='github@tabbedout.com',
    description='Annotate Terraform graphs with AWS icons.',
    long_description=open('README.rst').read(),
    py_modules=['aws_icons'],
    packages=['icons'],
    include_package_data=True,
    zip_safe=False,
    entry_points={
        'console_scripts': ['terraform-iconify=aws_icons:main']
    },
    platforms='any',
    classifiers=[
        'Development Status :: 4 - Beta',
        'Environment :: Console',
        'Programming Language :: Python',
        'Programming Language :: Python :: 2',
        'Programming Language :: Python :: 3',
    ]
)
