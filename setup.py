"""
sentry-auth-govuk
==================
:copyright: (c) 2016 Crown copyright, Government Digital Service
"""

from setuptools import find_packages, setup

install_requires = [
    'sentry>=7.0.0,<9',
]

setup(
    name='sentry-auth-govuk',
    version='0.0.1',
    description="A Sentry plugin for GOV.UK's Signon service",
    url='https://github.com/alphagov/sentry-auth-govuk/',
    author='GOV.UK developers',
    author_email='govuk-dev@digital.cabinet-office.gov.uk',
    license='MIT',
    classifiers=[
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
    ],
    keywords='govuk alphagov sentry',
    packages=find_packages(),
    install_requires=install_requires,
    entry_points={
        'sentry.apps': [
            'auth_govuk = sentry_auth_govuk',
        ],
    },
)
