from setuptools import setup

setup(
    name='django-ot',
    version='0.2',
    packages=['django_ot', 'django_ot.migrations', 'django_ot.management',
              'django_ot.management.commands',
              'django_ot.otcms',
              'django_ot.otcms.migrations'],
    include_package_data=True,
    license='MIT',
    description='django application for opentopic',
    url='https://github.com/tomaszroszko/django-ot',
    author='Tomasz Roszko',
    author_email='tomaszroszko@gmail.com',
    zip_safe=False,
    classifiers=[
        'Environment :: Web Environment',
        'Framework :: Django',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: BSD License',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Programming Language :: Python :: 2.6',
        'Programming Language :: Python :: 2.7',
        'Topic :: Internet :: WWW/HTTP',
        'Topic :: Internet :: WWW/HTTP :: Dynamic Content',
        ],
)