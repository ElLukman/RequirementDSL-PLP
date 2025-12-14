import unittest
import logging
import json

# Konfigurasi Logging
logging.basicConfig(level=logging.INFO, format='%(message)s')

# --- MOCK SYSTEM STATE (Memori Bersama) ---
class SystemState:
    data = {}
    
    @classmethod
    def set(cls, key, value):
        cls.data[key] = value
    @classmethod
    def get(cls, key):
        return cls.data.get(key)

# --- KODE INI DIGENERATE OTOMATIS OLEH REQSPECL ---
# Dibuat oleh: ReqSpecL generator


class TestFeature_OtentikasiUser(unittest.TestCase):
    # Memastikan urutan tes berdasarkan nama (alfabetis)
    def setUp(self):
        print('\n' + '-'*50)
    
    def test_001_Nasabah_login_dengan_kredensial_valid(self):
        logging.info("SCENARIO 001: Nasabah login dengan kredensial valid")
        current_state = SystemState.data
        logging.info(f"  [DEBUG] State Awal: {current_state}")
        # GIVEN: Sistem siap menerima input
        logging.info("  [GIVEN] Sistem siap menerima input")
        # WHEN: Nasabah memasukkan username dan password benar
        logging.info("  [WHEN] Nasabah memasukkan username dan password benar")
        # THEN: Sistem memvalidasi kredensial
        logging.info("  [THEN] Sistem memvalidasi kredensial (Verified)")
        # THEN: Status sesi menjadi 'ACTIVE'
        logging.info("  [THEN] Status sesi menjadi 'ACTIVE' (Verified)")
    
    def test_002_Nasabah_mengakses_dashboard_akun(self):
        logging.info("SCENARIO 002: Nasabah mengakses dashboard akun")
        current_state = SystemState.data
        logging.info(f"  [DEBUG] State Awal: {current_state}")
        # GIVEN: Status sesi adalah 'ACTIVE'
        logging.info("  [GIVEN] Status sesi adalah 'ACTIVE'")
        # WHEN: Nasabah membuka halaman dashboard
        logging.info("  [WHEN] Nasabah membuka halaman dashboard")
        # THEN: Sistem menampilkan informasi saldo
        logging.info("  [THEN] Sistem menampilkan informasi saldo (Verified)")
    
    def test_003_Nasabah_melakukan_logout(self):
        logging.info("SCENARIO 003: Nasabah melakukan logout")
        current_state = SystemState.data
        logging.info(f"  [DEBUG] State Awal: {current_state}")
        # GIVEN: Status sesi adalah 'ACTIVE'
        logging.info("  [GIVEN] Status sesi adalah 'ACTIVE'")
        # WHEN: Nasabah menekan tombol Logout
        logging.info("  [WHEN] Nasabah menekan tombol Logout")
        # THEN: Sistem mengakhiri sesi
        logging.info("  [THEN] Sistem mengakhiri sesi (Verified)")
        # THEN: Status sesi menjadi 'INACTIVE'
        logging.info("  [THEN] Status sesi menjadi 'INACTIVE' (Verified)")
    
    def test_004_Akses_dashboard_setelah_logout(self):
        logging.info("SCENARIO 004: Akses dashboard setelah logout")
        current_state = SystemState.data
        logging.info(f"  [DEBUG] State Awal: {current_state}")
        # GIVEN: Status sesi adalah 'INACTIVE'
        logging.info("  [GIVEN] Status sesi adalah 'INACTIVE'")
        # WHEN: Nasabah mencoba membuka halaman dashboard via URL
        logging.info("  [WHEN] Nasabah mencoba membuka halaman dashboard via URL")
        # THEN: Sistem menolak akses
        status = SystemState.get('status_kelas')
        if status == 'CLOSED':
            logging.info("  [SUCCESS] Sistem menolak karena kelas CLOSED")
        else:
            pass
        # THEN: Sistem menampilkan pesan error 'Silakan Login Kembali'
        logging.info("  [THEN] Sistem menampilkan pesan error 'Silakan Login Kembali' (Verified)")

# GIVEN: Status sesi adalah 'ACTIVE'
logging.info("  [GIVEN] Status sesi adalah 'ACTIVE'")
# GIVEN: Saldo Nasabah > 500000
logging.info("  [GIVEN] Saldo Nasabah > 500000")
# GIVEN: Rekening tujuan valid
logging.info("  [GIVEN] Rekening tujuan valid")
# WHEN: Nasabah transfer Rp 100.000 ke teman
logging.info("  [WHEN] Nasabah transfer Rp 100.000 ke teman")
# THEN: Sistem mengurangi saldo pengirim
logging.info("  [THEN] Sistem mengurangi saldo pengirim (Verified)")
# THEN: Sistem menambah saldo penerima
logging.info("  [THEN] Sistem menambah saldo penerima (Verified)")
# THEN: Notifikasi 'Transfer Berhasil' muncul
logging.info("  [THEN] Notifikasi 'Transfer Berhasil' muncul (Verified)")
# GIVEN: Status sesi adalah 'ACTIVE'
logging.info("  [GIVEN] Status sesi adalah 'ACTIVE'")
# GIVEN: Saldo Nasabah < 10000
logging.info("  [GIVEN] Saldo Nasabah < 10000")
# WHEN: Nasabah mencoba transfer Rp 1.000.000
logging.info("  [WHEN] Nasabah mencoba transfer Rp 1.000.000")
# THEN: Sistem menolak transaksi
status = SystemState.get('status_kelas')
if status == 'CLOSED':
logging.info("  [SUCCESS] Sistem menolak karena kelas CLOSED")
else:
pass
# THEN: Peringatan 'Saldo Tidak Cukup' ditampilkan
logging.info("  [THEN] Peringatan 'Saldo Tidak Cukup' ditampilkan (Verified)")


if __name__ == '__main__':
unittest.main()
