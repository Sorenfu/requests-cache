#!/usr/bin/env python
# -*- coding: utf-8 -*-
import requests
import requests_cache

u = 'http://maps.googleapis.com/maps/api/geocode/json?latlng=56.7615984,8.8680764&sensor=false'
cacher = requests_cache.CachedSession(cache_name='geocode',backend='redis',expire_after=60*60*24*10,min_cache_response_size=200)

for i in range(2):
    r = cacher.get(u)
    print r.text
    print r.from_cache

