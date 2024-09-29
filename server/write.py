def write_data(bin,txt):#rcv_data and decode data
    with open('myfile.bin', 'ab') as f1, open('myfile.txt', 'a', encoding='utf-8') as f:
        f1.write(bin)#write myfile.bin
        f.write(txt)#write myfile.txt