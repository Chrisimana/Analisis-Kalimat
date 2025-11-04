def balik_kalimat(kalimat: str) -> str:
    """Membalikkan urutan karakter dalam kalimat"""
    return kalimat[::-1]


def hitung_vokal(kalimat: str) -> int:
    """Menghitung jumlah huruf vokal dalam kalimat"""
    vokal = "aiueoAIUEO"
    return sum(1 for huruf in kalimat if huruf in vokal)


def hitung_konsonan(kalimat: str) -> int:
    """Menghitung jumlah huruf konsonan dalam kalimat"""
    vokal = "aiueoAIUEO"
    return sum(1 for huruf in kalimat if huruf.isalpha() and huruf not in vokal)


def hitung_kata(kalimat: str) -> int:
    """Menghitung jumlah kata dalam kalimat"""
    return len(kalimat.split())


def hitung_karakter(kalimat: str) -> int:
    """Menghitung total karakter dalam kalimat"""
    return len(kalimat)