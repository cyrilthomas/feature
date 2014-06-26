from feature import *

@feature_with("my_function")
def my_function():
    print "Hello feature"

@feature_with("my_function1")
def my_function1():
    print "Hello feature1"

@feature_with("STANDARD")
def my_function2():
    print "Hello feature2"

@feature_with("my_function3")
def my_function3():
    print "Hello feature3"

@feature_with("my_function4")
def my_function4():
    print "Hello feature4"

@feature_with("STANDARD")
def my_default():
    print "Hello DEFAULT"

@feature_with("experimental")
def experimental():
    '''Experimental function'''
    return [1,2,3]

def main():
    feature_setup('feature_config.json')
    my_function()
    feature_setup({'my_function1': {'active': True}}, update=True)
    my_function1()
    my_function2()
    feature_setup({'my_function3': {'active': True}}, update=True)
    my_function3()
    # feature_setup('feature_config.json')
    my_function4()
    my_default()
    import datetime
    feature_setup({'experimental': {
        'active': bool(1) if (datetime.date.today() - datetime.date(2014,06,14)).days >= 0 else bool(0),
        'doc': "Beta program"
    }})
    print experimental, experimental.__doc__, experimental()

    print is_feature_active('STANDARD')
    print is_feature_deactive('UNKNOWN')

if __name__ == '__main__':
    main()