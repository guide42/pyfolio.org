"""
    Folio website.
"""

from folio import Folio

__version__ = '0.3'

proj = Folio(__name__, extensions=['themes'],
             jinja_extensions=['jinja2_highlight.HighlightExtension'])

proj.config.update({
    'THEME': 'folio',
})


@proj.context('*.html')
def version(env):
    return {'version': __version__}


if __name__ == '__main__':
    proj.config['DEBUG'] = True
    proj.build()
