"""
    loading configuration over paster *.ini file
"""
from grokcore.startup import startup
from ConfigParser import ConfigParser

from raptus.mailcone.app import config



def raw_configurator(ini_file, local_conf_key='app:mailcone', here=__file__, zope_conf=''):
    configparser = ConfigParser()
    configparser.read(ini_file)
    configparser.defaults().update(dict(here=here))
    configurator(dict(here=here,
                      __file__=ini_file,
                      zope_conf=zope_conf),
                **dict(configparser.items(local_conf_key)))


def configurator(global_conf, **local_conf):
    config.here = global_conf.get('here')
    config.ini_file = global_conf.get('__file__')
    config.zope_conf = global_conf.get('zope_conf')
    
    configparser = ConfigParser()
    configparser.read(config.ini_file)
    
    # building 2D dicts
    parsed = dict()
    for key, value in local_conf.iteritems():
        if configparser.has_section(value):
            parsed[key] = dict([(o, configparser.get(value, o),) for o in configparser.options(value)
                                if not o in configparser.defaults().keys()])
    config.local_configuration = local_conf
    config.local_configuration.update(parsed)
    
    
def application_factory(global_conf, **local_conf):
    configurator(global_conf, **local_conf)
    return application_factory(global_conf, **local_conf)


def debug_application_factory(global_conf, **local_conf):
    configurator(global_conf, **local_conf)
    return startup.debug_application_factory(global_conf, **local_conf)
