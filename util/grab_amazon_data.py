from httplib import HTTPConnection
from urlparse import urlparse, urlunparse
from amara import bindery
import amara

def paramunparse(params):
    result = ""
    for k, v in params.iteritems():
        result += k + "=" + v + "&"
    return result.rstrip('&')

AWSAccessKeyId = 'AKIAJZDWZOHWGEYFQBDA'
isbn = '0-3951-7711-1'
# ISBN's are sometimes formatted with hyphens
# The ASIN for books is equal to the ISBN with no hyphens
asin = isbn.replace('-','')
host = 'webservices.amazon.com'
path = '/onca/xml'
params = { 'Service': 'AWSECommerceService',
           'AWSAccessKeyId': AWSAccessKeyId,
           'Operation': 'ItemLookup',
           'MerchantId': 'Featured',
           'IdType': 'ASIN',
           'ResponseGroup': 'Medium',
           'ItemId': asin}

query = urlunparse(('','',path, '', paramunparse(params), ''))
print 'http://'+host+query
conn = HTTPConnection(host)
conn.request('GET',query)
xmlresponse = conn.getresponse().read()
doc = amara.bindery.parse(xmlresponse)
print "Found", len(doc.ItemLookupResponse.Items.Item), "items."
print "Looking at first item"
item = doc.ItemLookupResponse.Items.Item[0]
print "Title:", item.ItemAttributes.Title
print "Authors:",
for author in item.ItemAttributes.Author:
    print author.__str__() + ";",

print
price = item.OfferSummary.LowestNewPrice.Amount #unformatted
print "List Price:", item.ItemAttributes.ListPrice.FormattedPrice
print "Amazon Price:", item.OfferSummary.LowestNewPrice.FormattedPrice