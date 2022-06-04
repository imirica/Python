#fixed sample code from:
#https://docs.microsoft.com/en-us/microsoft-edge/webdriver-chromium/ie-mode?tabs=python#known-limitations

from selenium import webdriver

ie_options = webdriver.IeOptions()
ie_options.add_additional_option("ie.edgechromium", True)
ie_options.add_additional_option("ie.edgepath",'C:\Program Files (x86)\Microsoft\Edge\Application\msedge.exe')

driver = webdriver.Ie('C:\\IEDriverServer\\IEDriverServer.exe',options=ie_options)
driver.get("http://www.bing.com")
