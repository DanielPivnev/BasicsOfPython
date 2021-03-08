with open('cookies.txt', 'r', encoding='utf-8') as f:
     userList = []
     userCount = []
     user = f.readline()
     GreatUser = ''
     while user:
          user = user.split('"')[-2]
          if user not in userList:
               userList.append(user)
               userCount.append(1)
          else:
               userCount[userList.index(user)] += 1
          user = f.readline()
     GreatUser = userCount[0]
     for i in range(1, len(userCount)):
          if userCount[i] > GreatUser:
               GreatUser = userCount[i]
     print(f'The biggest spammer is "{userList[userCount.index(GreatUser)]}" with {GreatUser} spams.')
