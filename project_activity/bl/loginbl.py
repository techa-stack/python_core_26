
from dao.logindao import LoginDAO 
class LoginBL:
    def getLoginDetailsBL(username, password):
        print("Into Login BL. Invoking DB to get the user details")
        response = LoginDAO.getLoginDeatilsFromDB(username, password)
        print(response)
        return response