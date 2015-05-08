# -*- coding: utf-8 -*-

#função de login
def login():
    return auth.login()
#função index
@auth.requires_login()
def index():
    resultado = []
    for item in results_ldap:
        if item != {}:
            resultado += [item]
    return response.render('principal/index.html',resultado=resultado)

def logout():
    return auth.logout()

