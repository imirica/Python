//fixed sample code from:
//https://docs.microsoft.com/en-us/microsoft-edge/webdriver-chromium/ie-mode?tabs=java#known-limitations

import org.openqa.selenium.WebDriver;
import org.openqa.selenium.ie.InternetExplorerDriver;
import org.openqa.selenium.ie.InternetExplorerOptions;

public class IEDriverSample {
    public static void main(String[] args) {
    
        InternetExplorerOptions ieOptions = new InternetExplorerOptions();
        ieOptions.attachToEdgeChrome();
        ieOptions.withEdgeExecutablePath("C:\\Program Files (x86)\\Microsoft\\Edge\\Application\\msedge.exe");
        System.setProperty("webdriver.ie.driver", "C:\\IEDriverServer\\IEDriverServer.exe");
        
        WebDriver driver = new InternetExplorerDriver(ieOptions);
        driver.get("http://www.bing.com");
    }
}
