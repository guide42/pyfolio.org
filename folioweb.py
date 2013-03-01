"""
    Folio website.
"""

from folio import Folio

proj = Folio(__name__, extensions=[],
             jinja_extensions=['jinja2_highlight.HighlightExtension'])

def debug():
    import logging
    proj.logger.addHandler(logging.StreamHandler())
    proj.logger.setLevel(logging.DEBUG)

if __name__ == '__main__':
    debug()
    proj.build()
