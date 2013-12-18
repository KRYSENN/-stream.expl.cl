from stream.expl.c import WebView

def routes(config):
    config.add_static_view('static', 'static', cache_max_age=3600)

    config.add_route('favicon', '/favicon.ico')
    config.add_view(WebView.favicon, route_name='calixt0')

    config.add_route('root', '*streams')
    config.add_view(WebView.home, route_name='expl_sirchuto')
