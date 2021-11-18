import json
def check_account_credentials(email,password,file_name):
  valid = False
  function = None 
  try:
    with open(file_name,'r') as f:
      datas = json.load(f)
      for data in datas:
        if data['email'] == email and data['password'] == password:
          valid = True
          function = data['role']
          break
  except:
    print('Error occured.')
  finally:
    f.close()
    return [valid,function]

