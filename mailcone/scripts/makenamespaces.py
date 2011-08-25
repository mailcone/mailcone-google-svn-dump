#!/opt/python-buildout/python-2.6/bin/python2.6


SVN = ['branches', 'tags', 'trunk']

NAMESPACE = ['raptus','mailcone']

PACKAGES =['mailfilter',
          'mfa_complexmatchfilter',
          'mfa_core_action',
          'mfa_core_auth',
          'mfa_core_customer',
          'mfa_core_filter',
          'mfa_pythoncodefilter',
          'mfa_sendnotificationaction',
          'mfa_simplematchfilter',
          'mfa_writelogaction',
          ]


import os
import shutil

for package in PACKAGES:
    fullnamespace = '.'.join(NAMESPACE + [package])
    os.makedirs(fullnamespace)
    for svn in SVN:
        path = os.path.join(fullnamespace, svn)
        os.makedirs(path)
    ns = [fullnamespace, svn]
    for f in NAMESPACE:
        ns.append(f)
        os.makedirs(os.path.join(*ns))
    shutil.move(package, os.path.join(*ns))


