#!/usr/bin/env python

try:
        import sys
        import random
        import math
        import os
        import getopt
        import pygame
        from socket import *
        from pygame.locals import *
except ImportError, err:
        print "couldn't load module. %s" % (err)
        sys.exit(2)

