original = open('botnet_dataset/capture20110818.binetflow', 'rb')
botnet = open('botnet_dataset/botnet_dataset.csv' ,'wb')
non_botnet = open('botnet_dataset/non_botnet.csv', 'wb')

for line in original.readlines():
    if 'StartTime' in line:
        botnet.write(line)
        non_botnet.write(line)

    if 'Botnet' in line:
        botnet.write(line)
    else:
        non_botnet.write(line)

