django-subdomainer
=================

####Claim: Better than django-subdomains.
####Reality: A lower-level implementation of django-subdomains

##Installation instructions
:Add the 'custom_django_modules' folder to 
: Add the SUBDOMAIN_URLCONFS dictionary with the following syntax to your settings.py file

SUBDOMAIN_URLCONFS = {
   '*' : 'my_application.urls',
   'www' : 'my_application.urls',
   'api' : 'api.urls'
 }

The dictionary entries are in the format of 'subdomain':'project url handler'. In the above example, 3 subdomains are handled, directing to 2 different projects: my_application and api.
: Capiche?

I'll be working on it whenever I come back to a project that needs better subdomain handling. Let me know if there's any issues.
