"""PaddleOCR Demo - OCR using PaddleOCR library."""

import argparse
import sys
from pathlib import Path

from paddleocr import PaddleOCR


def main():
    parser = argparse.ArgumentParser(description="OCR demo using PaddleOCR")
    parser.add_argument("image", help="Path to the image file")
    parser.add_argument(
        "-l",
        "--lang",
        default="japan",
        help="Language code (default: japan). Options: en, japan, ch, etc.",
    )
    args = parser.parse_args()

    image_path = Path(args.image)
    if not image_path.exists():
        print(f"Error: Image not found: {image_path}", file=sys.stderr)
        sys.exit(1)

    print(f"Image: {image_path}")
    print(f"Language: {args.lang}")
    print()

    print("Initializing PaddleOCR...")
    ocr = PaddleOCR(
        lang=args.lang,
        use_doc_orientation_classify=False,  # 文書向き検出OFF
        use_doc_unwarping=False,  # 歪み補正OFF
        use_textline_orientation=False,  # テキスト行向き検出OFF
    )

    print("Performing OCR...")
    results = ocr.predict(str(image_path))

    print("\n" + "=" * 50)
    print("Results")
    print("=" * 50)

    count = 0
    for result in results:
        if "rec_texts" not in result:
            continue
        texts = result["rec_texts"]
        scores = result["rec_scores"]
        for text, confidence in zip(texts, scores):
            count += 1
            print(f"\n[{count}] {text}")
            print(f"    Confidence: {confidence:.2%}")

    print("\n" + "=" * 50)
    print(f"Total: {count} text regions detected")


if __name__ == "__main__":
    main()
