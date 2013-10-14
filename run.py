#!/usr/bin/env python

from folioweb import proj
from folio.server import run

proj.config['DEBUG'] = True
run(proj)
