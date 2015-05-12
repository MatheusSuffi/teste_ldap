# -*- coding: utf-8 -*-

#função de login
def login():
    return auth.login()
#função index

@auth.requires_login()
def index():

    resultado = []
    print resultado
    for item in results_ldap:
        if item != {}:
            resultado += [item]
            print resultado
    return response.render('principal/index.html',resultado=resultado)

#funçao logout
def logout():
    return auth.logout()

