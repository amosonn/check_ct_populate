#!/usr/bin/env python
from check_ct_populate import wsgi

from django.contrib.contenttypes.models import ContentType

print("{!s:^20} | {!s:^20} | {!s:^20}".format("ContentType pk","app_label","model"))
print("{!s:^20} | {!s:^20} | {!s:^20}".format(*(("-"*20,)*3)))
for ct in ContentType.objects.all():
    print("{!s:^20} | {!s:^20} | {!s:^20}".format(ct.pk,ct.app_label,ct.model))
print("{!s:^20} | {!s:^20} | {!s:^20}".format(*(("-"*20,)*3)))
