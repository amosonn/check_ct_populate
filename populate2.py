#!/usr/bin/env python
from check_ct_populate import wsgi

from myapp.models import Wrapper, Second

o2 = Second.objects.create()
w = Wrapper.objects.create(wrapped=o2)
