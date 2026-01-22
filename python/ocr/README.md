# OCR Demo

OCR demo using EasyOCR, PaddleOCR, and Tesseract.

## Setup

```bash
cd python/ocr
uv sync

# Tesseract requires separate installation
brew install tesseract tesseract-lang
```

## Usage

### EasyOCR

```bash
# Japanese + English (default)
uv run python easyocr_demo.py samples/test-ocr-ja.jpeg

# English only
uv run python easyocr_demo.py samples/test-ocr.jpeg -l en
```

### PaddleOCR

```bash
# Japanese (default)
uv run python paddle_demo.py samples/test-ocr-ja.jpeg

# English
uv run python paddle_demo.py samples/test-ocr.jpeg -l en
```

### Tesseract

```bash
# Japanese + English (default)
uv run python tesseract_demo.py samples/test-ocr-ja.jpeg

# English
uv run python tesseract_demo.py samples/test-ocr.jpeg
```

## Language Codes

| Library | Japanese | English | Chinese |
|---------|----------|---------|---------|
| EasyOCR | `ja` | `en` | `ch_sim` |
| PaddleOCR | `japan` | `en` | `ch` |
| Tesseract | `jpn` | `eng` | `chi_sim` |

## Benchmark Results

### test-ocr.jpeg (English receipt)

| Text | EasyOCR | PaddleOCR | Tesseract |
|------|---------|-----------|-----------|
| GREEN | 99% | 99% | - |
| MEADOWS | 23% (MEADロwS) | 99% | - |
| GROCERS | 36% (GRDCERS) | 99% | - |
| Milk | 65% | 98% | - |
| Bread | 99% | 99% | - |
| Apples | 99% | 99% | - |
| Eggs | 95% | 99% | - |
| Avocado | 99% | 99% | - |
| TOTAL | 87% | 99% | - |

### test-ocr-ja.jpeg (Handwritten Japanese)

| Text | EasyOCR | PaddleOCR | Tesseract |
|------|---------|-----------|-----------|
| 14時から会議(A会議室) | 20% (`{時から会議(義)`) | 97% ✅ | ❌ |
| 田中さんに資料送付 | 96% ✅ | 99% ✅ | ❌ |
| 備品発注の確認 | 57% | 99% ✅ | ❌ |
