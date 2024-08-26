import get_os
import find_chrome_version as fcv
import request_get as rget
import chrome_drivers as cd

def driverFinder():
    dict_driver_matcher = {}
    plataform_os = get_os.get_user_os()
    latest_driver = rget.get_uri_strip("https://chromedriver.storage.googleapis.com/LATEST_RELEASE")
    if plataform_os != None:
        chrome_version = fcv.define_chrome_version(plataform_os)
        if chrome_version >= latest_driver:
            dict_driver_matcher["user_os"] = plataform_os
            dict_driver_matcher["chrome_version"] = latest_driver
            return dict_driver_matcher
        else:
            dict_driver_matcher["user_os"] = plataform_os
            if chrome_version in cd.driver_versions():
                dict_driver_matcher["chrome_version"] = chrome_version
            return dict_driver_matcher
                       
    else:
        raise "Os não listado"
    
driverFinder()