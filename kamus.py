meme_dict = {"CRINGE": "Sesuatu yang sangat aneh atau memalukan",
            "LOL": "Tanggapan umum terhadap sesuatu yang lucu",
             "FYI": "Supaya tahu aja..",
             "ROFL": "ROFL digunakan sebagai reaksi terhadap sesuatu yang lucu, mirip dengan LOL"
            }

word = input("Ketik kata yang tidak Kamu mengerti (gunakan huruf kapital semua!): ")
if word in meme_dict.keys():
    # Apa yang harus kita lakukan jika kata itu ditemukan?
    print(meme_dict[word])

else:
    # Apa yang harus kita lakukan jika kata itu tidak ditemukan?
    print("Kita belum memiliki kata ini... Tapi kita sedang mengusahakannya!")
