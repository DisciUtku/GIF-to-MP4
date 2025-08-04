# GIF to MP4 Converter

This program is a simple and lightweight GUI application that batch converts all GIF files in a selected folder to MP4 format.

## Features

-  **GIF Conversion**: Converts GIF files to MP4 format
-  **Batch Processing**: Automatically finds all GIF files in the folder
-  **Fast Conversion**: Optimized conversion using FFmpeg

## Requirements

### System Requirements
- Windows 10/11
- Python 3.7 or higher
- FFmpeg (see installation instructions below)

### Python Libraries
This program uses only standard Python libraries:
- `tkinter` (for GUI)
- `subprocess` (for FFmpeg calls)
- `threading` (to prevent interface freezing)
- `os` and `pathlib` (for file operations)

## Installation

### 1. FFmpeg Installation

Follow these steps to install FFmpeg:

1. Go to the [FFmpeg official site](https://ffmpeg.org/download.html)
2. Click on "Windows" section, then "Windows builds" link
3. Click on "Windows builds from gyan.dev" link
4. Download "ffmpeg-git-full.7z" file
5. Extract the downloaded file
6. Add the `bin` folder from the extracted folder to your system PATH:
   - System Properties → Advanced System Settings → Environment Variables
   - Select "Path" variable and click "Edit"
   - Click "New" and add the full path to FFmpeg's bin folder
   - Example: `C:\ffmpeg\bin`

### 2. Program Installation

1. Download this project to your computer
2. Navigate to the project folder in command line
3. Run the program:
   ```bash
   python gif_to_mp4_converter.py
   ```

### 3. Easy Startup

You can double-click the `start.bat` file to start the program.

## 📖 Usage

1. **Start Program**: Run `start.bat` file
2. **Select Folder**: Click "Select Folder" button
3. **Select the folder containing GIF files**
4. **Start Conversion**: Click "Start Conversion" button
5. **Wait for Completion**: Follow the progress bar
6. **Check Results**: Find your MP4 files in the "Outputs" folder

##  Output Details

- **Output Folder**: "Outputs" folder is created inside the selected folder
- **File Names**: Original file names are preserved, only extension becomes .mp4
- **Example**: `animation.gif` → `Outputs/animation.mp4`

##  Supported Formats

- **GIF**: Animated GIF files (most common format)

## Technical Details

### Conversion Parameters
- **Video Codec**: H.264 (libx264)
- **Pixel Format**: yuv420p (for wide compatibility)
- **Quality**: Original GIF quality is preserved


## Troubleshooting

### FFmpeg Not Found Error
- Make sure FFmpeg is installed correctly
- Check that FFmpeg's bin folder is added to your system PATH
- Test by running `ffmpeg -version` in command line

### Conversion Error
- Make sure GIF files are not corrupted
- Ensure there are no Turkish characters in file paths
- Make sure you have sufficient disk space

### Program Won't Start
- Make sure Python is installed
- Test by running `python --version` in command line

## License

This project is open source and can be used for educational purposes.

## Contributing

For bug reports or feature suggestions, please open an issue on GitHub.

---

**Note**: This program uses FFmpeg and is subject to FFmpeg's license terms. 
