import json

f = open('demo.json', 'r')
json_dict = json.load(f)

newfile={}
for key in json_dict:
    value={}
    value['title'] = json_dict[key]['title']
    authors = json_dict[key]['authors']
    affils = json_dict[key]['affils']
    txt = ''
    for i in range(len(authors)):
        if not i==(len(authors)-1):
            txt+=authors[i]+'('+affils[i]+'),'
        else:
            txt+=authors[i]+'('+affils[i]+')'
    value['authors'] = txt
    newfile[key] = value

fnew = open('./demoweb.json', 'w')
json.dump(newfile,fnew,ensure_ascii=False,indent=4)