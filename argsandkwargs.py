'''def shege( level,*different):
    
    print('the type of shege you want:' + str(level))
    for diff in different:
        print ( '@' +diff)

    
    

shege(14,'promax')
shege(15,'normal','chill',)
'''

def album(fname,last,**artistinfo):
    profile={}
    profile['name']=fname
    profile['lname']=last
    for key,value in artistinfo.items():
        profile[key]=value
        return profile
f=album('Dreyys', 'Slime',
 stagename='princeton',
 genre='trap')
print(f)
    