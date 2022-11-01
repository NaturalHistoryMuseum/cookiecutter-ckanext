#!/usr/bin/env python
# encoding: utf-8
#
# This file is part of {{ cookiecutter.slug }}
# Created by the Natural History Museum in London, UK

from ckan.plugins import SingletonPlugin, implements, interfaces, toolkit


class {{ cookiecutter.class }}Plugin(SingletonPlugin):
    '''
    {{ cookiecutter.summary }}
    '''

    implements(interfaces.IConfigurer, inherit=True)

    ## IConfigurer
    def update_config(self, config):
        '''

        :param config:

        '''
        toolkit.add_template_directory(config, u'theme/templates')
        toolkit.add_public_directory(config, u'theme/public')
        toolkit.add_resource(u'theme/assets', u'{{ cookiecutter.slug }}')
