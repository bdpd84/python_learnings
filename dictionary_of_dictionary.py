dictionary = {
  
'Hindu': {
  
  'first_name':'Sai',
  'last_name':'Ram',
  'religion':'Hinduism',

},

'Sikh': {
  'first_name':'vai',
  'last_name':'guru',
  'religion':'sikhism',  
}

}

for religion, name in dictionary.items():
    print(religion +":")
    print("\t"+ name['first_name'])
    print("\t"+ name['last_name'])
    print("\t"+ name['religion'])