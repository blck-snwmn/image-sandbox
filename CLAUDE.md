# image-sandbox

Experimental repository for image processing. Trying various image processing techniques with different languages and libraries.

## Target Processing

Experimenting with various image-related processing. Examples:
- Background removal
- Polygonization
- OCR
- Machine learning (MediaPipe, etc.)
- Other image processing in general

## Directory Structure

```
/<language>/
  ├── <processing>/
  │   └── ...
  └── <processing>/
      └── ...
```

Example:
```
/python/
  ├── ocr/
  ├── background-removal/
  └── mediapipe/
/go/
  └── ocr/
/rust/
  └── polygon/
```

Create subdirectories for each processing type under each language directory.

## Default Tools

- **Python**: Use `uv` for package management and virtual environments
- **TypeScript**: Use `bun` as the runtime and package manager
