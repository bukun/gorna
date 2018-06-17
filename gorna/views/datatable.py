from pyramid.view import view_config
from .tools import load_excel


@view_config(route_name='datable', renderer='../templates/datable.jinja2')
def my_view(request):
    print('=' * 40)
    print(request.params)

    sig0 = request.matchdict['sig0']
    sig1 = request.matchdict['sig1']

    file_path = './meta_xlsx/{sig0}/{sig1}'.format(sig0=sig0, sig1=sig1)
    print(file_path)

    data = load_excel(file_path)

    return data

