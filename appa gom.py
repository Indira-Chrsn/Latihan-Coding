dict_mhs = {'field' : [('Nama', "^([a-zA-Z]+([ '-]| ')?[a-zA-Z]+){1,4}$"),
                           ('Email', '^([a-z0-9]+[._]?[a-z0-9]+)+[@]\w+[.]\w{2,3}'),
                           ('Password', '^[a-zA-Z0-9]{8,12}$')],
             'data' : {'113': {'Nama': 'Dummy', 'Email': 'dummy@telU.com', 'Password': '12345678'},
                       '114': {'Nama': 'Joni', 'Email': 'joni@telU.com', 'Password': '12345678'},
                       '115': {'Nama': 'jeje', 'Email': 'jeje@telU.com', 'Password': '12345678'}

                       }           
            }

def print_to_file(dict_mhs):
    '''
    Print data mahasiswa ke dalam file teks. 1 mahasiswa per baris, dan kolomnya adalah sesuai field, pisahkan dengan tab.
    '''
    print('----Fungsi "print_to_file" dijalankan----')
    file = input('Masukkan nama file: ')
    f = open(file, "x")
    f = open(file, 'w')
    f.write("{}\t{}\t{}\t{}\n".format("Nim","Nama","Email","Password"))
    f.close()


    for key, value in dict_mhs['data'].items():
        f = open(file, 'a')
        f.write('{}\t{}\t{}\t{}\n'.format(key, value['Nama'], value['Email'], value['Password']))
        f.close()

    
    """with open(file,'a') as data:
        data.write(str(dict_mhs['data']))"""
    z = print('Penyimpanan berhasil')
    return z

print_to_file(dict_mhs)
