import xmlrpc.client
url = "http://localhost:5555"
db = 'jq'
username = 'admin'
password = 'admin'


common = xmlrpc.client.ServerProxy('{}/xmlrpc/2/common'.format(url))
a = common.version()

uid = common.authenticate(db, username, password, {})
models = xmlrpc.client.ServerProxy('{}/xmlrpc/2/object'.format(url))

b = models.execute_kw(db, uid, password,
                      'res.partner', 'search',
                      [[['is_company', '=', True]]])

c = models.execute_kw(db, uid, password,
                      'res.partner', 'search_count',
                      [[]])
d = models.execute_kw(db, uid, password, 'res.partner', 'search_read', [[]], {'fields': ['name'], 'limit': 2})

new = models.execute_kw(db, uid, password, 'res.partner', 'create', [{
    'name': "XML RPC",
}])

create_model = models.execute_kw(db, uid, password, 'ir.model', 'create', [{
    'name': "x_xml_model",
    'model': "x_.xml.xml",
}])
print(create_model)