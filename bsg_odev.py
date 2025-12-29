import time

class XorshiftRNG:
    def __init__(self, seed=None):
        if seed is None:
            self.state = int(time.time() * 1000) & 0xFFFFFFFF
        else:
            self.state = seed & 0xFFFFFFFF
        if self.state == 0:
            self.state = 123456789

    def random_int(self):
        x = self.state
        x ^= (x << 13) & 0xFFFFFFFF
        
        x ^= (x >> 17) & 0xFFFFFFFF
        
        x ^= (x << 5) & 0xFFFFFFFF
        
        self.state = x
        return x

    def random_float(self):
        return self.random_int() / 4294967295.0

    def randint(self, low, high):

        range_width = high - low
        return low + (self.random_int() % range_width)

rng = XorshiftRNG()

print(f"Başlangıç Seed: {rng.state}")
print("-" * 20)

print("0-1 arası ondalıklı:")
for _ in range(5):
    print(f"{rng.random_float():.5f}")

print("\n1 ile 100 arası tam sayı:")
for _ in range(5):
    print(rng.randint(1, 100))