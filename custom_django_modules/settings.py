## Just add the following to your projects settings.py file

SUBDOMAIN_URLCONFS = {
  '*' : 'www_futureequation_com.urls',
  'www' : 'www_futureequation_com.urls',
  'dashboard' : 'dashboard.urls'
}
