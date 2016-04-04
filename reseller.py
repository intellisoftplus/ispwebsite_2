# Provision a customer from end-to-end
import httplib2
from oauth2client.client import SignedJwtAssertionCredentials

# establish the list of scopes.
OAUTH2_SCOPES = [
  'https://www.googleapis.com/auth/apps.order',
  'https://www.googleapis.com/auth/siteverification',
  'https://www.googleapis.com/auth/admin.directory.user'
]

# replace with your own values.
SERVICE_ACCOUNT_EMAIL = '404608567968-ciedk421m6pq03ikp3vg90a83dqhj6vs@developer.gserviceaccount.com'
PRIVATE_KEY_FILE = 'privatekey.p12'
RESELLER_ADMINISTRATOR_USER = 'superadmin@reseller.mycompany.com'

# create an HTTP client
http = httplib2.Http()

# read private key.
f = file(PRIVATE_KEY_FILE)
key = f.read()
f.close()

# establish the credentials.
credentials = SignedJwtAssertionCredentials(
  service_account_name=SERVICE_ACCOUNT_EMAIL,
  private_key=key,
  scope=' '.join(SCOPES),
  sub=RESELLER_ADMINISTRATOR_USER)

# authorize
credentials.authorize(http)



#Create a customer with the Reseller API
from apiclient.discovery import build
from apiclient.http import HttpError

# utilize the same http object constructed earlier.
service = build(serviceName='reseller',
                version='v1',
                http=http)

# default vault of false.
customer_exists = False

try:
  customer_record = service.customers().get(customerId='acme.com').execute()
  # a customer record was returned, customer exists
  customer_exists = True
except HttpError, ex:
  if int(e.resp['status']) == 404:
    # customer record not found
    customer_exists = False
  else:
    # unknown error!
    raise


# Create a customer record in Google Apps
from apiclient.discovery import build
from apiclient.http import HttpError

# utilize the same http object constructed earlier.
service = build(serviceName='reseller',
                version='v1',
                http=http)

customer_record = service.customers().insert(body={
  'customerDomain': 'acme.com',
  'alternateEmail': 'marty.mcfly@gmail.com',
  'phoneNumber': '212-565-0000',
  'postalAddress': {
    'contactName': 'Marty McFly',
    'organizationName': 'Acme Corp',
    'postalCode': '10009',
    'countryCode': 'US',
  }
}).execute()



