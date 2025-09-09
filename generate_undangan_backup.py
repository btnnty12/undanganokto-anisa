import os

# data acara
acara_list = [
    {
        "judul": "Ngakuk Kebayan",
        "hari": "Senin, 22 September 2025",
        "pukul": "09.00 WIB s/d selesai",
        "tempat": "Karta Raharja Kec. Tulang Bawang Udik, Kab. Tulang Bawang Barat"
    },
    {
        "judul": "Akad Nikah",
        "hari": "Rabu, 24 September 2025",
        "pukul": "09.00 WIB s/d selesai",
        "tempat": "Jl. Jagad Buana Gg. Pancasila No.35, RT 03 RK 04 Desa Negara Tulang Bawang, Kec. Bunga Mayang, Kab. Lampung Utara",
        "maps": "https://maps.app.goo.gl/o3zDdygzkPqmhQVH9?g_st=aw"
    },
    {
        "judul": "Pumgawi Gawi / Canggok Muli Meranai",
        "hari": "Selasa, 30 September 2025",
        "pukul": "09.00 WIB s/d selesai",
        "tempat": "Jl. Jagad Buana Gg. Pancasila, Desa Negara Tulang Bawang, Kec. Bunga Mayang, Kab. Lampung Utara"
    },
    {
        "judul": "Resepsi Pernikahan",
        "hari": "Sabtu, 04 Oktober 2025",
        "pukul": "10.00 WIB s/d selesai",
        "tempat": "Jl. Jagad Buana Gg. Pancasila No.35, RT 03 RK 04 Desa Negara Tulang Bawang, Kec. Bunga Mayang, Kab. Lampung Utara",
        "highlight": True
    }
]

acara_html = "".join([
    f"""
    <div class='card {"highlight" if ac.get("highlight") else ""}'>
        <h3>{ac['judul']}</h3>
        <p><strong>{ac['hari']}</strong> | {ac['pukul']}</p>
        <p>📍 {ac['tempat']}</p>
        <a href="{ac.get('maps', '#')}" target="_blank" class="map-link">Lihat di Google Maps</a>
    </div>
    """
    for ac in acara_list
])

# Data Undangan
data = {
    "nama_pria": "Ns. Oktorullah, S.Kep",
    "nama_wanita": "Anisa Agustina, S.H.",
    "panggilan": "Okto & Anisa",
    "tanggal_resepsi": "Sabtu, 04 Oktober 2025",
    "lokasi": "Jl. Jagad Buana Gg. Pancasila No.35, Lampung Utara",
    "maps": "https://maps.app.goo.gl/o3zDdygzkPqmhQVH9?g_st=aw",
    "musik": "kumbang hati.mp3",
    "foto_pria": "DSC03249.jpg",
    "foto_wanita": "DSC03246.jpg",
    "rekening": [
        "BRI - 565501021252537 a.n ANISA AGUSTINA",
        "BNI - 0461191523 a.n OKTORULLAH"
    ],
    "wa_rsvp": "6282176886737"
}

galeri = [
    "foto1.jpg", "foto2.jpg", "foto3.jpg",
    "foto4.jpg", "foto5.jpg", "foto6.jpg",
    "foto7.jpg", "foto8.jpg", "foto9.jpg"
  ]

galeri_html = "".join([f"<div class='slide'><img src='{img}' alt='Galeri'></div>" for img in galeri])

# HTML TEMPLATE
html_template = f"""
<!DOCTYPE html>
<html lang="id">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>Undangan {data['panggilan']}</title>
  <link href="https://fonts.googleapis.com/css2?family=Poppins:wght@300;500;700&family=Great+Vibes&display=swap" rel="stylesheet">
  <style>
    * {{
      margin: 0; padding: 0; box-sizing: border-box;
    }}
    body {{
      font-family: 'Poppins', sans-serif;
      background: url('tapis.jpg') fixed center center;
      background-size: cover;
      color: #333;
      overflow-x: hidden;
    }}
    h1,h2,h3 {{
      font-family: 'Great Vibes', cursive;
      color: #b71c1c;
    }}
    .cover-section {{
  height: 100vh;
  display: flex; justify-content: center; align-items: center;
  text-align: center;
  position: relative;
  overflow: hidden;
  background: url('tapis.jpg') center/cover no-repeat;
}}
.cover-overlay {{
  position: absolute;
  top:0; left:0; width:100%; height:100%;
  background: rgba(0,0,0,0.5);
}}
.cover-section-content {{
  position: relative;
  z-index: 1;
  animation: fadeInUp 2s ease;
}}
.cover-photo {{
  width: 200px; height: 200px;
  border-radius: 50%;
  border: 8px solid #fff;
  object-fit: cover;
  box-shadow: 0 0 25px rgba(255,215,0,0.5);
  margin-bottom: 20px;
  animation: zoomIn 3s ease;
}}
.cover-title {{
  font-size: 60px;
  color: #fff;
  text-shadow: 2px 2px 10px rgba(0,0,0,0.7);
}}
.cover-date {{
  font-size: 20px;
  color: #f5f5f5;
  margin-top: 10px;
}}

/* BUTTON */
.btn {{
  margin-top: 25px; padding: 15px 30px;
  border: none; border-radius: 30px;
  background: linear-gradient(45deg, #d4af37, #b71c1c);
  color: white; font-size: 18px; cursor: pointer;
  box-shadow: 0 4px 12px rgba(0,0,0,0.3);
  transition: 0.3s;
  text-decoration: none; display: inline-block;
}}
.btn:hover {{
  transform: scale(1.05);
}}
    section {{
      min-height: 80vh;
      padding: 60px 20px;
      background: rgba(255,255,255,0.95);
      margin: 40px auto;
      border-radius: 20px;
      max-width: 900px;
      text-align: center;
      transform: translateY(30px);
      opacity: 0;
      transition: all 1s ease-in-out;
    }}
    section.visible {{
      transform: translateY(0);
      opacity: 1;
    }}
    .couple {{
      display: flex; justify-content: center;
      gap: 40px; flex-wrap: wrap;
    }}
    .couple img {{
      width: 220px; height: 220px; object-fit: cover;
      border-radius: 50%; border: 8px solid #d4af37;
      box-shadow: 0 8px 25px rgba(0,0,0,0.4);
      transition: transform 0.4s;
    }}
    .couple img:hover {{
      transform: scale(1.08);
    }}
    .countdown {{
      margin-top: 30px;
      font-size: 22px;
      font-weight: bold;
      color: #b71c1c;
    }}
    .gallery-grid {{
  display: grid;
  grid-template-columns: repeat(auto-fit, minmax(220px, 1fr));
  gap: 15px;
  margin-top: 20px;
}}
.gallery-grid img {{
  width: 100%;
  border-radius: 15px;
  box-shadow: 0 6px 15px rgba(0,0,0,0.3);
  cursor: pointer;
  transition: transform 0.4s;
}}
.gallery-grid img:hover {{
  transform: scale(1.05);
}}
.lightbox {{
  display: none;
  position: fixed; top:0; left:0; width:100%; height:100%;
  background: rgba(0,0,0,0.8);
  display: flex; align-items: center; justify-content: center;
  z-index: 1000;
}}
.lightbox img {{
  max-width: 90%; max-height: 80%;
  border-radius: 10px;
  box-shadow: 0 0 20px rgba(255,255,255,0.3);
}}
    .timeline {{
      margin-top: 30px; text-align: left;
    }}
    .timeline .card {{
      background: #fff;
      padding: 20px;
      margin: 20px auto;
      border-left: 6px solid #c19a6b;
      border-radius: 15px;
      box-shadow: 0 6px 15px rgba(0,0,0,0.1);
      max-width: 600px;
      transition: transform 0.3s, box-shadow 0.3s, border-left-color 0.3s;
    }}
    .timeline .card:hover {{
      transform: translateY(-5px);
      box-shadow: 0 12px 25px rgba(0,0,0,0.2);
      border-left-color: #b71c1c;
    }}
    .timeline .card.highlight {{
      border-left-color: #b71c1c;
      background: #fff5f5;
    }}
    .timeline .card h3 {{
      color: #8b0000;
      font-size: 1.5rem;
      margin-bottom: 10px;
    }}
    .timeline .card p {{
      margin: 5px 0;
      font-size: 0.95rem;
    }}
    .music-control {{
      position: fixed; bottom: 20px; right: 20px;
      background: #b71c1c; color: #fff;
      border-radius: 50%; width: 60px; height: 60px;
      display: flex; align-items: center; justify-content: center;
      box-shadow: 0 6px 15px rgba(0,0,0,0.3);
      cursor: pointer; font-size: 24px;
      z-index: 999;
    }}
    footer {{
      text-align:center; padding:30px; font-size:14px; color:#555;
    }}
    @media(max-width:600px){{
      .couple img {{ width:160px; height:160px; }}
      .gallery-slider img {{ width:220px; height:160px; }}
    }}
    @keyframes fadeInUp {{
  from{{opacity:0; transform: translateY(40px);}}
  to {{opacity:1; transform: translateY(0);}}
}}
@keyframes zoomIn {{
  from {{transform: scale(0.8); opacity:0;}}
  to {{transform: scale(1); opacity:1;}}
}}
  </style>
</head>
<body>

<!-- COVER -->
<section id="cover-section" class="cover-section">
  <div class="cover-overlay"></div>
  <div class="cover-section-content">
    <img src="DSC03210.jpg" alt="Foto Pengantin" class="cover-photo">
    <h1 class="cover-title">{data['panggilan']}</h1>
    <p class="cover-date">{data['tanggal_resepsi']}</p>
    <button class="btn" onclick="bukaUndangan()">💌 Buka Undangan</button>
  </div>
</section>

<!-- CONTENT -->
<div id="content" style="display:none;">

  <section id="doa">
    <h2>🌸 Doa & Harapan</h2>
    <p style="margin-top:20px; font-size:16px; line-height:1.8;">
      “Dan di antara tanda-tanda (kebesaran)-Nya ialah Dia menciptakan untukmu pasangan hidupmu
      supaya kamu merasa tenteram kepadanya, dan dijadikan-Nya di antaramu rasa kasih dan sayang.”
      (QS. Ar-Rum: 21)
    </p>
  </section>

  <section id="mempelai">
    <h2>🤵 & 👰 Mempelai</h2>
    <div class="couple" style="margin-top:30px;">
      <div>
        <img src="{data['foto_pria']}" alt="Okto">
        <p><b>{data['nama_pria']}</b></p>
      </div>
      <div>
        <img src="{data['foto_wanita']}" alt="Anisa">
        <p><b>{data['nama_wanita']}</b></p>
      </div>
    </div>
  </section>

  <section id="story">
    <h2>💌 Cerita Kami</h2>
    <p style="margin-top:20px; font-size:16px; line-height:1.8;">
      Akhir tahun 2021 okto dikenalkan oleh saudaranya yang kebetulan kenal dengan anisa pada saat kuliah, tetapi komunikasi pertama hanyalah kenalan antara kedua belah pihak. Tahun 2023 kami kembali berkomunikasi dengan menanyakan kabar satu sama lain hingga melakukan pertemuan, setelah melakukan beberapa kali pertemuan terbentuk lah komitmen untuk kejenjang yang lebih serius dalam menjalin hubungan.
Tahun 2025 okto dan keluarga datang kerumah  untuk menyampaikan ke inginan untuk kejenjang yang lebih serius (Menikah) , moment bahagia tersebut dirasakan bersama dengan adanya melakukan tunangan dan sampai lah tiba kesepakatan antara kedua belah keluarga hingga penentuan tangal acara pernikahan.
    </p>
  </section>

  <section id="acara">
    <h2>📅 Rangkaian Acara</h2>
    <div class="timeline">
      {acara_html}
    </div>
    <div class="countdown" id="countdown"></div>
  </section>

  <section id="galeri">
    <h2>📸 Galeri</h2>
    <div class="gallery-grid">
      {''.join([f"<img src='{img}' alt='Galeri' onclick='openLightbox(this.src)'>" for img in galeri])}
    </div>
  </section>

  <!-- Lightbox -->
  <div id="lightbox" class="lightbox" onclick="this.style.display='none'">
    <img id="lightbox-img">
  </div>

  <section id="amplop">
    <h2>🎁 Amplop Digital</h2>
    <p style="margin-top:15px;">{"<br>".join(data['rekening'])}</p>
  </section>

  <section id="rsvp">
    <h2>🙏 Konfirmasi Kehadiran</h2>
    <a href="https://wa.me/{data['wa_rsvp']}" class="btn" target="_blank">📲 RSVP via WhatsApp</a>
  </section>

  <footer>
    Terima kasih atas doa & restu Anda 🌹<br>
    <b>{data['panggilan']}</b>
  </footer>

</div>

<!-- Musik -->
<audio id="musik" loop>
  <source src="{data['musik']}" type="audio/mpeg">
</audio>
<div class="music-control" onclick="toggleMusic()">🎶</div>

<script>
  function bukaUndangan() {{
    document.getElementById("cover-section").style.display = "none";
    document.getElementById("content").style.display = "block";
    document.getElementById("musik").play();
    window.scrollTo(0,0);
  }}
function openLightbox(src) {{
  document.getElementById("lightbox-img").src = src;
  document.getElementById("lightbox").style.display = "flex";
}}

  // Countdown (diselaraskan ke pukul 10:00 WIB)
  var acara = new Date("Oct 4, 2025 10:00:00").getTime();
  var x = setInterval(function() {{
    var now = new Date().getTime();
    var distance = acara - now;

    var days = Math.floor(distance / (1000*60*60*24));
    var hours = Math.floor((distance % (1000*60*60*24)) / (1000*60*60));
    var minutes = Math.floor((distance % (1000*60*60)) / (1000*60));
    var seconds = Math.floor((distance % (1000*60)) / 1000);

    var el = document.getElementById("countdown");
    if (!el) return;

    if (distance >= 0) {{
      el.innerHTML = days + " Hari " + hours + " Jam " + minutes + " Menit " + seconds + " Detik ";
    }} else {{
      clearInterval(x);
      el.innerHTML = "Acara Sedang Berlangsung 🎉";
    }}
  }}, 1000);

  // Scroll Animation
  window.addEventListener("scroll", function() {{
    document.querySelectorAll("section").forEach(function(sec) {{
      var pos = sec.getBoundingClientRect().top;
      if(pos < window.innerHeight - 100) {{
        sec.classList.add("visible");
      }}
    }});
  }});

  // Music Control
  function toggleMusic() {{
    var musik = document.getElementById("musik");
    var ctrl = document.querySelector(".music-control");
    if(musik.paused) {{
      musik.play();
      ctrl.innerHTML = "⏸";
    }} else {{
      musik.pause();
      ctrl.innerHTML = "🎶";
    }}
  }}
</script>

</body>
</html>
"""

# Simpan file
base_dir = os.path.dirname(os.path.abspath(__file__))
output_file = os.path.join(base_dir, "undangan.html")

with open(output_file, "w", encoding="utf-8") as f:
    f.write(html_template)

print(f"✅ Undangan interaktif cantik dibuat di {output_file}")