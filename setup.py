from setuptools import setup

setup(name='django-timesince-human',
      version='0.1',
      description="Humanized and localized timesince template filter for Django",
      long_description="",
      author='Markus Kaiserswerth',
      author_email='mkai@sensun.org',
      license='GPL',
      packages=['timesince_human'],
      zip_safe=True,
      install_requires=['django'],
)
