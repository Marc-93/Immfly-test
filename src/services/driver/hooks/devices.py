ANDROID_CAPS = {'platformName': 'Android',
                'automationName': 'UiAutomator2',
                'appPackage': 'XXXXX',
                'appActivity': 'XXXXX',
                'autoGrantPermissions': 'true'}


def iphone_caps(app_path, device):
    """Sets the iphone caps according app_path and device.

    :param app_path: app where .app is installed
    :param device: name of device
    :return: iphone caps
    """
    return {"platformName": "iOS",
            "automationName": "XCUITest",
            "deviceName": device,
            "app": app_path}


def get_capabilities(desired_caps):
    """Gets the desired caps according platform selected for test.

    :param desired_caps: desired params for android or iOS
    :return: desired final capabilities
    """
    if desired_caps['platform'] == 'android':
        return ANDROID_CAPS

    if desired_caps['platform'] == 'ios':
        return iphone_caps(desired_caps['app_path'],
                           desired_caps['device'])
