listStockProduct = [
    {
        'id_product' : 'AFP123',
        'nama': 'Ayam Frozen Potong',
        'stock_product':20,
        'uom' : 'Kg',
        'exp_date': '21/06/2023',
        'purchase_price_per_uom' :35000
    },
    {
        'id_product' : 'AFU123',
        'nama': 'Ayam Frozen utuh',
        'stock_product':15,
        'uom' : 'Kg',
        'exp_date': '18/06/2023',
        'purchase_price_per_uom' :30000
    },
    {
        'id_product' : 'BDF123',
        'nama': 'Boneless Dada Frozen',
        'stock_product':10,
        'uom' : 'Kg',
        'exp_date': '19/05/2023',
        'purchase_price_per_uom' :40000
    },
    {
        'id_product' : 'BPF123',
        'nama': 'Boneless Paha Frozen',
        'stock_product':23,
        'uom' : 'Kg',
        'exp_date': '13/05/2023',
        'purchase_price_per_uom' :40000
    },
    {
        'id_product' : 'DGS123',
        'nama': 'Daging Giling Sapi',
        'stock_product':7,
        'uom' : 'Kg',
        'exp_date': '20/04/2023',
        'purchase_price_per_uom' :90000
    },
    {
        'id_product' : 'CRF123',
        'nama': 'Cumi Ring Frozen',
        'stock_product':17,
        'uom' : 'Kg',
        'exp_date': '25/05/2023',
        'purchase_price_per_uom' :60000
    },
]

def menampilkanDaftarProduct() : 
    while True:
        subMenu= input ('''
        Submenu Daftar Product
        1. Menampilkan Daftar Product
        2. Menampilkan Product tertentu
        3. kembali ke menu awal
        Silahkan pilih Submenu Daftar Product [1-3] : ''')
        
        if subMenu == '1':
            print ('\n---------------------------------------------------List Daftar Product---------------------------------------------------\n')
            print ('i \t| id_product \t|nama \t\t\t| stock_product \t| Uom \t| exp_date \t| purchase_price_per_uom')
            i=0
            for i in range (len(listStockProduct)) :
                print ('{} \t|     {}\t| {} \t| {} \t\t\t| {} \t| {} \t| {}'.format(i,listStockProduct[i]['id_product'],listStockProduct[i]['nama'],listStockProduct[i]['stock_product'],listStockProduct[i]['uom'],listStockProduct[i]['exp_date'],listStockProduct[i]['purchase_price_per_uom']))
        
        elif subMenu == '2':
            idProduct= str(input('\tMasukkan id_product:')).upper()
            for x in range(len(listStockProduct)):
                if idProduct == listStockProduct[x]['id_product']:
                    y = '\tProduct Tersedia'
                    break
                else:
                    y = '\tProduct Tidak Tersedia'
            print(y)
            if y == '\tProduct Tersedia':
                print('\n---------------------------------------------------Berikut Productnya:---------------------------------------------------\n')
                print ('i \t| id_product \t|nama \t\t\t| stock_product \t| uom \t| exp_date \t| purchase_price_per_uom')
                print('{} \t|     {}\t| {} \t| {} \t\t\t| {} \t| {} \t| {}'.format(x,listStockProduct[x]['id_product'],listStockProduct[x]['nama'],listStockProduct[x]['stock_product'],listStockProduct[x]['uom'],listStockProduct[x]['exp_date'],listStockProduct[x]['purchase_price_per_uom']))
            else:
                break
        elif subMenu == '3':
            break
        else:
            print('\n------------------------------Pilihan Yang Anda Masukkan Salah ------------------------------\n')

def menambahProduct() :
    while True:
        subMenu= input ('''
        Submenu Menambah Product
        1. Menambah Product
        2. kembali ke menu awal
        Silahkan pilih Submenu Menambah Product [1-2] : ''')
        
        if subMenu == '1':
            idProduct = input ('\tMasukkan Id Product : ').upper()
            namaProduct = input ('\tMasukkan Nama Product: ').capitalize()
            stockProduct = int (input ('\tMasukkan Stock Product: '))
            uomProduct = input ('\tMasukkan Uom Product: ').capitalize()
            expProduct = input ('\tMasukkan Expired Date Product (dd/mm/yyyy): ')
            purchasePrice =  int(input ('\tMasukkan Purchase Price Product per Uom: '))
            while True:
                checker =input('\tApakah data akan di simpan? (Y/N): ').upper()
                if checker == 'N':
                    print('\n--------------------------------Data Tidak Di Tambahkan------------------------------\n')
                    break
                elif checker == 'Y':
                    listStockProduct.append({
                        'id_product' : idProduct,
                        'nama': namaProduct,
                        'stock_product': stockProduct,
                        'uom' : uomProduct,
                        'exp_date': expProduct,
                        'purchase_price_per_uom' : purchasePrice})
                    print('\n-----------------------------Data Telah Berhasil Di Tambahkan---------------------------\n')
                    break
                else:
                    print('\n------------------------------Pilihan Yang Anda Masukkan Salah ------------------------------\n')
                       
        elif subMenu == '2':
             break
        else:
            print('\n------------------------------Pilihan Yang Anda Masukkan Salah ------------------------------\n') 
               
def mengupdateInfoProduct() :
    while True:
        subMenu= input ('''
        Submenu Mengupdate Info Product
        1. Mengupdate Info Product
        2. kembali ke menu awal
        Silahkan pilih Submenu Menghapus Product [1-2] : ''')
        if subMenu == '1':
            idProduct= str(input('\tMasukkan id_product Yang Ingin Diupdate: ')).upper()
            for x in range(len(listStockProduct)):
                if idProduct == listStockProduct[x]['id_product']:
                    y = '\tProduct Tersedia'
                    break
                else:
                    y = '\tProduct Tidak Tersedia'
            print(y)
            if y == '\tProduct Tersedia':
                while True:            
                    checker = input('\tingin mengupdate info product? (Y/N): ').upper()
                    if checker == 'N':
                        print('\n ------------------------------Data Product Tidak Di Update------------------------------\n')
                        break
                    elif checker == 'Y':
                            subMenu= input ('\tMasukkan nama Kolom yang ingin di Update: ').lower()
                            if subMenu == 'id_product':
                                    listStockProduct[x]['id_product']=input('\t Masukkan id_product Terbaru: ').upper()
                                    print('\n------------------------------id_product sudah berhasil di update------------------------------\n')
                            elif subMenu == 'nama': 
                                    listStockProduct[x]['nama']=input('\t Masukkan nama product Terbaru: ').capitalize()
                                    print('\n-----------------------------Nama product sudah berhasil di update-----------------------------\n')
                            elif subMenu == 'stock_product': 
                                    listStockProduct[x]['stock_product']=input('\t Masukkan jumlah stock product Terbaru: ')
                                    print('\n-----------------------------stock_product sudah berhasil di update----------------------------\n')
                            elif subMenu == 'uom': 
                                    listStockProduct[x]['uom']=input('\t Masukkan Uom product Terbaru: ')
                                    print('\n-----------------------------Uom product sudah berhasil di update------------------------------\n')
                            elif subMenu == 'exp_date': 
                                    listStockProduct[x]['exp_date']=input('\t Masukkan tanggal exp_date product Terbaru(dd/mm/yy): ')
                                    print('\n---------------------------exp_date product sudah berhasil di update---------------------------\n')
                            elif subMenu == 'purchase_price_per_uom': 
                                    listStockProduct[x]['purchase_price_per_uom']=input('\t Masukkan purchase_price_per_uom Terbaru: ')
                                    print('\n------------------------purchase_price_per_uom sudah berhasil di update------------------------\n')
                            else:
                                  print('\n------------------------------Pilihan Yang Anda Masukkan Salah ------------------------------\n') 
                    else:
                        print('\n------------------------------Pilihan Yang Anda Masukkan Salah ------------------------------\n')                                
                            
        elif subMenu == '2':
            break
        else:
            print('\n------------------------------Pilihan Yang Anda Masukkan Salah ------------------------------\n')
            
def menghapusProduct() :
    while True:
        subMenu= input ('''
        Submenu Menghapus Product
        1. Menghapus Product
        2. kembali ke menu awal
        Silahkan pilih Submenu Menghapus Product [1-2] : ''')
        if subMenu == '1':
            idProduct= str(input('\tMasukkan id_product yang ingin dihapus:')).upper()
            for i in range (len(listStockProduct)):
                if idProduct == listStockProduct[i]['id_product']:
                    y = '\tProduct Tersedia'
                    break
                else:
                    y = '\tProduct Tidak Tersedia'       
            print(y)
            if y == '\tProduct Tersedia':
                while True:
                    checker = input('\tingin menghapus product tersebut (Y/N): ').upper()
                    if checker == 'N':
                        print('\n------------------------------Product Tidak Dihapus------------------------------\n')
                        break
                    elif checker == 'Y':
                        del listStockProduct[i]
                        print('\n-------------------------Product Telah Berhasil Di Hapus--------------------------\n')
                        break
                    else:
                        print('\n------------------------------Pilihan Yang Anda Masukkan Salah ------------------------------\n')
                else:
                    break
               
        elif subMenu == '2':
            break
        else:
            print('\n----------------------------Pilihan Yang Anda Masukkan Salah ----------------------------\n')             
            
while True:
    PilihanMenu = input('''
        Selamat Datang di Gudang Frozen Food
        List Menu:
        1. Menampilkan Daftar Product
        2. Menambahkan Product
        3. Mengupdate Product
        4. Menghapus Product
        5. Exit Program
        Masukkan angka Menu yang ingin dijalankan :''')
    
    if(PilihanMenu == '1'):
        menampilkanDaftarProduct()
    elif (PilihanMenu=='2'):
        menambahProduct()
    elif (PilihanMenu=='3'):
        mengupdateInfoProduct() 
    elif (PilihanMenu=='4'):
        menghapusProduct()
    elif (PilihanMenu=='5'):
        print('\n--------------------------------------------EXIT----------------------------------------------\n')
        print('=> \t\t\t\t ANDA KELUAR DARI APLIKASI \t\t\t\t <=')
        print('=> \t\t\t TERIMA KASIH TELAH MENGGUNAKAN APLIKASI \t\t\t <=')
        break 
    else:
        print('\n------------------------------Pilihan Yang Anda Masukkan Salah ------------------------------\n')