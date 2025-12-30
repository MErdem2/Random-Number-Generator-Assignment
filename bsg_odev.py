import time

class CollatzRNG:
    def __init__(self, seed=None):
        if seed is None:
            
            self.state = int(time.time() * 1000)
        else:
            self.state = seed

    def next_bit(self):
        """Bir sonraki rastgele biti üretir."""
        if self.state % 2 == 0:
            self.state = self.state // 2
        else:
            self.state = 3 * self.state + 1
        
        return self.state % 2

    def generate_bytes(self, num_bytes):
        """Belirtilen sayıda byte üretir."""
        result = []
        for _ in range(num_bytes):
            byte_val = 0
            for _ in range(8):
                byte_val = (byte_val << 1) | self.next_bit()
            result.append(byte_val)
        return bytes(result)

    def generate_bit_string(self, length):
        """Belirtilen uzunlukta 0 ve 1 stringi üretir."""
        return "".join(str(self.next_bit()) for _ in range(length))


def run_tests():
    print("--- Collatz RNG Test Başlatılıyor ---")
    
    seed_value = 123456789
    rng = CollatzRNG(seed=seed_value)
    print(f"Seed Değeri: {seed_value}")
    
    bit_count = 1000
    bit_string = rng.generate_bit_string(bit_count)
    
    print(f"\nÜretilen İlk 50 Bit: {bit_string[:50]}...")
    
    zeros = bit_string.count('0')
    ones = bit_string.count('1')
    
    print("\n--- Frekans Testi Sonuçları ---")
    print(f"Toplam Bit: {bit_count}")
    print(f"0 Sayısı: {zeros} (%{zeros/bit_count*100:.2f})")
    print(f"1 Sayısı: {ones} (%{ones/bit_count*100:.2f})")
    
    if 45 < (zeros/bit_count*100) < 55:
        print("SONUÇ: BAŞARILI. (0 ve 1 dağılımı dengeli)")
    else:
        print("SONUÇ: UYARI. (Dağılımda sapma var, seed değiştirilmeli veya algoritma tuzlanmalı)")

if __name__ == "__main__":
    run_tests()
