MODULES = ['backend', 'main', 'recovery']

DEPS =  [
    (['any'],
     [
    	('app', 'Samba', 'smbd'),
     ])
]

NAME = 'Samba'
PLATFORMS = ['any']
DESCRIPTION = 'Control Samba server'
VERSION = '0.1'
AUTHOR = 'Ajenti team'
HOMEPAGE = 'http://ajenti.org'
