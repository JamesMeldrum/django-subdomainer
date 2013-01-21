## custom_django_modules.middleware.*

from django.conf import settings

class SubdomainHandler(object):
  """
    Correctly the request to the delegate, based on the subdomain
  """

  def process_request(self, request):
    req_subdomain = request.get_host().split('.')[0]
    if req_subdomain in settings.SUBDOMAIN_URLCONFS.keys():
      request.urlconf = settings.SUBDOMAIN_URLCONFS[req_subdomain]
    elif settings.DEBUG == False:
      request.urlconf = settings.ROOT_URLCONF
    else:
      raise Exception("Subdomain %s not in SUBDOMAIN_URLCONFS in project settings (usually settings.py). This message is only displayed when the settings DEBUG = True" % req_subdomain)
    return None
