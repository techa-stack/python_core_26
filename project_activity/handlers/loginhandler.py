from bl.loginbl import LoginBL
class LoginHandler:
    def handle_login(username, password):
        print("Into the login handler")
        print("Invoking login BL for further checks")
        return LoginBL.getLoginDetailsBL(username, password)