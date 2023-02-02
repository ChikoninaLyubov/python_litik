import calculator as cc
import view as vc

def start():
  string = vc.menu_calculator()
  my_list = cc.split_string(string)
  vc.otvet(cc.calculator(my_list))