def get_default_context(request, menu_item=''):
    c = {}
    c['user'] = request.user
    if menu_item:
        c[menu_item] = 'menu-selected'
    return c
