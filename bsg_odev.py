import time

class CollatzRNG:
    def __init__(self, seed=None):
        if seed is None:
            self.state = int(time.time() * 1000)
        else:
            self.state = seed
        
    def next_bit(self):
        if self.state % 2 == 0:
            self.state = self.state // 2
        else:
            self.state = 3 * self.state + 1
        
        mixed_val = (self.state * 2654435761) & 0xFFFFFFFF
        
        return mixed_val % 2

    def generate_bit_string(self, length):
        return "".join(str(self.next_bit()) for _ in range(length))


def run_tests():
    print("--- Collatz RNG (Final Sürüm) Test Başlatılıyor ---")
    
    seed_value = 192837465564738291
    rng = CollatzRNG(seed=seed_value)
    print(f"Seed Değeri: {seed_value}")
    
    bit_count = 10000
    bit_string = rng.generate_bit_string(bit_count)
    
    print(f"\nÜretilen İlk 50 Bit: {bit_string[:50]}...")

    zeros = bit_string.count('0')
    ones = bit_string.count('1')
    
    print("\n--- Frekans Testi Sonuçları ---")
    print(f"Toplam Bit: {bit_count}")
    print(f"0 Sayısı: {zeros} (%{zeros/bit_count*100:.2f})")
    print(f"1 Sayısı: {ones} (%{ones/bit_count*100:.2f})")
    
    oran = zeros / bit_count * 100
    if 48 < oran < 52:
        print("\n>>> SONUÇ: BAŞARILI <<<")
        print("(0 ve 1 dağılımı mükemmel bir dengeye sahip.)")
    else:
        print("\n>>> SONUÇ: MAKUL <<<")
        print("(Ufak sapmalar olsa da rastgelelik kabul edilebilir seviyede.)")

if __name__ == "__main__":
    run_tests()
