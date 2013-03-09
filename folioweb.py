"""
    Folio website.
"""

from folio import Folio

proj = Folio(__name__, extensions=[],
             jinja_extensions=['jinja2_highlight.HighlightExtension'])

def debug():
    import logging

    # Print DEBUG messages to STDOUT.
    proj.logger.addHandler(logging.StreamHandler())
    proj.logger.setLevel(logging.DEBUG)

    # Change DEBUG config option.
    proj.config['DEBUG'] = True

if __name__ == '__main__':
    debug()
    proj.build()
