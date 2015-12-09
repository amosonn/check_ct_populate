#!/usr/bin/env python
from check_ct_populate import wsgi

from myapp.models import Wrapper

print("{!s:^20} | {!s:^20} | {!s:^20}".format("Wrapper pk","Object","Object pk"))
print("{!s:^20} | {!s:^20} | {!s:^20}".format(*(("-"*20,)*3)))
for w in Wrapper.objects.all():
    print("{!s:^20} | {!s:^20} | {!s:^20}".format(w.pk,w.wrapped,w.wrapped.pk))
print("{!s:^20} | {!s:^20} | {!s:^20}".format(*(("-"*20,)*3)))
