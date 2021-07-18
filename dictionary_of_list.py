user_fav_lang = {

'Sai':['python','java'],
'Ram':['C','C++','Perl'],
'Balaji':['Linux','Docker','Kubernetes'],

}

for name, languages in user_fav_lang.items():
    print(name +": ")
    for lang in languages:
        print("- " +lang,end="")
        print("\t")