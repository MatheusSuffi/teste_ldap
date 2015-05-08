import ldap
#Adicionar futuramente uma verificação para ldap local e ldap em rede!
#.replace('[','').replace(']','')
l = ldap.initialize("ldap://192.168.100.235")

try:
    l.protocol_version = ldap.VERSION3
    l.set_option(ldap.OPT_REFERRALS, 0)
    bind = l.simple_bind_s("Administrator@forip.local", "Nvnpfa@2012")
    base = "dc=forip, dc=local"
    criteria = "(&(objectClass=user))"
    attributes = ['displayName', 'mobile','facsimileTelephoneNumber','ipPhone']
    result = l.search_s(base, ldap.SCOPE_SUBTREE, criteria, attributes)

    results_ldap = [entry for dn, entry in result if isinstance(entry, dict)]
finally:
    l.unbind()