import re


def email_parses(email):
     try:
          email_parse = re.compile(r'((?:\w?\.?-?)+)@((?:\w?-?)+\.\w+)')
          email_parsed = email_parse.findall(email)[0]
          dicti = {
               'username': email_parsed[0],
               'domain': email_parsed[1]
          }
          return dicti
     except:
          raise ValueError


user_email = 'suport@geekbrains.ru'
print(email_parses(user_email))
