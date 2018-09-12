original = 'botnet_dataset/non_botnet.csv'

nuevo = 'botnet_dataset/non_botnet_bool.csv'

fo = open(original, 'rb')
fn = open(nuevo, 'wb')

for line in fo.readlines():                     
    sections = line.split(',')   
    if 'Botnet' in line:
        sections[len(sections)-1] = 1
    else:
        sections[len(sections)-1] = 0
    line = ""
    for index in range(0, len(sections)):
        if index == len(sections)-1:
            line += str(sections[index]) + '\n'
        else:
            line += str(sections[index]) + ','
    fn.write(line)

