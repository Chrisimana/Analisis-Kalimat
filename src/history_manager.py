import json
import os
from datetime import datetime

class HistoryManager:
    def __init__(self, filename="history.json"):
        self.filename = filename
        self.history = []
        self.load_history()
    
    def load_history(self):
        """Memuat riwayat dari file"""
        if os.path.exists(self.filename):
            try:
                with open(self.filename, 'r') as file:
                    self.history = json.load(file)
            except (json.JSONDecodeError, IOError):
                self.history = []
    
    def save_history(self):
        """Menyimpan riwayat ke file"""
        try:
            with open(self.filename, 'w') as file:
                json.dump(self.history, file, indent=2)
        except IOError:
            pass  # Gagal menyimpan, tapi program tetap berjalan
    
    def add_entry(self, kalimat_asli, kalimat_dibalik, jumlah_vokal, jumlah_konsonan, jumlah_kata, total_karakter):
        """Menambahkan entri baru ke riwayat"""
        entry = {
            "timestamp": datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
            "kalimat_asli": kalimat_asli,
            "kalimat_dibalik": kalimat_dibalik,
            "jumlah_vokal": jumlah_vokal,
            "jumlah_konsonan": jumlah_konsonan,
            "jumlah_kata": jumlah_kata,
            "total_karakter": total_karakter
        }
        
        self.history.append(entry)
        
        # Batasi riwayat hingga 50 entri terakhir
        if len(self.history) > 50:
            self.history = self.history[-50:]
        
        self.save_history()
    
    def get_history(self):
        """Mengembalikan seluruh riwayat"""
        return self.history
    
    def clear_history(self):
        """Menghapus semua riwayat"""
        self.history = []
        self.save_history()