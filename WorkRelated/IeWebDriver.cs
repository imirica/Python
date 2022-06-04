//fixed sample code from:
//https://docs.microsoft.com/en-us/microsoft-edge/webdriver-chromium/ie-mode?tabs=c-sharp#known-limitations

using System;
using OpenQA.Selenium;
using OpenQA.Selenium.IE;

namespace IEDriverSample
{
    class Program
    {
        static void Main(string[] args)
        {
            var ieOptions = new InternetExplorerOptions();
            ieOptions.AttachToEdgeChrome = true;
            //change the path accordingly
            ieOptions.EdgeExecutablePath = "C:/Program Files (x86)/Microsoft/Edge/Application/msedge.exe";

            var driver = new InternetExplorerDriver("C:\\IEDriverServer\\", ieOptions);
            driver.Url = "https://bing.com";

        }
    }
}
