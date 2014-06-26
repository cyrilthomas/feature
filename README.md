###Feature toggle

Using simple JSON based configurations

_file: config.json_
```json
{
  "my_feature": {
    "active": true,
    "doc": "The default active feature"
  }
}
```
_file: app.py_
```python
from feature import feature_with, feature_setup

@feature_with('my_feature')
def sum(a,b):
  return a + b

def main():
  feature_setup('config.json')
  sum(2,3)

if __name__ == '__main__':
  main()
```

Or more complex python dictonary configurations

_file: config.py_
```python
import datetime

feat_config = {
  'my_feature': {
    'active': True,
    'doc': "The default active feature"
  },
  
  'experimental': {
    'active': True if (datetime.date.today() - datetime.date(2014,06,14)).days >= 0 else False,
    'doc': "Beta program"
  }
}
```
_file: app.py_
```python
from feature import feature_with, feature_setup
import config

@feature_with('experimental')
def sum(a,b):
  return a + b

def main():
  feature_setup(config.feat_config)
  sum(2,3)

if __name__ == '__main__':
  main()
```
