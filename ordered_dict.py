from collections import OrderedDict

fav_lang = OrderedDict()

fav_lang['Sai']= ['Python','Java']
fav_lang['Ram']= ['C','C++','Perl']
fav_lang['Balaji']=['Linux','Docker','Kubernetes']

for names,languages in fav_lang.items():
    print(names + " :")
    for lang in languages:
        print( "\t"+ "- " +lang)