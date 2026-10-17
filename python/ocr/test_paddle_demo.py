"""Deterministic smoke tests for the PaddleOCR demo."""

import sys
import unittest
from pathlib import Path
from unittest.mock import MagicMock, patch

import paddle_demo


class PaddleDemoSmokeTest(unittest.TestCase):
    def test_initializes_official_pipeline_and_runs_prediction(self):
        """Exercise PaddleOCR's public constructor and prediction wrapper offline."""
        sample = Path(__file__).parent / "samples" / "test-ocr.jpeg"
        pipeline = MagicMock()
        pipeline.predict.return_value = iter(
            [{"rec_texts": ["smoke text"], "rec_scores": [0.99]}]
        )
        create_pipeline_patch = patch(
            "paddleocr._pipelines.base.create_pipeline", return_value=pipeline
        )

        with (
            create_pipeline_patch as create_pipeline,
            patch.object(sys, "argv", ["paddle_demo.py", str(sample), "--lang", "en"]),
            patch("builtins.print") as print_mock,
        ):
            paddle_demo.main()

        create_pipeline.assert_called_once()
        config = create_pipeline.call_args.kwargs["config"]
        self.assertEqual(config["pipeline_name"], "OCR")
        self.assertFalse(config["use_doc_preprocessor"])
        self.assertFalse(config["use_textline_orientation"])
        self.assertEqual(
            config["SubModules"]["TextDetection"]["model_name"],
            "PP-OCRv6_medium_det",
        )
        self.assertEqual(
            config["SubModules"]["TextRecognition"]["model_name"],
            "PP-OCRv6_medium_rec",
        )

        pipeline.predict.assert_called_once_with(
            str(sample),
            use_doc_orientation_classify=None,
            use_doc_unwarping=None,
            use_textline_orientation=None,
            text_det_limit_side_len=None,
            text_det_limit_type=None,
            text_det_thresh=None,
            text_det_box_thresh=None,
            text_det_unclip_ratio=None,
            text_rec_score_thresh=None,
            return_word_box=None,
        )
        print_mock.assert_any_call("\n[1] smoke text")
        print_mock.assert_any_call("    Confidence: 99.00%")
        print_mock.assert_any_call("Total: 1 text regions detected")


if __name__ == "__main__":
    unittest.main()
