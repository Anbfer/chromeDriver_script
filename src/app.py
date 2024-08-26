import webbrowser
import time
import driver_finder as df

# Windows: reg query "HKEY_CURRENT_USER\Software\Google\Chrome\BLBeacon" /v version
# linux: google-chrome --version | grep -iE " [0-9]{1,3}.[0-9]{1,3}

teste = df.driverFinder()

api_url = f'https://chromedriver.storage.googleapis.com/{teste["chrome_version"]}/chromedriver_{teste["user_os"]}.zip'

if __name__ == "__main__":
    print("Baixando ChromeDriver: " + teste["chrome_version"])
    time.sleep(2)
    print("\n" + api_url)
    time.sleep(2)
    webbrowser.open(api_url)
    input("\nPressione enter para sair")
    