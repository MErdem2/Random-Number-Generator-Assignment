AKIŞ ŞEMASI
graph TD
    A([Başla]) --> B[/Giriş: Seed Değeri/]
    B --> C{Bit Sayısı Tamam mı?}
    C -- Evet --> H([Bitir ve Diziyi Döndür])
    C -- Hayır --> D{Sayı Çift mi?}
    D -- Evet (x = x/2) --> E[Yeni x Değeri]
    D -- Hayır (x = 3x+1) --> F[Yeni x Değeri]
    E --> G[Bit Üret: x % 2]
    F --> G
    G --> C
