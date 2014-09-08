#! /usr/bin/env python
# -*- coding: utf-8 -*-

import os
import sys
import yaml

if __name__ == '__main__':
    if len(sys.argv) < 3:
        print >> sys.stderr, 'Usage: %s <input.yml> <output.png>' % sys.argv[0].split(os.sep)[-1]
        sys.exit(1)
