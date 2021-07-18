users = [
    {
        'last_name' :'Ram',
        'first_name':'Sai',
        'location' :'Bengaluru',
    },

    {
        'last_name':'Datta',
        'first_name':'Balaji',
        'location':'London',
    },
]
for user in users:
    for k, v in user.items():
        print(k + ":" + v)
    print("\n")