"""Tesseract OCR Demo - OCR using pytesseract (Google Tesseract)."""

import argparse
import sys
from pathlib import Path

import pytesseract
from PIL import Image


def main():
    parser = argparse.ArgumentParser(description="OCR demo using pytesseract")
    parser.add_argument("image", help="Path to the image file")
    parser.add_argument(
        "-l",
        "--lang",
        default="jpn+eng",
        help="Language code (default: jpn+eng). Options: eng, jpn, jpn+eng, etc.",
    )
    args = parser.parse_args()

    image_path = Path(args.image)
    if not image_path.exists():
        print(f"Error: Image not found: {image_path}", file=sys.stderr)
        sys.exit(1)

    print(f"Image: {image_path}")
    print(f"Language: {args.lang}")
    print()

    img = Image.open(image_path)

    print("Performing OCR...")

    # テキスト抽出
    text = pytesseract.image_to_string(img, lang=args.lang)

    print("\n" + "=" * 50)
    print("Results (Text)")
    print("=" * 50)
    print(text)

    # 詳細情報（単語ごとの信頼度）
    print("\n" + "=" * 50)
    print("Results (Details)")
    print("=" * 50)

    data = pytesseract.image_to_data(img, lang=args.lang, output_type=pytesseract.Output.DICT)

    count = 0
    for i, word in enumerate(data["text"]):
        conf = data["conf"][i]
        if word.strip() and conf > 0:
            count += 1
            print(f"[{count}] {word} ({conf}%)")

    print("\n" + "=" * 50)
    print(f"Total: {count} words detected")


if __name__ == "__main__":
    main()
