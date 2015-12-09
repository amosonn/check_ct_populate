#!/usr/bin/env python
from check_ct_populate import wsgi

from myapp.models import Wrapper, First

o1 = First.objects.create()
w = Wrapper.objects.create(wrapped=o1)
