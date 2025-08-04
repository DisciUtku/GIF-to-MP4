#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import subprocess
import sys

def test_ffmpeg():
    print("FFmpeg Installation Test")
    print("=" * 30)
    
    try:
        result = subprocess.run(["ffmpeg", "-version"], 
                              capture_output=True, text=True, timeout=10)
        
        if result.returncode == 0:
            print("✅ FFmpeg found successfully!")
            print(f"Version: {result.stdout.split('ffmpeg version')[1].split()[0]}")
            print("\nFFmpeg installation completed. You can use the GIF to MP4 converter.")
            return True
        else:
            print("❌ FFmpeg found but could not be executed.")
            return False
            
    except FileNotFoundError:
        print("❌ FFmpeg not found!")
        print("\nTo install FFmpeg:")
        print("1. Go to https://ffmpeg.org/download.html")
        print("2. Download FFmpeg for Windows")
        print("3. Extract the downloaded file")
        print("4. Add the bin folder to your system PATH")
        print("5. Run this test again")
        return False
        
    except subprocess.TimeoutExpired:
        print("❌ FFmpeg did not respond (timeout)")
        return False
        
    except Exception as e:
        print(f"❌ Unexpected error: {e}")
        return False

if __name__ == "__main__":
    success = test_ffmpeg()
    if not success:
        sys.exit(1)
    else:
        print("\n🎉 Test successful! You're ready to use the program.") 