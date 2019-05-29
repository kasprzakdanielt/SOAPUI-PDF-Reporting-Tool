# SOAPUI PDF Reporting Tool


It started as a simple project for my engineer's degree. Everything was done as fast as possible and needs a proper cleanup, that's why it is so messy.

It should work when configured properly(config.cfg). 
I included a sample SOAPUI project "CountryInfoService-soapui-project.xml"(wsdl service is not working right now sadly, dunno if it will come up again) and "numberconversion-soapui-project".

First version is available here: [SOAPUI PDF Reporting Tool](https://github.com/kasprzakdanielt/SOAPUI-PDF-Reporting-Tool/releases)


## Getting Started

To generate a report you can ask SOAPUI to produce it through the TestRunner you can launch testRunner by right-clicking on the Test suite test case or the entire project you want to run. These reports are generated in an XML format and are not presentable.

My 'tool' was designed as a substitute for pdf report generation that is available in SOAPUI Pro version.
Basic reports for functional tests are working.
Example report:

![firstpage](https://i.imgur.com/jksqk1X.png)

![secondpage](https://i.imgur.com/gWFM4Wi.png)

![thirdpage](https://i.imgur.com/embilTZ.png)

## Known problems

If you are getting errors like 
```
11:06:57,562 INFO  [DefaultSoapUICore] initialized soapui-settings from [C:\Users\Daniel\soapui-settings.xml]
11:06:59,144 INFO  [PluginManager] Adding plugin from [C:\Users\Daniel\.soapuios\plugins\ready-mqtt-plugin-dist.jar]
11:06:59,144 INFO  [PluginManager] Adding plugin from [C:\Users\Daniel\.soapuios\plugins\soapui-swagger-plugin-2.2-dist.jar]
11:06:59,967 ERROR [SoapUI] An error occurred [com.eviware.soapui.plugins.auto.factories.AutoImportMethodFactory], see error log for details
11:06:59,993 ERROR [SoapUI] An error occurred [com.eviware.soapui.plugins.auto.factories.AutoDiscoveryMethodFactory], see error log for details
11:07:00,009 INFO  [PluginManager] Adding plugin from [C:\Users\Daniel\.soapuios\plugins\ready-uxm-plugin-1.0.1-dist.jar]
11:07:00,127 ERROR [SoapUI] An error occurred [com.eviware.soapui.plugins.auto.factories.AutoImportMethodFactory], see error log for details
11:07:00,138 ERROR [SoapUI] An error occurred [com.eviware.soapui.plugins.auto.factories.AutoDiscoveryMethodFactory], see error log for details
11:07:00,185 INFO  [PluginManager] Adding plugin from [C:\Users\Daniel\.soapuios\plugins\readyapi-postman-1.0.1.jar]
11:07:00,902 ERROR [SoapUI] An error occurred [com.eviware.soapui.plugins.auto.factories.AutoImportMethodFactory], see error log for details
11:07:00,913 ERROR [SoapUI] An error occurred [com.eviware.soapui.plugins.auto.factories.AutoDiscoveryMethodFactory], see error log for details
11:07:00,956 ERROR [SoapUI] An error occurred [com.eviware.soapui.plugins.auto.factories.AutoImportMethodFactory], see error log for details
11:07:00,969 ERROR [SoapUI] An error occurred [com.eviware.soapui.plugins.auto.factories.AutoDiscoveryMethodFactory], see error log for details
11:07:00,981 INFO  [PluginManager] Adding plugin from [C:\Users\Daniel\.soapuios\plugins\readyapi-swaggerhub-plugin-1.0.jar]
11:07:01,479 ERROR [SoapUI] An error occurred [com.eviware.soapui.plugins.auto.factories.AutoImportMethodFactory], see error log for details
11:07:01,491 ERROR [SoapUI] An error occurred [com.eviware.soapui.plugins.auto.factories.AutoDiscoveryMethodFactory], see error log for details
```
Delete that plugins folder(in my case "C:\Users\Daniel\.soapuios\plugins").


### Customising 

If you want your pdf report to look different just change it in "Html_files\html.html".


### Prerequisites

SOAPUI Open Source 
https://www.soapui.org/downloads/soapui.html


## Issues & Questions
If you have any questions or issues:
[Add a ticket here](https://github.com/kasprzakdanielt/SOAPUI-PDF-Reporting-Tool/issues)
or 
[Email me](mailto:kasprzak.daniel.kontakt@gmail.com)
