# import xmlrpc.client
from athsurveyapp.models import Branch, db


def save_branch(name, address):
    new_branch = Branch(name, address)
    db.session.add(new_branch)
    db.commit()


# def get_branches():
#     url = "http://192.168.10.17:8059"
#     db = "Final_AlraisEnterprises"
#     username = "donato"
#     password = "...donato09@"

#     common = xmlrpc.client.ServerProxy('{}/xmlrpc/2/common'.format(url))
#     print(common.version())

#     uid = common.authenticate(db, username, password, {})

#     models = xmlrpc.client.ServerProxy('{}/xmlrpc/2/object'.format(url))
#     partners = models.execute_kw(db, uid, password,
#                                  'res.company', 'search_read', [],
#                                  {'fields': ['name']})

#     return partners


# def get_employees(company_id):

#     url = "http://192.168.10.17:8059"
#     db = "Final_AlraisEnterprises"
#     username = "donato"
#     password = "...donato09@"

#     common = xmlrpc.client.ServerProxy('{}/xmlrpc/2/common'.format(url))
#     print(common.version())

#     uid = common.authenticate(db, username, password, {})

#     models = xmlrpc.client.ServerProxy('{}/xmlrpc/2/object'.format(url))
#     employees = models.execute_kw(db, uid, password,
#                                   'hr.employee', 'search_read', [
#                                       [['company_id', '=', int(company_id)]]],
#                                   {'fields': ['name']})

#     return employees
