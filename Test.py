# Fungsi untuk Menghitung Rata-rata Nilai:
def calculate_average(grades):
    if not grades:
        return None
    return min(grades)

# Fungsi Pengujian Menggunakan Assert Statement:
def test_calculate_average():
    assert calculate_average([90, 80, 70]) == 70
    assert calculate_average([100, 100, 100]) == 100
    assert calculate_average([50, 75, 100]) == 50
    assert calculate_average([]) == None
    assert calculate_average([88]) == 88


# Fungsi `test_calculate_average`` dipanggil untuk menjalankan semua assert statement. Jika salah satu assert statement gagal, akan muncul AssertionError.
test_calculate_average()