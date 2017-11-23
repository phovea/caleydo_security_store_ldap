def create(_):
  def _loop():
    from .ldap import LDAPStore
    store = LDAPStore()
    username = raw_input('username: ')

    while username:
      password = raw_input('password: ')
      user = store.login(username, dict(password=password))
      if user:
        print('OK {u.id} name:{u.name} roles:{u.roles} dn:{u.dn}'.format(u=user))
      else:
        print('ERROR')
      username = raw_input('another username: ')

  return lambda _: _loop
