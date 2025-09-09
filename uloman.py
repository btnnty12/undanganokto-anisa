from PIL import Image, ImageDraw, ImageFont

# Ukuran A4 300 DPI
WIDTH, HEIGHT = 2480, 3508

# Buat kanvas putih
background = Image.new("RGB", (WIDTH, HEIGHT), "white")

# Load font Times New Roman
font_title = ImageFont.truetype("times.ttf", 100)  # pastikan font tersedia
font_body = ImageFont.truetype("times.ttf", 60)

# Tambahkan Judul
draw = ImageDraw.Draw(background)
title_text = "UNDANGAN MULI MERANAI"
w, h = draw.textsize(title_text, font=font_title)
draw.text(((WIDTH - w) / 2, 300), title_text, fill="black", font=font_title)

# Isi teks undangan (dari Anda)
body_text = """
Uloman

Ngehaguk kuti rumpok Tuha Raja Unggal Suku Muli Najin Meranai 

Tiyuh : …………………………
Di : ………………………..

ASSALAMUALAIKUM Wr. Wb.
SUMBAHPUN……SUMBAHPUN

Tabik-tabik jama kuti unyin muli najin meranai hikam haga mokpok gerok canggot muranai mansa muli atau wayah-wayah dirasan anak buay hikam keluarga.

Hi. Kausar, S.Pd.,MM. Gelar Raja Bangsawan

Rani/Tanggal : Selasa malam Rabu, 30 September 2025
Pok Tangan Jinganan : Tiyuh Negara Tulang Bawang Kec. Bunga Mayang Kab. Lampung Utara
Pukul : 19.00 WIB s.d Selesai
Acara : Canggot Muli Najin Meranai

Untuk sinalah hikam sangat mengharopko kuti rumpok dapok ratong ngeramik ragomi canggot sai hikam laksanako mudah-mudahan unyin kuti rumpok tiyuh tuha raja punyimbang unggal suku muli najin muranai dijaohko sai kuasa jak sawat halangan sehingga kuti rumpok dapok jama-jama ratong nyaksiko canggot sai haga hikam laksanako.

WASSALAMUALAIKUM Wr. Wb.

Gedung Ketapang 10 September 2025
Hormat Hikam

YOVI SETYAWAN
Kepala Meranai Tiyuh Gedung Ketapang
"""

# Gambar isi teks (multiline)
draw.multiline_text((300, 700), body_text, fill="black", font=font_body, spacing=20)

# Simpan hasil PNG
background.save("undangan_muli_meranai.png", dpi=(300,300))
print("Undangan berhasil disimpan!")