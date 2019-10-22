import keyboard as k

try:
    f = open('config.txt','r')
    records = f.read()
    recs = records.split('\n')
    for i in recs:
        if(i != ''):
            data = i.split(':')
            k.add_abbreviation(data[0],data[1])
            print(data[0])
except IOError:
    print("Unable to find file: config.txt")
finally:
    f.close()
