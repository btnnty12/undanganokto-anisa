#!/usr/bin/env python3
"""
Script untuk mengompres gambar undangan digital
Mengurangi ukuran file untuk performa yang lebih baik
"""

import os
from PIL import Image
import shutil

def compress_image(input_path, output_path, quality=85, max_width=1920, max_height=1080):
    """
    Kompres gambar dengan kualitas dan ukuran yang optimal
    
    Args:
        input_path: Path gambar asli
        output_path: Path gambar hasil kompres
        quality: Kualitas JPEG (1-100)
        max_width: Lebar maksimal
        max_height: Tinggi maksimal
    """
    try:
        with Image.open(input_path) as img:
            # Konversi ke RGB jika RGBA
            if img.mode in ('RGBA', 'LA', 'P'):
                img = img.convert('RGB')
            
            # Resize jika terlalu besar
            if img.width > max_width or img.height > max_height:
                img.thumbnail((max_width, max_height), Image.Resampling.LANCZOS)
            
            # Simpan dengan kompresi
            img.save(output_path, 'JPEG', quality=quality, optimize=True)
            
            # Hitung pengurangan ukuran
            original_size = os.path.getsize(input_path)
            compressed_size = os.path.getsize(output_path)
            reduction = ((original_size - compressed_size) / original_size) * 100
            
            print(f"✅ {os.path.basename(input_path)}: {original_size/1024/1024:.1f}MB → {compressed_size/1024/1024:.1f}MB ({reduction:.1f}% reduction)")
            
            return True
            
    except Exception as e:
        print(f"❌ Error compressing {input_path}: {str(e)}")
        return False

def main():
    # Direktori kerja
    base_dir = "/Users/ratukemala/undangan"
    
    # Buat folder untuk gambar yang sudah dikompres
    compressed_dir = os.path.join(base_dir, "compressed")
    if not os.path.exists(compressed_dir):
        os.makedirs(compressed_dir)
    
    # Daftar gambar yang perlu dikompres
    images_to_compress = [
        # Gambar utama
        "DSC03210.jpg",  # Cover photo
        "DSC03246.jpg",  # Foto wanita
        "DSC03249.jpg",  # Foto pria
        "ortu.jpeg",     # Foto keluarga
        
        # Galeri
        "foto1.jpg", "foto2.jpg", "foto3.jpg",
        "foto4.jpg", "foto5.jpg", "foto6.jpg", 
        "foto7.jpg", "foto8.jpg", "foto9.jpg",
        
        # Background
        "tapis.jpg"
    ]
    
    print("🖼️  Memulai kompresi gambar...")
    print("=" * 50)
    
    total_original = 0
    total_compressed = 0
    success_count = 0
    
    for image_name in images_to_compress:
        input_path = os.path.join(base_dir, image_name)
        output_path = os.path.join(compressed_dir, image_name)
        
        if os.path.exists(input_path):
            # Hitung ukuran asli
            original_size = os.path.getsize(input_path)
            total_original += original_size
            
            # Kompres gambar
            if compress_image(input_path, output_path, quality=85, max_width=1920, max_height=1080):
                success_count += 1
                total_compressed += os.path.getsize(output_path)
        else:
            print(f"⚠️  File tidak ditemukan: {image_name}")
    
    print("=" * 50)
    print(f"📊 Hasil Kompresi:")
    print(f"   ✅ Berhasil: {success_count}/{len(images_to_compress)} gambar")
    print(f"   📦 Ukuran asli: {total_original/1024/1024:.1f} MB")
    print(f"   📦 Ukuran setelah kompres: {total_compressed/1024/1024:.1f} MB")
    print(f"   💾 Penghematan: {((total_original - total_compressed)/total_original)*100:.1f}%")
    print(f"   💾 Hemat: {(total_original - total_compressed)/1024/1024:.1f} MB")
    
    # Backup gambar asli
    backup_dir = os.path.join(base_dir, "original_backup")
    if not os.path.exists(backup_dir):
        os.makedirs(backup_dir)
        print(f"\n📁 Membuat backup di: {backup_dir}")
        
        for image_name in images_to_compress:
            input_path = os.path.join(base_dir, image_name)
            backup_path = os.path.join(backup_dir, image_name)
            if os.path.exists(input_path):
                shutil.copy2(input_path, backup_path)
    
    print(f"\n🎉 Kompresi selesai! Gambar tersimpan di: {compressed_dir}")
    print("💡 Langkah selanjutnya: Update HTML untuk menggunakan gambar yang sudah dikompres")

if __name__ == "__main__":
    main()
