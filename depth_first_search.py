#contoh peta 
peta =  {'A':set(['B']),
         'B':set(['C']),
         'C':set(['D','H','I']),
         'D':set(['C','E','F','H']),
         'E':set(['D']),
         'F':set(['D','G']),
         'G':set(['F','H']),
         'H':set(['C','D','G','L']),
         'I':set(['C','J','K']),
         'J':set(['I']),
         'K':set(['I','L']),
         'L':set(['K','H'])}
	
def dfs(graf, mulai, tujuan): # A - H
    stack = [[mulai]]
    visited = set()

    while stack:
        #hitung panjang tumpukan dan masukkan ke variabel panjang_tumpukan
        #panjang_tumpukan = -1 # PALING BELAKANG -> KONSEP LIFO
        
       
        # masukkan tumpukan palinif state == tujuan:g atas ke variabel jalur
        jalur = stack.pop(-1) # 
    
        # simpan node yang dipilih ke variabel state, misal jalur = C,B maka simpan B ke variabel state
        state = jalur[-1] #-1 artinya adalah indeks paling belakang

        # cek state apakah sama dengan tujuan, jika ya maka return jalur
        if state == tujuan:
            return jalur
        # jika state tidak sama dengan tujuan, maka cek apakah state tidak ada di visited
        elif state not in visited:
            # jika state tidak ada di visited maka cek cabang
            for cabang in graf.get(state, []): #cek semua cabang dari state
                jalur_baru = list(jalur) #masukkan isi dari variabel jalur ke variabel jalur_baru
                jalur_baru.append(cabang) #update/tambah isi jalur_baru dengan cabang
                stack.append(jalur_baru) #update/tambah queue dengan jalur_baru

            # tandai state yang sudah dikunjungi sebagai visited
            visited.add(state)
    
        #cek isi tumpukan
        isi = len(stack)
        if isi == 0:
            print("Tidak ditemukan")

mulai=input("masukkan awalan : ")
tujuan=input("masukkan tujuan : ")   
print(dfs(peta,mulai,tujuan))
