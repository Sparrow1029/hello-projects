#!/usr/bin/env python3
#-*- coding: utf-8 -*-

import os
basedir = os.path.abspath(os.path.dirname(__file__))

CSRF_ENABLED = True
SECRET_KEY = 'you-will-never-guess'

OAUTH_CREDENTIALS = { #tutorial has app.config['OAUTH_CRED...']' unnecessary}
    'facebook': {
        'id': '',
        'secret': ''
    },
    'twitter': {
        'id': '5QBffUro5Z9cDzhHyKOWGn6jo',
        'secret': 'QXKyDpugSvfgBYG1AGiFsUuu0Cp0BVwWauL2TPvZSK4AK96H1z'
    }
}

OPENID_PROVIDERS = [
    {'name': 'Google', 'url': 'https://www.google.com/accounts/08/id'},
    {'name': 'Yahoo', 'url': 'https://me.yahoo.com'},
    {'name': 'AOL', 'url': 'https://openid.aol.com/<username>'},
    {'name': 'Flickr', 'url': 'https://www.google.com/accounts/08/id'},
    {'name': 'MyOpenID', 'url': 'https://www.myopenid.com'}]

SQLALCHEMY_DATABASE_URI = 'sqlite:///' + os.path.join(basedir, 'CRUDapp.db')
SQLALCHEMY_MIGRATE_REPO = os.path.join(basedir, 'db_repository')
# Setting this to suppress FSADeprecationWarning
SQLALCHEMY_TRACK_MODIFICATIONS = False
