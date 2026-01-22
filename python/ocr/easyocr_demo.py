"""EasyOCR Demo - OCR using EasyOCR library."""

import argparse
import sys
from pathlib import Path

import easyocr


def main():
    parser = argparse.ArgumentParser(description="OCR demo using EasyOCR")
    parser.add_argument("image", help="Path to the image file")
    parser.add_argument(
        "-l",
        "--languages",
        nargs="+",
        default=["ja", "en"],
        help="Language codes (default: ja en)",
    )
    parser.add_argument("--gpu", action="store_true", help="Use GPU if available")
    args = parser.parse_args()

    image_path = Path(args.image)
    if not image_path.exists():
        print(f"Error: Image not found: {image_path}", file=sys.stderr)
        sys.exit(1)

    print(f"Image: {image_path}")
    print(f"Languages: {args.languages}")
    print(f"GPU: {args.gpu}")
    print()

    print("Initializing EasyOCR reader...")
    reader = easyocr.Reader(args.languages, gpu=args.gpu)

    print("Performing OCR...")
    results = reader.readtext(str(image_path))

    print("\n" + "=" * 50)
    print("Results")
    print("=" * 50)

    for i, (bbox, text, confidence) in enumerate(results, 1):
        print(f"\n[{i}] {text}")
        print(f"    Confidence: {confidence:.2%}")

    print("\n" + "=" * 50)
    print(f"Total: {len(results)} text regions detected")


if __name__ == "__main__":
    main()
