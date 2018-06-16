def includeme(config):
    config.add_static_view('static', 'static', cache_max_age=3600)
    config.add_route('home', '/')
    config.add_route('datable', '/datable/{sig0}/{sig1}')
    config.add_route('hello', '/hello')
    config.add_route('visual', '/visual')


