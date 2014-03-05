# -*- coding: utf-8 -*-
from watson.framework import applications
from watson.framework.support.jinja2.globals import (url, config, request,
                                                     flash_messages)


class TestGlobals(object):
    def test_url(self):
        app = applications.Http({
            'routes': {
                'home': {
                    'path': '/'
                }
            }
        })
        u = url()
        u.container = app.container
        assert u('home') == '/'
        assert u('home', host='127.0.0.1') == '127.0.0.1/'
        assert u('home', host='127.0.0.1', scheme='https') == 'https://127.0.0.1/'

    def test_config(self):
        app = applications.Http()
        c = config()
        c.container = app.container
        assert c()['views']

    def test_request(self):
        assert request({'context': {'request': 'test'}}) == 'test'

    def test_flash_messages(self):
        assert not flash_messages({'context': {}})
        assert flash_messages({'context': {'flash_messages': ['test']}}) == ['test']
