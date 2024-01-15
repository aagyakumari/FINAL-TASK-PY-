def user_add(pwfile):
    import getpass  
    import codecs  
     

    def add_user(username, real_name, password):
        with open(pwfile, "a") as file:
            file.write(f"{username}:{real_name}:{password}\n")
        print("\nUser Created.\n")  

    # ask user for input until they provide it.
    while True:
        username = input("\nEnter new username: ")
        if username:
            break
    while True:    
        real_name = input("\nEnter real name: ")
        if real_name:
            break
    while True:
        password = getpass.getpass("\nEnter password: ")  
        password = codecs.encode(password, "rot_13")
        if password:
            break
               
    
    # Checking if username already exists 
    with open(pwfile, "r") as file:
        lines = file.readlines()
        for line in lines:
         if (username + ":") in line:
            print("Cannot add. This username already exists.")
            break
        else:
            add_user(username, real_name, password)
            

    
        
