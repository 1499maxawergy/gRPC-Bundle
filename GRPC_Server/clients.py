client_list = [
    {
        'username': 'Example404',
        'password': '12345'
    }
]

def finder(username:str , password:str):
    index = 0
    for element in client_list:
        if element['username'] == username and element['password'] == password:
            return index
        index+=1
    return -1

def updater(old_username:str, old_password:str, new_username:str, new_password:str):
    index = finder(username=old_username, password=old_password)
    if index == -1:
        return False
    else:
        client_list[index]['username'] = new_username
        client_list[index]['password'] = new_password
        return True

def deleter(username:str , password:str):
    index = finder(username=username, password=password)
    if index == -1:
        return False
    else:
        client_list.pop(index)
        return True

def adder(username:str , password:str):
    for element in client_list:
        if element['username'] == username:
            return False
    client_list.append({
        'username': username,
        'password': password
    })
    return True