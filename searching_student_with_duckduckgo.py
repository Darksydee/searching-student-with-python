import requests
from bs4 import BeautifulSoup
import time
import random

MAX_SEARCHES = 1  # Batasi jumlah pencarian maksimal
MIN_DELAY = 5  # Waktu minimum antara setiap permintaan
MAX_DELAY = 10  # Waktu maksimum antara setiap permintaan

def search_student_info(name):
    search_query = f"{name} site:linkedin.com"
    duckduckgo_url = f"https://duckduckgo.com/html/?q={search_query}"

    # Header yang lebih mirip dengan perilaku browser manusia
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36",
        "Accept-Language": "en-US,en;q=0.5",
        "Accept-Encoding": "gzip, deflate, br",
        "Referer": "https://duckduckgo.com/",
        "Connection": "keep-alive",
        "Upgrade-Insecure-Requests": "1",
        "Sec-Fetch-Dest": "document",
        "Sec-Fetch-Mode": "navigate",
        "Sec-Fetch-Site": "same-origin",
        "Sec-Fetch-User": "?1",
        "Cache-Control": "max-age=0",
        "TE": "trailers"
    }

    searches_done = 0  # Melacak jumlah pencarian yang sudah dilakukan
    print("Mencari menggunakan DuckDuckGo...")
    while searches_done < MAX_SEARCHES:
        try:
            response = requests.get(duckduckgo_url, headers=headers)
            if response.status_code == 200:
                soup = BeautifulSoup(response.text, 'html.parser')
                results = soup.find_all('a', class_='result__a')

                if results:
                    print("Hasil pencarian:")
                    for result in results:
                        link = result['href']
                        if "linkedin.com" in link:
                            print("Profil LinkedIn:", link)
                            # Lakukan hal lain sesuai kebutuhan
                    searches_done += 1  # Tambahkan jumlah pencarian yang sudah dilakukan
                    if searches_done >= MAX_SEARCHES:
                        break  # Keluar dari loop jika sudah mencapai batas
                else:
                    print("Tidak ada hasil yang ditemukan.")
            else:
                print(f"Gagal melakukan koneksi ke DuckDuckGo dengan kode status: {response.status_code}.")
                break  # Keluar dari loop jika terjadi kesalahan
        except Exception as e:
            print(f"Terjadi kesalahan: {e}")
            break  # Keluar dari loop jika terjadi kesalahan

        # Menunggu antara setiap permintaan untuk mengurangi risiko deteksi sebagai bot
        delay = random.randint(MIN_DELAY, MAX_DELAY)
        time.sleep(delay)

if __name__ == "__main__":
    name = input("Masukkan nama mahasiswa yang ingin dicari informasinya: ")
    search_student_info(name)
