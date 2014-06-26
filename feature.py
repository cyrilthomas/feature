# A feature decorator
import functools
FEATURE_CONFIG = {}

class FeatureSetupError(Exception): pass

def feature_setup(config, update=False):
    '''
    Expects a file name with JSON formatted contents
    {
        "DEFAULT": {
            "active": true,
            "doc": "The default active feature"
        }
    }

    Or a pure python dictonary
    {
        'DEFAULT': {
            'active': True,
            'doc': "The default active feature"
        },

        'experimental': {
            'active': True if (datetime.date.today() - datetime.date(2014,06,14)).days >= 0 else False,
            'doc': "Beta program"
        }
    }
    '''
    global FEATURE_CONFIG
    _config = config
    if not isinstance(config, dict):
        import json
        with open(config) as f:
            _config = json.load(f)
    
    if update:
        FEATURE_CONFIG.update(_config)
    else:
        FEATURE_CONFIG = _config

def is_feature_active(feat):
    status = True \
        if isinstance(FEATURE_CONFIG.get(feat), dict) \
            and FEATURE_CONFIG.get(feat).get('active') \
        else False
    return status

def is_feature_deactive(*args, **kwargs):
    return not is_feature_active(*args, **kwargs)

def feature_with(feat):
    def feature_wrapper(func):
        @functools.wraps(func)
        def feature(*args, **kwargs):
            if not FEATURE_CONFIG:
                raise FeatureSetupError
            func_return = None
            if is_feature_active(feat):
                func_return = func(*args, **kwargs)
            return func_return
        return feature
    return feature_wrapper