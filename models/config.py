# -*- coding: utf-8 -*-
from gluon.storage import Storage
import ldap
config = Storage(
    db=Storage(),
)

# Conexão com o Banco de Dados
if request.is_local:
    config.db.uri = "postgres:pg8000://matheus:123456@localhost/teste_ldap"
else:
    config.db.uri = "postgres:pg8000://forip:yma2578k@127.0.0.1/teste_ldap"
db = DAL(**config.db)

# Importações
from gluon.tools import Auth
from gluon.contrib.login_methods.ldap_auth import ldap_auth
# Login com LDAP

# Configuração Auth
auth = Auth(db, controller="principal",function="login")
auth.settings.create_user_groups=False
auth.settings.actions_disabled=['register','change_password','request_reset_password','retrieve_username','profile']
auth.settings.remember_me_form = False
auth.settings.login_next = URL(a='teste_ldap', c='principal', f='index')
auth.settings.login_methods = [ldap_auth(mode='ad',
   server='192.168.100.235',
   base_dn='dc=forip,dc=local')]

auth.messages.logged_in = 'Bem Vindo'
auth.messages.access_denied = 'Acesso negado! Contate o administrador'
auth.messages.invalid_username = 'Usuario Inválido '
auth.messages.invalid_login = 'Usuario ou Senha Inválidos'
auth.messages.invalid_password = 'Senha Inválida'
auth.messages.login_button = "Entrar"
auth.messages.label_email = 'E-mail'
auth.messages.label_password = 'Password'