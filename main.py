# Nama : Wiweka Yoga Sadewa
# NIM : 20/456382/TK/50512
# Prodi : Teknologi Infotmasi
# ----------------------------

from experta import *

class MedicalExpert(KnowledgeEngine):

    @Rule(salience = 2)
    def needed_data(self):
        print('\n[-----------------------------------------------------------------------------------------------------------]')
        print("Hai, ini merupakan projek sederhana untuk memeriksa apakah kamu mengalami intoleransi terhadap makanan\nDisclaimer untuk tidak menggunakan projek ini sebagai pilihan utama diagnosis penyakit anda\n\nAkan diberikan 15 gejala intoleransi makanan dan anda diminta untuk menjawab 'y' untuk ya dan 'n' untuk tidak")
        print('[-----------------------------------------------------------------------------------------------------------]\n')

    # Question
    @Rule(salience = 1)
    def Question(self):
        self.sakit_perut = input("Sakit perut: ")
        self.kembung = input("Kembung: ")
        self.diare = input("Diare: ")
        self.sakit_kepala = input("Sakit Kepala: ")
        self.sakit_sendi = input("Sakit Sendi: ")
        self.ruam_kulit = input("Ruam Kulit: ")
        self.cemas = input("Cemas: ")
        self.detak_kencang = input("Detak Jantung Kencang: ")
        self.kentut_berlebih = input("Kentut Berlebih: ")
        self.mual_muntah = input("Mual atau muntah: ")
        self.sulit_tidur = input("Sulit tidur: ")
        self.hidung_mampet = input("Hidung mampet: ")
        self.gatal = input("Gatal: ")
        self.keram_perut = input("Keram perut: ")
        self.nafas_ngik = input("Nafas bersura ngik: ")

        self.declare(Fact(sakit_perut = self.sakit_perut))
        self.declare(Fact(kembung = self.kembung))
        self.declare(Fact(diare = self.diare))
        self.declare(Fact(sakit_kepala = self.sakit_kepala))
        self.declare(Fact(sakit_sendi = self.sakit_sendi))
        self.declare(Fact(ruam_kulit = self.ruam_kulit))
        self.declare(Fact(cemas = self.cemas))
        self.declare(Fact(detak_kencang = self.detak_kencang))
        self.declare(Fact(kentut_berlebih = self.kentut_berlebih))
        self.declare(Fact(mual_muntah = self.mual_muntah))
        self.declare(Fact(sulit_tidur = self.sulit_tidur))
        self.declare(Fact(hidung_mampet = self.hidung_mampet))
        self.declare(Fact(gatal = self.gatal))
        self.declare(Fact(keram_perut = self.keram_perut))
        self.declare(Fact(nafas_ngik = self.nafas_ngik))

    # Diagnosa
    @Rule(Fact(sakit_perut = 'y'), Fact(kembung = 'y'), Fact(diare = 'y'), Fact(sakit_kepala = 'n'), Fact(sakit_sendi = 'n'), Fact(ruam_kulit ='n'), Fact(cemas ='n'), Fact(detak_kencang ='n'), Fact(kentut_berlebih ='y'), Fact(mual_muntah ='y'), Fact(sulit_tidur ='n'), Fact(hidung_mampet ='n'), Fact(gatal ='n'), Fact(keram_perut ='n'), Fact(nafas_ngik = 'n'))
    def disease_0(self):
        self.declare(Fact(disease = 'Laktosa'))

    @Rule(Fact(sakit_perut = 'y'), Fact(kembung = 'y'), Fact(diare = 'y'), Fact(sakit_kepala = 'y'), Fact(sakit_sendi = 'y'), Fact(ruam_kulit ='y'), Fact(cemas ='y'), Fact(detak_kencang ='n'), Fact(kentut_berlebih ='n'), Fact(mual_muntah ='n'), Fact(sulit_tidur ='n'), Fact(hidung_mampet ='n'), Fact(gatal ='n'), Fact(keram_perut ='n'), Fact(nafas_ngik = 'n'))
    def disease_1(self):
        self.declare(Fact(disease = 'Gluten'))

    @Rule(Fact(sakit_perut = 'n'), Fact(kembung = 'n'), Fact(diare = 'n'), Fact(sakit_kepala = 'n'), Fact(sakit_sendi = 'n'), Fact(ruam_kulit = 'n'), Fact(cemas = 'y'), Fact(detak_kencang = 'y'), Fact(kentut_berlebih = 'n'), Fact(mual_muntah = 'n'), Fact(sulit_tidur = 'y'), Fact(hidung_mampet = 'n'), Fact(gatal = 'n'), Fact(keram_perut = 'n'), Fact(nafas_ngik = 'n'))
    def disease_2(self):
        self.declare(Fact(disease = 'Kafein'))

    @Rule(Fact(sakit_perut = 'n'), Fact(kembung = 'n'), Fact(diare = 'y'), Fact(sakit_kepala = 'n'), Fact(sakit_sendi = 'n'), Fact(ruam_kulit = 'n'), Fact(cemas = 'n'), Fact(detak_kencang = 'n'), Fact(kentut_berlebih = 'n'), Fact(mual_muntah = 'n'), Fact(sulit_tidur = 'n'), Fact(hidung_mampet = 'y'), Fact(gatal = 'y'), Fact(keram_perut = 'n'), Fact(nafas_ngik = 'y'))
    def disease_3(self):
        self.declare(Fact(disease = 'Salisilat'))
    
    @Rule(Fact(sakit_perut = 'n'), Fact(kembung = 'n'), Fact(diare = 'y'), Fact(sakit_kepala = 'y'), Fact(sakit_sendi = 'n'), Fact(ruam_kulit = 'y'), Fact(cemas = 'y'), Fact(detak_kencang = 'n'), Fact(kentut_berlebih = 'n'), Fact(mual_muntah = 'n'), Fact(sulit_tidur = 'n'), Fact(hidung_mampet = 'n'), Fact(gatal = 'y'), Fact(keram_perut = 'y'), Fact(nafas_ngik = 'n'))
    def disease_0(self):
        self.declare(Fact(disease = 'Amina'))

    @Rule(Fact(sakit_perut = 'y'), Fact(kembung = 'y'), Fact(diare = 'y'), Fact(sakit_kepala = 'n'), Fact(sakit_sendi = 'n'), Fact(ruam_kulit = 'n'), Fact(cemas = 'n'), Fact(detak_kencang = 'n'), Fact(kentut_berlebih = 'y'), Fact(mual_muntah = 'n'), Fact(sulit_tidur = 'n'), Fact(hidung_mampet = 'n'), Fact(gatal = 'n'), Fact(keram_perut = 'n'), Fact(nafas_ngik = 'n'))
    def disease_0(self):
        self.declare(Fact(disease = 'FODMAPs'))

    @Rule(Fact(sakit_perut = 'n'), Fact(kembung = 'n'), Fact(diare = 'y'), Fact(sakit_kepala = 'n'), Fact(sakit_sendi = 'n'), Fact(ruam_kulit = 'y'), Fact(cemas = 'n'), Fact(detak_kencang = 'n'), Fact(kentut_berlebih = 'n'), Fact(mual_muntah = 'n'), Fact(sulit_tidur = 'n'), Fact(hidung_mampet = 'y'), Fact(gatal = 'y'), Fact(keram_perut = 'n'), Fact(nafas_ngik = 'y'))
    def disease_0(self):
        self.declare(Fact(disease = 'Sulfit'))

    @Rule(Fact(sakit_perut = 'y'), Fact(kembung = 'y'), Fact(diare = 'n'), Fact(sakit_kepala = 'n'), Fact(sakit_sendi = 'n'), Fact(ruam_kulit = 'n'), Fact(cemas = 'n'), Fact(detak_kencang = 'n'), Fact(kentut_berlebih = 'y'), Fact(mual_muntah = 'y'), Fact(sulit_tidur = 'n'), Fact(hidung_mampet = 'n'), Fact(gatal = 'n'), Fact(keram_perut = 'n'), Fact(nafas_ngik = 'n'))
    def disease_0(self):
        self.declare(Fact(disease = 'Fruktosa'))

    @Rule(Fact(sakit_perut = 'y'), Fact(kembung = 'n'), Fact(diare = 'y'), Fact(sakit_kepala = 'n'), Fact(sakit_sendi = 'n'), Fact(ruam_kulit = 'y'), Fact(cemas = 'n'), Fact(detak_kencang = 'n'), Fact(kentut_berlebih = 'n'), Fact(mual_muntah = 'y'), Fact(sulit_tidur = 'n'), Fact(hidung_mampet = 'y'), Fact(gatal = 'y'), Fact(keram_perut = 'n'), Fact(nafas_ngik = 'y'))
    def disease_0(self):
        self.declare(Fact(disease = 'Seafood'))

    @Rule(Fact(sakit_perut = 'y'), Fact(kembung = 'y'), Fact(diare = 'y'), Fact(sakit_kepala = 'n'), Fact(sakit_sendi = 'n'), Fact(ruam_kulit = 'y'), Fact(cemas = 'n'), Fact(detak_kencang = 'n'), Fact(kentut_berlebih = 'n'), Fact(mual_muntah = 'y'), Fact(sulit_tidur = 'n'), Fact(hidung_mampet = 'n'), Fact(gatal = 'y'), Fact(keram_perut = 'y'), Fact(nafas_ngik = 'n'))
    def disease_0(self):
        self.declare(Fact(disease = 'Telur'))
    
    # If Unknwon
    @Rule(NOT (Fact(disease = W())))
    def unmatched(self):
        self.declare(Fact(disease = 'unknown'))

    @Rule(Fact(disease = MATCH.disease))
    def getDisease(self, disease): 
        if(disease == 'unknown'):
            # Varibel gejala
            mapDisease = ['sakit_perut', 'kembung', 'diare', 'sakit_kepala', 'sakit_sendi', 'ruam_kulit', 'cemas', 'detak_kencang', 'kentut_berlebih', 'mual_muntah', 'sulit_tidur', 'hidung_mampet', 'gatal', 'keram_perut', 'nafas_ngik']
            
            mapDisease_val = [self.sakit_perut, self.kembung, self.diare, self.sakit_kepala, self.sakit_sendi, self.ruam_kulit, self.cemas, self.detak_kencang, self.kentut_berlebih, self.mual_muntah, self.sulit_tidur, self.hidung_mampet, self.gatal, self.keram_perut, self.nafas_ngik]
            
            dictionary= {
                        "Laktosa": "sakit_perut,kembung,diare,kentut_berlebih,mual_muntah",
                        "Gluten": "sakit_perut,kembung,diare,sakit_kepala,sakit_sendi,ruam_kulit,cemas",
                        "Kafein": "detak_kencang,cemas,sulit_tidur",
                        "Salisilat": "hidung_mampet,nafas_ngik,diare,gatal",
                        "Amina": "ruam_kulit,sakit_kepala, gatal,cemas,keram_perut,diare",
                        "FODMAPs": "kembung,diare,kentut_berlebih,sakit_perut",
                        "Sulfit": "gatal,hidung_mampet,ruam_kulit,diare,nafas_ngik",
                        "Fruktosa": "kentut_berlebih,mual_muntah,sakit_perut, kembung",
                        "Seafood": "gatal,ruam_kulit,nafas_ngik,hidung_mampet,sakit_perut,diare,mual_muntah",
                        "Telur": "sakit_perut,kembung,keram_perut,diare,mual_muntah,ruam_kulit,gatal"
                        }
                        
            # Mencari gejala yang dirasakan
            yes_symptoms = []
            for i in range(0,len(mapDisease_val)):
                if mapDisease_val[i] == 'y':
                    yes_symptoms.append(mapDisease[i])
            
            max_val = 0
            for key in dictionary.keys():
                val = dictionary[key].split(",")
                count = 0
                tot_symptoms = 0
                    
                # Mencari Gejala yang paing banyak terdeteksi di tiap penyakit
                # Mengubah ke bentuk persen dan memilih dengn persen terbanyak
                for x in val:
                    if x in yes_symptoms:
                        count += 1
                    tot_symptoms += 1
                count = count / tot_symptoms
                
                if count > max_val:
                    max_val = count
                    pred_dis = key
            
            if max_val == 0:
                print("Kamu tidak intoleran terhadap jenis makanan apapun")
            else:
                print('\n[-----------------------------------------------------------------------------------------------------------]')
                print("Kami tidak menemukan secara pasti akan penyakitmu namun kemungkinan besar kamu memiliki intoleransi terhadap",pred_dis)
                print ('\nSedikit info tentang intoleransi',pred_dis)               
                f = open("intolerance/" + pred_dis + ".txt", "r")
                print(f.read())
                print('[-----------------------------------------------------------------------------------------------------------]\n')
        else:
            print('\n[-----------------------------------------------------------------------------------------------------------]')
            print("Kamu memiliki intoleransi terhadap",disease)
            print ('\nSedikit info tentang intoleransi',disease)               
            f = open("intolerance/" + disease + ".txt", "r")
            print(f.read())
            print('[-----------------------------------------------------------------------------------------------------------]\n')

engine = MedicalExpert()
engine.reset()
engine.run()