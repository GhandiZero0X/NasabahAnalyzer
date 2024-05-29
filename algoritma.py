class ExpertSystem:
    def __init__(self):
        pass
    
    def classify(self, prestasi, jaminan, pekerjaan):
        if jaminan == 'Logam Mulia':
            return 'Kelas Mikro'
        elif jaminan == 'BPKB':
            if pekerjaan == 'Swasta':
                return 'Kelas Sedang'
            elif pekerjaan == 'Wirausaha':
                if prestasi == 'Baik':
                    return 'Kelas Atas'
                elif prestasi == 'Bermasalah':
                    return 'Kelas Mikro'
        elif jaminan == 'Sertifikat HM':
            if pekerjaan == 'PNS':
                return 'Kelas Atas'
            elif pekerjaan == 'Swasta':
                if prestasi == 'Baik':
                    return 'Kelas Atas'
                elif prestasi == 'Bermasalah':
                    return 'Kelas Sedang'
        return 'Keputusan tidak dapat dibuat'

# Buat instance dari ExpertSystem
expert_system = ExpertSystem()

# Contoh input
input_data = [
    {'prestasi': 'Baik', 'jaminan': 'Logam Mulia', 'pekerjaan': 'PNS'},
    {'prestasi': 'Bermasalah', 'jaminan': 'BPKB', 'pekerjaan': 'Swasta'},
    {'prestasi': 'Baik', 'jaminan': 'BPKB', 'pekerjaan': 'Wirausaha'},
    {'prestasi': 'Bermasalah', 'jaminan': 'Sertifikat HM', 'pekerjaan': 'Swasta'},
]

# Klasifikasikan setiap input
for data in input_data:
    prestasi = data['prestasi']
    jaminan = data['jaminan']
    pekerjaan = data['pekerjaan']
    hasil = expert_system.classify(prestasi, jaminan, pekerjaan)
    print(f"Prestasi: {prestasi}, Jaminan: {jaminan}, Pekerjaan: {pekerjaan} -> Tingkat Kelas: {hasil}")
