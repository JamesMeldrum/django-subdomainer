## Just add the following to your projects settings.py file

SUBDOMAIN_URLCONFS = {
  '*' : 'my_application.urls',
  'www' : 'my_application.urls',
  'api' : 'api.urls'
}
