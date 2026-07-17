#!/usr/bin/env python3
"""OCR all pages of 综合全文.pdf using tesseract with chi_sim."""
import fitz
import subprocess
import os
import sys
import time

PDF_PATH = r"C:\Users\82562\Downloads\fate\综合全文.pdf"
OUTPUT_DIR = r"C:\Users\82562\Downloads\fate\ocr_output"
TESSERACT = r"C:\Program Files\Tesseract-OCR\tesseract.exe"
TESSDATA = r"C:\Users\82562\Downloads\fate"
DPI = 300

os.makedirs(OUTPUT_DIR, exist_ok=True)

doc = fitz.open(PDF_PATH)
total = doc.page_count
print(f"Total pages: {total}")

start_time = time.time()

for i in range(total):
    page = doc[i]
    pix = page.get_pixmap(dpi=DPI)
    img_path = os.path.join(OUTPUT_DIR, f"page_{i+1:04d}.png")
    pix.save(img_path)
    
    # OCR with explicit encoding handling
    txt_path = os.path.join(OUTPUT_DIR, f"page_{i+1:04d}")
    result = subprocess.run(
        [TESSERACT, img_path, txt_path, "-l", "chi_sim", "--psm", "6"],
        capture_output=True, timeout=120,
        env={**os.environ, "TESSDATA_PREFIX": TESSDATA}
    )
    
    # Read the output text file tesseract created
    txt_file = txt_path + ".txt"
    if os.path.exists(txt_file):
        with open(txt_file, "r", encoding="utf-8") as f:
            text = f.read().strip()
    else:
        text = f"[OCR failed: {result.stderr.decode('utf-8', errors='replace')}]"
    
    # Clean up image to save space
    os.remove(img_path)
    
    elapsed = time.time() - start_time
    avg = elapsed / (i + 1)
    remaining = avg * (total - i - 1)
    print(f"Page {i+1}/{total} ({len(text)} chars) | ETA: {remaining/60:.1f} min")
    sys.stdout.flush()

doc.close()

# Combine all text files
full_path = os.path.join(OUTPUT_DIR, "full_text.txt")
with open(full_path, "w", encoding="utf-8") as out:
    for i in range(total):
        txt_file = os.path.join(OUTPUT_DIR, f"page_{i+1:04d}.txt")
        if os.path.exists(txt_file):
            with open(txt_file, "r", encoding="utf-8") as f:
                content = f.read().strip()
            out.write(f"=== 第 {i+1} 页 ===\n{content}\n\n")

print(f"\nDone! Full text saved to: {full_path}")
print(f"Total time: {(time.time()-start_time)/60:.1f} min")
