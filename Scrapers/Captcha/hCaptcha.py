# -*- coding: utf-8 -*-

import requests
from twocaptcha import TwoCaptcha


twoCaptcha =TwoCaptcha('xxa9dxxx1fxxx11caxxx3dxxx')  # Your API key


captcha_token = twoCaptcha.hcaptcha(sitekey='xxxxxx-xxxxxx-xxx-xxx',
                                      url='https://www.xxxxxxxxxx.html') # sitekey will be present in data-sitekey attribute

print(captcha_token)


