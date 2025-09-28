import os

# data acara
acara_list = [
    {
        "judul": "Ngakuk Kebayan",
        "hari": "Senin, 22 September 2025",
        "tempat": "Karta Raharja Kec. Tulang Bawang Udik, Kab. Tulang Bawang Barat",
        "selesai": True
    },
    {
        "judul": "Akad Nikah",
        "hari": "Rabu, 24 September 2025",
        "tempat": "Jl. Jagad Buana Gg. Pancasila No.35, RT 03 RK 04 Desa Negara Tulang Bawang, Kec. Bunga Mayang, Kab. Lampung Utara",
        "selesai": True
    },
    {
        "judul": "Acara Adat Lampung",
        "hari": "Selasa, 30 September s.d 2 oktober 2025",
        "tempat": "Jl. Jagad Buana Gg. Pancasila, Desa Negara Tulang Bawang, Kec. Bunga Mayang, Kab. Lampung Utara"
    },
    {
        "judul": "Resepsi Pernikahan",
        "hari": "Sabtu, 04 Oktober 2025",
        "pukul": "10.00 WIB s/d selesai",
        "tempat": "Jl. Jagad Buana Gg. Pancasila No.35, RT 03 RK 04 Desa Negara Tulang Bawang, Kec. Bunga Mayang, Kab. Lampung Utara",
        "maps": "https://maps.app.goo.gl/o3zDdygzkPqmhQVH9?g_st=aw",
        "highlight": True
    }
]

acara_html = "".join([
    f"""
    <div class='card {"highlight" if ac.get("highlight") else ""} {"selesai" if ac.get("selesai") else ""}'>
        <h3>{ac['judul']}</h3>
        <p><strong>{ac['hari']}</strong>{f" | {ac['pukul']}" if ac.get('pukul') else ""}</p>
        <p>📍 {ac['tempat']}</p>
        {f'<a href="{ac.get("maps", "#")}" target="_blank" class="map-link">Lihat di Google Maps</a>' if ac.get("maps") else ''}
        {f'<span class="selesai-badge">telah dilaksanakan</span>' if ac.get("selesai") else ''}
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
    "maps": "https://maps.app.goo.gl/wDivgd5js4zFs3gAA?g_st=aw",
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
    .section-title {{
      font-family: 'Dancing Script', cursive;
      font-weight: 700;
      font-size: 3rem;
      color: #8b0000;
      text-align: center;
      margin-bottom: 30px;
      position: relative;
      text-shadow: 2px 2px 4px rgba(0,0,0,0.1);
    }}
    .section-title::after {{
      content: '';
      position: absolute;
      bottom: -10px;
      left: 50%;
      transform: translateX(-50%);
      width: 100px;
      height: 4px;
      background: linear-gradient(90deg, #d4af37, #b71c1c, #d4af37);
      border-radius: 2px;
    }}
    .doa-section .section-title {{
      color: #fff;
      text-shadow: 2px 2px 4px rgba(0,0,0,0.5);
    }}
    .story-section .section-title {{
      color: #fff;
      text-shadow: 2px 2px 4px rgba(0,0,0,0.5);
    }}
    /* Pembuka Section */
    .pembuka-section {{
      background: linear-gradient(135deg, #ffffff, #f8f9fa);
      color: #333;
      position: relative;
      overflow: hidden;
    }}
    .pembuka-section::before {{
      content: '';
      position: absolute;
      inset: 0;
      background: url('tapis.jpg') center/cover no-repeat;
      opacity: 0.05;
      z-index: 0;
    }}
    .pembuka-content {{
      position: relative;
      z-index: 1;
      background: rgba(255,255,255,0.85);
      padding: 40px;
      border-radius: 20px;
      box-shadow: 0 12px 30px rgba(0,0,0,0.08);
      max-width: 900px;
      margin: 0 auto;
      backdrop-filter: blur(6px);
    }}
    .pembuka-salam {{
      font-family: 'Dancing Script', cursive;
      font-size: 2rem;
      color: #8b0000;
      margin-bottom: 16px;
    }}
    .pembuka-text {{
      font-size: 1rem;
      color: #444;
      line-height: 1.9;
    }}
    .cover-section {{
      height: 100vh;
      display: flex; 
      flex-direction: column;
      justify-content: space-between; 
      align-items: center;
      text-align: center;
      position: relative;
      overflow: hidden;
      background: linear-gradient(135deg, #8b0000, #b71c1c, #d4af37);
    }}
    .cover-overlay {{
      position: absolute;
      top: 0; left: 0; width: 100%; height: 100%;
      background: linear-gradient(180deg, 
        rgba(0,0,0,0.6) 0%, 
        rgba(0,0,0,0.2) 40%, 
        rgba(0,0,0,0.1) 60%, 
        rgba(0,0,0,0.5) 100%);
      z-index: 1;
    }}
    .cover-section-content {{
      position: relative;
      z-index: 2;
      width: 100%;
      height: 100%;
      display: flex;
      flex-direction: column;
      justify-content: space-between;
      padding: 20px;
    }}
    .cover-photo {{
      width: 100%; 
      height: 100%;
      object-fit: cover;
      object-position: center center;
      position: absolute;
      top: 0;
      left: 0;
      z-index: 0;
      image-rendering: -webkit-optimize-contrast;
      image-rendering: crisp-edges;
    }}
    .cover-top {{
      flex: 0 0 auto;
      padding: 20px;
      background: rgba(0,0,0,0.8);
      border-radius: 15px;
      backdrop-filter: blur(10px);
      margin: 20px;
      max-width: 300px;
      align-self: flex-start;
    }}
    .cover-bottom {{
      flex: 0 0 auto;
      padding: 30px;
      background: rgba(0,0,0,0.8);
      border-radius: 20px;
      backdrop-filter: blur(10px);
      margin: 20px;
      max-width: 400px;
      align-self: flex-end;
    }}
    .cover-text {{
      position: relative;
      z-index: 2;
      background: transparent;
      padding: 0;
      border-radius: 0;
    }}
    .cover-title {{
      font-size: clamp(2.5rem, 8vw, 4rem);
      color: #fff;
      text-shadow: 2px 2px 10px rgba(0,0,0,0.7);
      margin-bottom: 10px;
    }}
    .cover-date {{
      font-size: clamp(1rem, 4vw, 1.2rem);
      color: #f5f5f5;
      margin-top: 10px;
    }}
    .cover-nama {{
      font-size: clamp(1rem, 4vw, 1.2rem);
      color: #fff;
      margin-bottom: 15px;
      text-shadow: 2px 2px 4px rgba(0,0,0,0.7);
      text-align: center;
      line-height: 1.4;
    }}
    .cover-nama .kepada {{
      font-size: clamp(0.8rem, 3vw, 0.9rem);
      color: #f5f5f5;
      margin-bottom: 5px;
      font-style: italic;
    }}
    .cover-nama .bapak-ibu {{
      font-size: clamp(0.7rem, 3vw, 0.8rem);
      color: #e0e0e0;
      margin-bottom: 8px;
    }}
    .cover-nama .nama-tamu {{
      font-size: clamp(1.2rem, 5vw, 1.5rem);
      color: #fff;
      font-weight: bold;
      text-shadow: 2px 2px 6px rgba(0,0,0,0.8);
      border-bottom: 2px solid #d4af37;
      padding-bottom: 5px;
      display: inline-block;
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
      transform: translateY(0);
      opacity: 1;
      transition: all 0.5s ease-in-out;
    }}
    section.visible {{
      transform: translateY(0);
      opacity: 1;
    }}
    
    /* AMPLOP DIGITAL STYLING - FIX ROTATION */
    .amplop-section {{
      background: linear-gradient(135deg, #f8f9fa, #e9ecef);
      border-radius: 20px;
      padding: 40px;
      margin: 20px 0;
      position: relative;
      overflow: hidden;
      box-shadow: 0 10px 30px rgba(0,0,0,0.1);
      transform: none !important;
      transform-origin: center center !important;
    }}
    .amplop-section, .amplop-section * {{
      transform: none !important;
      transform-origin: center center !important;
    }}
    .amplop-content {{
      position: relative;
      z-index: 1;
      transform: none !important;
      transform-origin: center center !important;
    }}
    .amplop-header {{
      text-align: center;
      margin-bottom: 30px;
      transform: none !important;
      transform-origin: center center !important;
    }}
    .amplop-icon {{
      font-size: 3rem;
      display: block;
      margin-bottom: 15px;
      animation: bounce 2s infinite;
      transform: none !important;
      transform-origin: center center !important;
    }}
    .amplop-subtitle {{
      font-size: 16px;
      color: #666;
      margin-top: 10px;
      font-style: italic;
      transform: none !important;
      transform-origin: center center !important;
    }}
    .rekening-list {{
      display: grid;
      grid-template-columns: repeat(auto-fit, minmax(300px, 1fr));
      gap: 20px;
      margin: 30px 0;
      transform: none !important;
      transform-origin: center center !important;
    }}
    .rekening-item {{
      background: linear-gradient(135deg, #fff, #f8f9fa);
      padding: 25px;
      border-radius: 15px;
      border: 2px solid #e9ecef;
      text-align: center;
      transition: all 0.3s ease;
      position: relative;
      overflow: hidden;
      transform: none !important;
      transform-origin: center center !important;
    }}
    .rekening-item:hover {{
      transform: translateY(-5px) !important;
      box-shadow: 0 15px 35px rgba(0,0,0,0.1);
      border-color: #d4af37;
    }}
    .bank-name {{
      font-size: 18px;
      font-weight: bold;
      color: #8b0000;
      margin-bottom: 10px;
      font-family: 'Dancing Script', cursive;
      transform: none !important;
      transform-origin: center center !important;
    }}
    .account-number {{
      font-size: 16px;
      color: #333;
      font-weight: 600;
      margin-bottom: 8px;
      letter-spacing: 1px;
      transform: none !important;
      transform-origin: center center !important;
    }}
    .account-holder {{
      font-size: 14px;
      color: #666;
      font-style: italic;
      transform: none !important;
      transform-origin: center center !important;
    }}
    .amplop-footer {{
      text-align: center;
      margin-top: 30px;
      padding: 20px;
      background: rgba(139, 0, 0, 0.1);
      border-radius: 15px;
      font-size: 16px;
      color: #8b0000;
      font-weight: 500;
      transform: none !important;
      transform-origin: center center !important;
    }}
    
    /* KOMENTAR SECTION STYLING - FIX ROTATION */
    .komentar-section {{
      background: linear-gradient(135deg, #fff5f5, #ffe8e8);
      border-radius: 20px;
      padding: 40px;
      margin: 20px 0;
      position: relative;
      overflow: hidden;
      box-shadow: 0 10px 30px rgba(0,0,0,0.1);
      transform: none !important;
      text-align: center;
      transform-origin: center center !important;
    }}
    .komentar-section, .komentar-section * {{
      transform: none !important;
      transform-origin: center center !important;
    }}
    .komentar-content {{
      position: relative;
      z-index: 1;
      transform: none !important;
      transform-origin: center center !important;
    }}
    .komentar-form {{
      background: rgba(255,255,255,0.9);
      padding: 30px;
      border-radius: 15px;
      margin-bottom: 30px;
      box-shadow: 0 5px 15px rgba(0,0,0,0.1);
      transform: none !important;
      transform-origin: center center !important;
    }}
    .form-group {{
      margin-bottom: 20px;
      transform: none !important;
      transform-origin: center center !important;
    }}
    .form-label {{
      display: block;
      margin-bottom: 8px;
      font-weight: 600;
      color: #8b0000;
      font-size: 14px;
      transform: none !important;
      transform-origin: center center !important;
    }}
    .komentar-input, .komentar-textarea {{
      width: 100%;
      padding: 12px 15px;
      border: 2px solid #e9ecef;
      border-radius: 10px;
      font-size: 14px;
      transition: all 0.3s ease;
      font-family: 'Poppins', sans-serif;
      transform: none !important;
      transform-origin: center center !important;
    }}
    .komentar-input:focus, .komentar-textarea:focus {{
      outline: none;
      border-color: #d4af37;
      box-shadow: 0 0 0 3px rgba(212, 175, 55, 0.1);
      transform: none !important;
    }}
    .komentar-textarea {{
      min-height: 100px;
      resize: vertical;
    }}
    .btn-group {{
      display: flex;
      gap: 15px;
      flex-wrap: wrap;
      justify-content: center;
      transform: none !important;
      transform-origin: center center !important;
    }}
    .komentar-btn, .wa-btn {{
      padding: 12px 25px;
      border: none;
      border-radius: 25px;
      font-size: 14px;
      font-weight: 600;
      cursor: pointer;
      transition: all 0.3s ease;
      text-decoration: none;
      display: inline-block;
      transform: none !important;
      transform-origin: center center !important;
    }}
    .komentar-btn {{
      background: linear-gradient(45deg, #d4af37, #b71c1c);
      color: white;
    }}
    .wa-btn {{
      background: linear-gradient(45deg, #25d366, #128c7e);
      color: white;
    }}
    .komentar-btn:hover, .wa-btn:hover {{
      transform: translateY(-2px) !important;
      box-shadow: 0 5px 15px rgba(0,0,0,0.2);
    }}
    .public-komentar {{
      background: rgba(255,255,255,0.8);
      padding: 30px;
      border-radius: 15px;
      box-shadow: 0 5px 15px rgba(0,0,0,0.1);
      transform: none !important;
      transform-origin: center center !important;
    }}
    .komentar-header {{
      text-align: center;
      margin-bottom: 25px;
      transform: none !important;
      transform-origin: center center !important;
    }}
    .komentar-item {{
      background: linear-gradient(135deg, #fff, #f8f9fa);
      padding: 20px;
      margin-bottom: 15px;
      border-radius: 12px;
      border-left: 4px solid #d4af37;
      box-shadow: 0 3px 10px rgba(0,0,0,0.1);
      transition: all 0.3s ease;
      transform: none !important;
      transform-origin: center center !important;
    }}
    .komentar-item:hover {{
      transform: translateX(5px) !important;
      box-shadow: 0 5px 20px rgba(0,0,0,0.15);
    }}
    .komentar-nama {{
      font-weight: bold;
      color: #8b0000;
      margin-bottom: 8px;
      font-size: 16px;
      transform: none !important;
      transform-origin: center center !important;
    }}
    .komentar-teks {{
      color: #333;
      line-height: 1.6;
      margin-bottom: 8px;
      transform: none !important;
      transform-origin: center center !important;
    }}
    .komentar-waktu {{
      font-size: 12px;
      color: #666;
      font-style: italic;
      transform: none !important;
      transform-origin: center center !important;
    }}
    .no-komentar {{
      text-align: center;
      color: #666;
      font-style: italic;
      padding: 30px;
      transform: none !important;
      transform-origin: center center !important;
    }}
    /* RSVP (Konfirmasi Kehadiran) */
    .rsvp-box {{
      background: rgba(255,255,255,0.9);
      padding: 20px;
      border-radius: 12px;
      box-shadow: 0 4px 12px rgba(0,0,0,0.08);
      margin: 25px 0;
    }}
    .rsvp-controls {{ display:flex; gap:12px; flex-wrap: wrap; justify-content:center; }}
    .rsvp-select, .rsvp-input {{ padding:10px 12px; border:2px solid #e9ecef; border-radius:10px; font-size:14px; }}
    .rsvp-btn {{ padding:10px 18px; border:none; border-radius:25px; background:linear-gradient(45deg,#66bb6a,#43a047); color:#fff; font-weight:600; cursor:pointer; }}
    .rsvp-btn:hover {{ filter: brightness(1.05); }}
    .rsvp-list {{ margin-top: 18px; text-align:left; }}
    .rsvp-item {{ background:#fff; border-radius:10px; padding:12px 14px; margin:8px 0; display:flex; align-items:center; justify-content:space-between; box-shadow:0 2px 8px rgba(0,0,0,0.06); }}
    .rsvp-name {{ font-weight:600; color:#8b0000; }}
    .rsvp-badge {{ padding:6px 10px; border-radius:16px; font-size:12px; color:#fff; }}
    .rsvp-yes {{ background:#43a047; }}
    .rsvp-maybe {{ background:#f9a825; }}
    .rsvp-no {{ background:#e53935; }}
    
    @keyframes bounce {{
      0%, 20%, 50%, 80%, 100% {{
        transform: translateY(0);
      }}
      40% {{
        transform: translateY(-10px);
      }}
      60% {{
        transform: translateY(-5px);
      }}
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
      grid-template-columns: repeat(auto-fit, minmax(250px, 1fr));
      gap: 20px;
      margin-top: 30px;
      padding: 20px;
      background: linear-gradient(135deg, rgba(255,255,255,0.1), rgba(248,249,250,0.1));
      border-radius: 20px;
      position: relative;
      overflow: hidden;
    }}
    .gallery-grid::before {{
      content: '';
      position: absolute;
      top: 0;
      left: 0;
      right: 0;
      bottom: 0;
      background: url('tapis.jpg') center/cover no-repeat;
      opacity: 0.03;
      z-index: 0;
    }}
    .gallery-grid > * {{
      position: relative;
      z-index: 1;
    }}
    .gallery-grid img {{
      width: 100%;
      height: 250px;
      object-fit: cover;
      border-radius: 20px;
      box-shadow: 0 8px 25px rgba(0,0,0,0.15);
      cursor: pointer;
      transition: all 0.4s ease;
      position: relative;
      overflow: hidden;
    }}
    .gallery-grid img::before {{
      content: '';
      position: absolute;
      top: 0;
      left: 0;
      right: 0;
      bottom: 0;
      background: linear-gradient(45deg, rgba(212, 175, 55, 0.1), rgba(183, 28, 28, 0.1));
      opacity: 0;
      transition: opacity 0.3s ease;
      z-index: 1;
    }}
    .gallery-grid img:hover::before {{
      opacity: 1;
    }}
    .gallery-grid img:hover {{
      transform: translateY(-10px) scale(1.02);
      box-shadow: 0 15px 40px rgba(0,0,0,0.25);
    }}
    .gallery-grid img:nth-child(odd) {{
      transform: rotate(-1deg);
    }}
    .gallery-grid img:nth-child(even) {{
      transform: rotate(1deg);
    }}
    .gallery-grid img:nth-child(odd):hover {{
      transform: translateY(-10px) scale(1.02) rotate(-1deg);
    }}
    .gallery-grid img:nth-child(even):hover {{
      transform: translateY(-10px) scale(1.02) rotate(1deg);
    }}
    .lightbox {{
      display: none;
      position: fixed; 
      top: 0; 
      left: 0; 
      width: 100%; 
      height: 100%;
      background: rgba(0,0,0,0.8);
      align-items: center; justify-content: center;
      z-index: 1000;
      backdrop-filter: blur(5px);
    }}
    .lightbox.open {{
      display: flex;
    }}
    .lightbox img {{
      max-width: 90%; 
      max-height: 80%;
      border-radius: 15px;
      box-shadow: 0 0 30px rgba(255,255,255,0.3);
      animation: zoomIn 0.3s ease;
    }}
    .lightbox::before {{
      content: '✕';
      position: absolute;
      top: 20px;
      right: 30px;
      color: white;
      font-size: 30px;
      cursor: pointer;
      z-index: 1001;
    }}
    .timeline {{
      margin-top: 30px; 
      text-align: left;
      position: relative;
    }}
    .timeline::before {{
      content: '';
      position: absolute;
      left: 30px;
      top: 0;
      bottom: 0;
      width: 4px;
      background: linear-gradient(180deg, #d4af37, #b71c1c, #d4af37);
      border-radius: 2px;
    }}
    .timeline .card {{
      background: linear-gradient(135deg, #fff, #fafafa);
      padding: 25px;
      margin: 30px auto;
      margin-left: 60px;
      border: none;
      border-radius: 20px;
      box-shadow: 0 8px 25px rgba(0,0,0,0.1);
      max-width: 600px;
      transition: all 0.4s ease;
      position: relative;
    }}
    .timeline .card::before {{
      content: '';
      position: absolute;
      left: -45px;
      top: 50%;
      transform: translateY(-50%);
      width: 20px;
      height: 20px;
      background: #d4af37;
      border: 4px solid #fff;
      border-radius: 50%;
      box-shadow: 0 0 0 4px #b71c1c;
    }}
    .timeline .card:hover {{
      transform: translateY(-8px) translateX(10px);
      box-shadow: 0 15px 35px rgba(0,0,0,0.2);
    }}
    .timeline .card.highlight {{
      background: linear-gradient(135deg, #fff5f5, #ffe8e8);
      border: 2px solid #b71c1c;
      box-shadow: 0 10px 30px rgba(183, 28, 28, 0.2);
    }}
    .timeline .card.highlight::before {{
      background: #b71c1c;
      box-shadow: 0 0 0 4px #d4af37;
    }}
    .timeline .card h3 {{
      color: #8b0000;
      font-size: 1.6rem;
      margin-bottom: 15px;
      font-family: 'Dancing Script', cursive;
      font-weight: 700;
    }}
    .timeline .card p {{
      margin: 8px 0;
      font-size: 1rem;
      line-height: 1.6;
    }}
    .timeline .card.selesai {{
      opacity: 0.6;
      background: linear-gradient(135deg, #f5f5f5, #e8e8e8);
    }}
    .selesai-badge {{
      display: inline-block;
      background: linear-gradient(45deg, #4caf50, #66bb6a);
      color: white;
      padding: 8px 15px;
      border-radius: 20px;
      font-size: 12px;
      margin-top: 10px;
      font-weight: bold;
      box-shadow: 0 4px 10px rgba(76, 175, 80, 0.3);
    }}
    .map-link {{
      display: inline-block;
      background: linear-gradient(45deg, #b71c1c, #d32f2f);
      color: white;
      padding: 10px 20px;
      border-radius: 25px;
      text-decoration: none;
      font-size: 13px;
      margin-top: 15px;
      transition: all 0.3s;
      font-weight: bold;
      box-shadow: 0 4px 15px rgba(183, 28, 28, 0.3);
    }}
    .map-link:hover {{
      background: linear-gradient(45deg, #8b0000, #b71c1c);
      transform: translateY(-2px);
      box-shadow: 0 6px 20px rgba(183, 28, 28, 0.4);
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
    .doa-section {{
      background: linear-gradient(135deg, #8b0000, #b71c1c, #d4af37);
      color: white;
      position: relative;
      overflow: hidden;
      min-height: 100vh;
      display: flex;
      align-items: center;
      justify-content: center;
    }}
    .doa-section::before {{
      content: '';
      position: absolute;
      top: 0;
      left: 0;
      right: 0;
      bottom: 0;
      background: url('bg.jpg') center/cover no-repeat;
      opacity: 0.15;
      z-index: 0;
    }}
    .doa-section::after {{
      content: '';
      position: absolute;
      top: 0;
      left: 0;
      right: 0;
      bottom: 0;
      background: radial-gradient(circle at center, transparent 0%, rgba(0,0,0,0.3) 100%);
      z-index: 1;
    }}
    .doa-content {{
      position: relative;
      z-index: 2;
      background: rgba(0,0,0,0.4);
      padding: 60px 40px;
      border-radius: 30px;
      backdrop-filter: blur(15px);
      border: 2px solid rgba(212, 175, 55, 0.3);
      box-shadow: 0 20px 40px rgba(0,0,0,0.3);
      max-width: 800px;
      text-align: center;
      animation: fadeInUp 2s ease;
    }}
    .doa-content .section-title {{
      font-size: 2.5rem;
      margin-bottom: 40px;
      text-shadow: 3px 3px 6px rgba(0,0,0,0.7);
      position: relative;
    }}
    .doa-content .section-title::after {{
      content: '';
      position: absolute;
      bottom: -15px;
      left: 50%;
      transform: translateX(-50%);
      width: 100px;
      height: 4px;
      background: linear-gradient(90deg, #d4af37, #fff, #d4af37);
      border-radius: 2px;
    }}
    .story-section {{
      background: linear-gradient(135deg, #d4af37, #b71c1c);
      color: white;
      position: relative;
      overflow: hidden;
    }}
    .story-section::before {{
      content: '';
      position: absolute;
      top: 0;
      left: 0;
      right: 0;
      bottom: 0;
      background: url('tapis.jpg') center/cover no-repeat;
      opacity: 0.1;
      z-index: 0;
    }}
    .story-content {{
      position: relative;
      z-index: 1;
      background: rgba(0,0,0,0.3);
      padding: 40px;
      border-radius: 20px;
      backdrop-filter: blur(10px);
    }}
    .quote-text {{
      font-size: 22px;
      line-height: 2;
      font-style: italic;
      text-align: center;
      margin: 40px 0;
      position: relative;
      font-weight: 300;
      text-shadow: 2px 2px 4px rgba(0,0,0,0.5);
      letter-spacing: 1px;
    }}
    .quote-text .arabic {{
      font-size: 24px;
      line-height: 2;
      font-style: normal;
      margin-bottom: 16px;
    }}
    .quote-text .latin {{
      font-size: 16px;
      line-height: 1.8;
      font-style: italic;
      opacity: 0.95;
    }}
    .quote-text::before {{
      content: '"';
      font-size: 80px;
      color: #d4af37;
      position: absolute;
      top: -30px;
      left: -20px;
      font-family: 'Great Vibes', cursive;
      text-shadow: 2px 2px 4px rgba(0,0,0,0.5);
      animation: float 3s ease-in-out infinite;
    }}
    .quote-text::after {{
      content: '"';
      font-size: 80px;
      color: #d4af37;
      position: absolute;
      bottom: -50px;
      right: -20px;
      font-family: 'Great Vibes', cursive;
      text-shadow: 2px 2px 4px rgba(0,0,0,0.5);
      animation: float 3s ease-in-out infinite reverse;
    }}
    .verse-ref {{
      text-align: center;
      font-size: 16px;
      color: #d4af37;
      margin-top: 40px;
      font-weight: bold;
      text-shadow: 2px 2px 4px rgba(0,0,0,0.5);
      padding: 15px 25px;
      background: rgba(212, 175, 55, 0.2);
      border-radius: 25px;
      border: 1px solid rgba(212, 175, 55, 0.4);
      display: inline-block;
      letter-spacing: 1px;
    }}
    .story-text {{
      font-size: 16px;
      line-height: 1.8;
      text-align: justify;
      margin: 20px 0;
    }}
    .ucapan-footer {{
      text-align: center;
      margin-top: 40px;
      padding: 30px;
      background: linear-gradient(135deg, rgba(139, 0, 0, 0.1), rgba(183, 28, 28, 0.1));
      border-radius: 15px;
      border: 1px solid rgba(139, 0, 0, 0.2);
    }}
    .ucapan-footer p:first-child {{
      font-size: 18px;
      color: #8b0000;
      margin-bottom: 10px;
      font-weight: 500;
    }}
    .ucapan-footer p:last-child {{
      font-size: 20px;
      color: #b71c1c;
      font-weight: bold;
      font-family: 'Dancing Script', cursive;
    }}
    footer {{
      text-align: center;
      padding: 10px 5px;
      background: linear-gradient(135deg, #f8f9fa, #e9ecef);
      color: #666;
      font-size: 14px;
      border-top: 1px solid #dee2e6;
    }}
    footer p {{
      margin: 2px 0;
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
/* Kerangka section seragam */
.keluarga-section,
.amplop-section,
.komentar-section {{
  max-width: 900px;
  margin: 40px auto;
  padding: 60px 20px;
  background: rgba(255,255,255,0.95);
  border-radius: 20px;
  box-shadow: 0 8px 25px rgba(0,0,0,0.08);
  position: relative;
  overflow: hidden;
}}

/* Overlay ikut radius dan tidak mengganggu klik */
.amplop-section::before,
.komentar-section::before {{
  border-radius: inherit;
  pointer-events: none;
}}

/* Pastikan tidak ada rotasi/geser yang bikin miring */
.amplop-section, .amplop-section * ,
.komentar-section, .komentar-section * {{ transform: none !important; }}

/* Matikan rotasi galeri agar tidak “nular” */
.gallery-grid img:nth-child(odd),
.gallery-grid img:nth-child(even),
.gallery-grid img:nth-child(odd):hover,
.gallery-grid img:nth-child(even):hover {{ transform: none !important; }}

/* Keluarga Besar: frame + posisi foto turun (peci aman) */
.keluarga-wrap {{ display:flex; flex-direction:column; align-items:center; gap:16px; }}
.keluarga-frame {{
  width: 260px; height: 320px; padding:10px;
  border:3px solid #d4af37; border-radius:18px; background:#fff;
  box-shadow:0 10px 30px rgba(0,0,0,0.15);
}}
.keluarga-foto {{
  width:100%; height:100%;
  object-fit: cover; object-position: center 25%;
  border-radius:14px; display:block;
}}
.keluarga-nama {{ max-width:720px; text-align:center; color:#555; line-height:1.8; margin-top:10px; }}
  </style>
</head>
<body>

<!-- COVER -->
<section id="cover-section" class="cover-section">
  <img src="DSC03210.jpg" alt="Foto Pengantin" class="cover-photo">
  <div class="cover-overlay"></div>
  <div class="cover-section-content">
    <div class="cover-top">
      <div class="cover-nama" id="cover-nama">
        <div class="kepada">Kepada Yth;</div>
        <div class="bapak-ibu">Bapak/Ibu/Saudara/i</div>
        <div class="nama-tamu" id="nama-tamu">Nama Tamu</div>
      </div>
    </div>
    <div class="cover-bottom">
      <div class="cover-text">
        <h1 class="cover-title">{data['panggilan']}</h1>
        <p class="cover-date">{data['tanggal_resepsi']}</p>
        <button class="btn" onclick="bukaUndangan()">💌 Buka Undangan</button>
      </div>
    </div>
  </div>
</section>

<!-- CONTENT -->
<div id="content" style="display:none;">

  <section id="pembuka" class="pembuka-section">
    <div class="pembuka-content">
      <h2 class="section-title">💐 Kalimat Pembuka</h2>
      <div class="pembuka-salam">Assalamu'alaikum Warahmatullahi Wabarakatuh</div>
      <div class="pembuka-text">
        Tanpa mengurangi rasa hormat, kami bermaksud mengundang Bapak/Ibu/Saudara/i
        untuk hadir dan memberikan doa restu pada acara resepsi pernikahan kami.
        Kehadiran dan doa restu Bapak/Ibu/Saudara/i merupakan kebahagiaan bagi kami.
      </div>
    </div>
  </section>

  <section id="doa" class="doa-section">
    <div class="doa-content">
      <h2 class="section-title">🌸 Allah berfirman</h2>
      <div class="quote-text">
        <div class="arabic">وَمِنْ اٰيٰتِهٖٓ أَنْ خَلَقَ لَكُمْ مِنْ أَنْفُسِكُمْ أَزْوَاجًا لِّتَسْكُنُوْٓا إِلَيْهَا وَجَعَلَ بَيْنَكُمْ مَوَدَّةً وَرَحْمَةً ۗ إِنَّ فِيْ ذٰلِكَ لَآيَاتٍ لِّقَوْمٍ يَتَفَكَّرُوْنَ</div>
        <div class="latin">Dan di antara tanda-tanda (kebesaran)-Nya ialah Dia menciptakan untukmu pasangan hidupmu supaya kamu merasa tenteram kepadanya, dan dijadikan-Nya di antaramu rasa kasih dan sayang.</div>
      </div>
      <div class="verse-ref">(QS. Ar-Rum: 21)</div>
    </div>
  </section>

  <section id="mempelai">
    <h2 class="section-title">🤵 & 👰 Mempelai</h2>
    <div class="couple" style="margin-top:30px;">
      <div>
        <img src="{data['foto_pria']}" alt="Okto">
        <p><b>{data['nama_pria']}</b></p>
        <p style="font-size:14px; color:#666; margin-top:10px;">
          Putra pertama dari 3 bersaudara<br>
          Putra dari Hi. Kausar, S.Pd.,M.M Gelar Raja Bangsawan<br>
          & Hj. Herlina Suryani, S.Pd Gelar Raja Hindia
        </p>
      </div>
      <div>
        <img src="{data['foto_wanita']}" alt="Anisa">
        <p><b>{data['nama_wanita']}</b></p>
        <p style="font-size:14px; color:#666; margin-top:10px;">
          Putri ke-5 (Bungsu) dari lima bersaudara<br>
          Putri dari Darpin Watoni (Alm) Gelar Tuan Pangeran Takdir<br>
          & Idayati Gelar Tuan Pengiran Dandiyan
        </p>
      </div>
    </div>
  </section>

  <section id="story" class="story-section">
    <div class="story-content">
      <h2 class="section-title">💌 Cerita Kami</h2>
      <div class="story-text">
        Akhir tahun 2021 okto dikenalkan oleh saudaranya yang kebetulan kenal dengan anisa pada saat kuliah, tetapi komunikasi pertama hanyalah kenalan antara kedua belah pihak. Tahun 2023 kami kembali berkomunikasi dengan menanyakan kabar satu sama lain hingga melakukan pertemuan, setelah melakukan beberapa kali pertemuan terbentuk lah komitmen untuk kejenjang yang lebih serius dalam menjalin hubungan.
        <br><br>
        Tahun 2025 okto dan keluarga datang kerumah untuk menyampaikan ke inginan untuk kejenjang yang lebih serius (Menikah), moment bahagia tersebut dirasakan bersama dengan adanya melakukan tunangan dan sampai lah tiba kesepakatan antara kedua belah keluarga hingga penentuan tangal acara pernikahan.
      </div>
    </div>
  </section>

  <section id="acara">
    <h2 class="section-title">📅 Rangkaian Acara</h2>
    <div class="timeline">
      {acara_html}
    </div>
    <div class="countdown" id="countdown"></div>
  </section>

  <section id="galeri">
    <h2 class="section-title">📸 Galeri</h2>
    <div class="gallery-grid">
      {''.join([f"<img src='{img}' alt='Galeri' onclick='openLightbox(this.src)'>" for img in galeri])}
    </div>
  </section>

  <section id="keluarga" class="keluarga-section">
    <h2 class="section-title">👨‍👩‍👧‍👦 Keluarga Besar</h2>
    <div class="keluarga-wrap">
      <div class="keluarga-frame">
        <img src="ortu.jpeg" alt="Keluarga Besar" class="keluarga-foto" />
      </div>
      <div class="keluarga-nama">
        Hi. Kausar, S.Pd.,M.M Gelar Raja Bangsawan<br>
        &amp; Hj. Herlina Suryani, S.Pd Gelar Raja Hindia
      </div>
    </div>
  </section>

  <!-- Lightbox -->
  <div id="lightbox" class="lightbox" onclick="this.style.display='none'">
    <img id="lightbox-img">
  </div>

  <section id="amplop" class="amplop-section">
    <div class="amplop-content">
      <div class="amplop-header">
        <span class="amplop-icon">🎁</span>
        <h2 class="section-title">Amplop Digital</h2>
        <p class="amplop-subtitle">Berikan doa dan restu Anda dengan mengirimkan amplop digital.</p>
      </div>
      <div class="rekening-list">
        {''.join([f'''
        <div class="rekening-item">
          <div class="bank-name">{rek.split(' - ')[0]}</div>
          <div class="account-number">{rek.split(' - ')[1].split(' a.n ')[0]}</div>
          <div class="account-holder">a.n {rek.split(' a.n ')[1]}</div>
        </div>
        ''' for rek in data['rekening']])}
      </div>
    </div>
  </section>

  <section id="komentar" class="komentar-section">
    <div class="komentar-content">
      <h2 class="section-title">🙏 Ucapan & Doa</h2>
      
      <div class="komentar-form">
        <div class="form-group">
          <label class="form-label">Nama Anda</label>
          <input type="text" id="nama-input" class="komentar-input" placeholder="Masukkan nama Anda">
        </div>
        <div class="form-group">
          <label class="form-label">Ucapan & Doa</label>
          <textarea id="komentar-text" class="komentar-textarea" placeholder="Tuliskan ucapan dan doa terbaik untuk mempelai..."></textarea>
        </div>
        <div class="btn-group">
          <button class="komentar-btn" onclick="tambahKomentar()">💝 Tambah Komentar</button>
          <button class="wa-btn" onclick="kirimKeWA()">📤 Kirim ke WhatsApp</button>
        </div>
      </div>
      
      <div class="public-komentar">
        <div class="komentar-header">
          <h3 style="color: #8b0000; font-family: 'Dancing Script', cursive; font-size: 2rem;">💝 Komentar</h3>
        </div>
        <div id="komentar-list" class="no-komentar">
          Belum ada ucapan dari tamu undangan. Jadilah yang pertama! 🌟
        </div>
      </div>
      
      <!-- Konfirmasi Kehadiran (RSVP) -->
      <div class="rsvp-box">
        <h3 style="text-align:center; color:#8b0000; margin-bottom:12px; font-family:'Dancing Script', cursive; font-size: 1.8rem;">✅ Konfirmasi Kehadiran</h3>
        <div class="rsvp-controls">
          <input id="rsvp-nama" class="rsvp-input" type="text" placeholder="Nama Anda">
          <select id="rsvp-status" class="rsvp-select">
            <option value="hadir">Hadir</option>
            <option value="maybe">Masih Dipertimbangkan</option>
            <option value="tidak">Tidak Hadir</option>
          </select>
          <button class="rsvp-btn" onclick="konfirmasiKehadiran()">Simpan</button>
        </div>
        <div class="rsvp-list" id="rsvp-list"></div>
      </div>
      
      <div class="ucapan-footer">
        <p>Terima kasih atas doa & restu Anda 🌹</p>
        <p><b>{data['panggilan']}</b></p>
      </div>
    </div>
  </section>

  <footer>
    <p>© 2025 - Undangan Digital {data['panggilan']} created by baityjn</p>
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
    // Tampilkan semua section langsung
    const sections = document.querySelectorAll('section');
    sections.forEach(section => {{
      section.classList.add('visible');
    }});
    // Panggil tampilkanNama setelah buka undangan
    tampilkanNama();
  }}
function openLightbox(src) {{
  document.getElementById("lightbox-img").src = src;
  document.getElementById("lightbox").classList.add("open");
}}
document.getElementById("lightbox").onclick = function() {{ 
  this.classList.remove("open"); 
}};

  // Countdown untuk acara resepsi
  var targetDate = new Date("October 4, 2025 10:00:00").getTime();
  var countdown = setInterval(function() {{
     var now = new Date().getTime();
     var distance = targetDate - now;
     var days = Math.floor(distance / (1000 * 60 * 60 * 24));
     var hours = Math.floor((distance % (1000 * 60 * 60 * 24)) / (1000 * 60 * 60));
     var minutes = Math.floor((distance % (1000 * 60 * 60)) / (1000 * 60));
     var seconds = Math.floor((distance % (1000 * 60)) / 1000);
     document.getElementById("countdown").innerHTML = days + "d " + hours + "h " + minutes + "m " + seconds + "s ";
     if (distance < 0) {{
       clearInterval(countdown);
       document.getElementById("countdown").innerHTML = "Acara telah dimulai!";
     }}
  }}, 1000);

  // Tampilkan semua section langsung saat load
  window.addEventListener('load', function() {{
    const sections = document.querySelectorAll('section');
    sections.forEach(section => {{
      section.classList.add('visible');
    }});
    tampilkanKomentar();
    tampilkanNama();
    tampilkanRSVP();
    optimizeImages();
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

  // Kirim Komentar ke WhatsApp
  function kirimKomentar() {{
    var komentar = document.getElementById("komentar-text").value;
    if (komentar.trim() === "") {{
      alert("Silakan tulis ucapan terlebih dahulu!");
      return;
    }}
    
    var nama = prompt("Masukkan nama Anda:");
    if (nama === null || nama.trim() === "") {{
      alert("Nama harus diisi!");
      return;
    }}
    
    var pesan = `*Ucapan untuk {data['panggilan']}*\\n\\nDari: ${{nama}}\\n\\n${{komentar}}`;
    var waUrl = `https://wa.me/6281271854664?text=${{encodeURIComponent(pesan)}}`;
    window.open(waUrl, '_blank');
  }}

  // Tampilkan nama di cover
  function tampilkanNama() {{
    const urlParams = new URLSearchParams(window.location.search);
    const nama = urlParams.get('nama') || urlParams.get('to');
    const namaElement = document.getElementById('nama-tamu');
    if (nama && namaElement) {{
      namaElement.textContent = nama;
    }}
  }}

  // Tambah komentar ke web
  function tambahKomentar() {{
    var nama = document.getElementById("nama-input").value;
    var komentar = document.getElementById("komentar-text").value;
    
    if (nama.trim() === "" || komentar.trim() === "") {{
      alert("Silakan isi nama dan ucapan terlebih dahulu!");
      return;
    }}
    
    simpanKomentar(nama, komentar);
    document.getElementById("nama-input").value = "";
    document.getElementById("komentar-text").value = "";
  }}

  // Kirim ke WhatsApp
  function kirimKeWA() {{
    var nama = document.getElementById("nama-input").value;
    var komentar = document.getElementById("komentar-text").value;
    
    if (nama.trim() === "" || komentar.trim() === "") {{
      alert("Silakan isi nama dan ucapan terlebih dahulu!");
      return;
    }}
    
    var pesan = `*Ucapan untuk {data['panggilan']}*\\n\\nDari: ${{nama}}\\n\\n${{komentar}}`;
    var waUrl = `https://wa.me/6281271854664?text=${{encodeURIComponent(pesan)}}`;
    window.open(waUrl, '_blank');
  }}

  // RSVP: Simpan kehadiran ke localStorage
  function konfirmasiKehadiran() {{
    var nama = (document.getElementById('rsvp-nama')||{{}}).value || '';
    var status = (document.getElementById('rsvp-status')||{{}}).value || 'hadir';
    if (nama.trim() === '') {{ alert('Nama harus diisi untuk konfirmasi kehadiran.'); return; }}

    var rsvpList = JSON.parse(localStorage.getItem('rsvpList') || '[]');
    // Update jika nama sudah ada
    var found = false;
    for (var i=0; i<rsvpList.length; i++) {{
      if (rsvpList[i].nama.toLowerCase() === nama.toLowerCase()) {{ rsvpList[i].status = status; found = true; break; }}
    }}
    if (!found) {{ rsvpList.push({{ nama: nama, status: status, waktu: new Date().toLocaleString('id-ID') }}); }}
    localStorage.setItem('rsvpList', JSON.stringify(rsvpList));
    tampilkanRSVP();

    var namaInput = document.getElementById('rsvp-nama'); if (namaInput) namaInput.value = '';
  }}

  function tampilkanRSVP() {{
    var rsvpList = JSON.parse(localStorage.getItem('rsvpList') || '[]');
    var container = document.getElementById('rsvp-list');
    if (!container) return;

    if (rsvpList.length === 0) {{ container.innerHTML = '<div class="no-komentar" style="text-align:center;">Belum ada konfirmasi kehadiran.</div>'; return; }}

    var html = '';
    rsvpList.forEach(function(item){{
      var badgeClass = item.status === 'hadir' ? 'rsvp-badge rsvp-yes' : (item.status === 'tidak' ? 'rsvp-badge rsvp-no' : 'rsvp-badge rsvp-maybe');
      var label = item.status === 'hadir' ? 'Hadir' : (item.status === 'tidak' ? 'Tidak Hadir' : 'Dipertimbangkan');
      html += '<div class="rsvp-item">'
        + '<div class="rsvp-name">' + item.nama + '</div>'
        + '<div class="' + badgeClass + '">' + label + '</div>'
        + '</div>';
    }});
    container.innerHTML = html;
  }}

  // Simpan komentar ke localStorage
  function simpanKomentar(nama, komentar) {{
    var komentarList = JSON.parse(localStorage.getItem('komentarList') || '[]');
    var komentarBaru = {{
      nama: nama,
      komentar: komentar,
      waktu: new Date().toLocaleString('id-ID')
    }};
    komentarList.push(komentarBaru);
    localStorage.setItem('komentarList', JSON.stringify(komentarList));
    tampilkanKomentar();
  }}

  // Tampilkan komentar dari localStorage
  function tampilkanKomentar() {{
    var komentarList = JSON.parse(localStorage.getItem('komentarList') || '[]');
    var komentarContainer = document.getElementById('komentar-list');
    
    if (komentarList.length === 0) {{
      komentarContainer.innerHTML = '<div class="no-komentar">Belum ada komentar. Jadilah yang pertama! 🌟</div>';
      return;
    }}
    
    var html = '';
    komentarList.forEach(function(komentar) {{
      html += '<div class="komentar-item">' +
        '<div class="komentar-nama">' + komentar.nama + '</div>' +
        '<div class="komentar-teks">' + komentar.komentar + '</div>' +
        '<div class="komentar-waktu">' + komentar.waktu + '</div>' +
        '</div>';
    }});
    
    komentarContainer.innerHTML = html;
  }}



  // Optimasi gambar
  function optimizeImages() {{
    const images = document.querySelectorAll('img');
    images.forEach(img => {{
      img.loading = 'lazy';
      img.decoding = 'async';
      if (img.src.includes('DSC03210.jpg') || img.src.includes('DSC03246.jpg') || img.src.includes('DSC03249.jpg')) {{
        img.style.imageRendering = 'crisp-edges';
        img.style.imageRendering = '-webkit-optimize-contrast';
      }}
    }});
  }}

</script>

</body>
</html>
"""

# Simpan file
base_dir = os.path.dirname(os.path.abspath(__file__))
output_file = os.path.join(base_dir, "index.html")

with open(output_file, "w", encoding="utf-8") as f:
    f.write(html_template)

print(f"✅ Undangan interaktif cantik dibuat di {output_file}")