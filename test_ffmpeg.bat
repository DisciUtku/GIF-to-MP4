@echo off
chcp 65001 >nul
title FFmpeg Installation Test
echo Starting FFmpeg installation test...
echo.
python test_ffmpeg.py
echo.
pause 