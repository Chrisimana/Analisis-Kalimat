import tkinter as tk
from gui import KalimatApp

def main():
    # Buat window utama
    root = tk.Tk()
    
    # Buat aplikasi
    app = KalimatApp(root)
    
    # Jalankan aplikasi
    root.mainloop()

if __name__ == "__main__":
    main()