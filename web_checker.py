import time
from selenium import webdriver
from webdriver_manager.firefox import GeckoDriverManager

'''
    Web Checker class
'''


class web_checker():
    def __init__(self):
        """
        @Definition: Initializes a web checker object
        @Preconditions: NONE
        @Postconditions: A web_checker object is instantiated with a webdriver
        @:arg None
        @:return None
        @algorithm
            Tries to:
            Initialize an instance of firefox without a header
            Catches the exception if the object hasn't been initialized
            Variable @____initialized__ determines whether the object has been properly initialized so that no method is used.
        """
        self.__initialized__ = ''
        try:
            driver2 = webdriver.FirefoxOptions()
            driver2.add_argument('--headless')
            self.driver = webdriver.Firefox(executable_path=GeckoDriverManager().install(), options=driver2)
        except:
            self.__initialized__ = "Problem while initializing the driver\n Check internet Connection"

    def __enter__(self):
        """
        @Definition: Enables the class to be used as a context manager
        @Preconditions: NONE
        @Postconditions: A webdriver object is instantiated as a context manager.
        @:arg None
        @:return None
        :return: self
        """
        return self

    def __process_check__(self):
        """
        @Definition: Checks that the web_checker object has been instantiated
        @Preconditions: NONE
        @Postconditions: NONE
        @:arg None
        @:return None
        @algorithm
            If the variable initialized is non-zero then it hasn't been able to create webdriver object.
        :return:
        """
        if self.__initialized__:print(self.__initialized__); exit()
        else: pass

    def check_password_data_base(self, password: str):
        """
        @Definition: Checks the given password with a data breach database
        @Preconditions: The web_checker object must be instantiated
        @Postconditions: NONE
        @:return None
        @algorithm
            checks whether the object has been instantiated properly
            Get a GET-request from site https://haveibeenpwned.com/Passwords to determine whether the password has been found in a data breach
            Enters string password in website and gets its response.
            prints out the final result.
        :param password:
        :return string with the results of check
        """
        self.__process_check__()
        self.driver.get("https://haveibeenpwned.com/Passwords")
        (self.driver.find_element("id", "Password")).send_keys(password)
        (self.driver.find_element("id", "searchPwnedPasswords")).click()
        time.sleep(5)
        response = self.driver.find_element("xpath", '/html/body/div[4]/div/div/div/div[1]').text
        # print(len(response), response)
        return "The password has been found in a breached database" if response else ("the password has not been "
                                                                                      "found in a data breach")

    def check_cracking_time(self, password: str):
        """
        @Definition: Checks how long it would take for the given password to be cracked
        @Preconditions: NONE
        @Postconditions: The web_checker object must be instantiated
        @:arg None
        @:return None
        @algorithm
            checks whether the object has been instantiated properly
            Get a GET-request from site https://www.passwordmonster.com/ to determine how long it'd take to crack the password
            Enters string password in website and gets its response.
            prints out the final result.
        :param password:
        :return: string with the results of check
        """
        self.__process_check__()
        self.driver.get("https://www.passwordmonster.com/")
        element = self.driver.find_element("id", "lgd_out_pg_pass")
        element.send_keys(password)
        time.sleep(2)
        search = self.driver.find_element("id", "first_estimate")
        return f'It would take {search.text} to decipher your password using raw computing power'

    def __exit__(self, exc_type, exc_val, exc_tb):
        """
        @Definition: exits from its context manager state
        @Preconditions: NONE
        @Postconditions: The web_checker object must be instantiated
        @:arg None
        @:return None
        @algorithm
            Closes its webdriver
        :param exc_type:
        :param exc_val:
        :param exc_tb:
        :return:
        """
        self.driver.close()

    def exit(self):
        """
        @Definition: closes its driver interface
        @Preconditions: NONE
        @Postconditions: The web_checker object must be instantiated
        @:arg None
        @:return None
        @algorithm
            Closes its webdriver
        :return:
        """
        self.driver.close()


def main():
    """
        Main program that tests class functionality
    :return:
    """
    # ##Normal use of the class
    # driver = web_checker()
    # print(driver.check_password_data_base("screwyounathan"))
    # print(driver.check_cracking_time("screwyounathan"))
    # driver.exit()

    ## As context manager
    with web_checker() as webCheck:
        print(webCheck.check_password_data_base("Mypassword"))
        print(webCheck.check_cracking_time("password"))


if __name__ == "__main__":
    main()
