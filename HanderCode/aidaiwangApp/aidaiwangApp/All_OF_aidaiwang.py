# -*- coding: utf-8 -*-

# import Band_BankCard_from_aidaiwangApp
# import BuyObject_from_aidaiwangApp
# import ChangePassword_from_aidaiwangApp
# import Change_BankCard_from_aidaiwangApp
# import Deposit_from_aidaiwangApp
import Login_aidaiwangApp
# import RealName_Auth_from_aidaiwangApp
# import Recharge_from_aidaiwangApp
import Register_aidaiwangApp
import LogOut_aidiawangApp

def test_all_of_aidaiwangApp(filename):
    print(u'selected all case')
    Register_aidaiwangApp.start_to_register(filename)
    Login_aidaiwangApp.start_to_login(filename)
    # RealName_Auth_from_aidaiwangApp.start_to_realnameauth()
    # Band_BankCard_from_aidaiwangApp.start_to_band_bankcard()
    # Recharge_from_aidaiwangApp.start_to_recharge()
    # BuyObject_from_aidaiwangApp.start_to_buyobject()
    # Deposit_from_aidaiwangApp.start_to_deposit()
    # Change_BankCard_from_aidaiwangApp.start_to_changebankcard()
    # ChangePassword_from_aidaiwangApp.start_to_changepassword()

    LogOut_aidiawangApp.start_to_logout()