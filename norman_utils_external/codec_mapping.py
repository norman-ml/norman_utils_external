class CodecMapping:
    # Key = Norman encoding value
    # Value = Library codec name
    Container = {
        # Audio (PyAV formats)
        "aac": "adts",
        "flac": "flac",
        "mp3": "mp3",
        "ogg": "ogg",
        "wav": "wav",

        # Image (Pillow formats)
        "jpg": "JPEG",
        "png": "PNG",
        "webp": "WEBP",

        # Video (PyAV formats)
        "mkv": "matroska",
        "mov": "mov",
        "mp4": "mp4",
        "webm": "webm"
    }

    # Key = Norman encoding value
    # Value = Library codec name
    Channel = {
        # Audio (PyAV codecs)
        "aac": "aac",
        "alac": "alac",
        "flac": "flac",
        "mp3": "libmp3lame",
        "mp3_vbr": "libmp3lame",
        "opus": "libopus",
        "vorbis": "libvorbis",
        "pcm_f32le": "pcm_f32le",
        "pcm_s16le": "pcm_s16le",
        "pcm_s24le": "pcm_s24le",
        "pcm_s32le": "pcm_s32le",

        # Image (Pillow modes)
        "1": "1",
        "cmyk": "CMYK",
        "l": "L",
        "p": "P",
        "rgb": "RGB",
        "rgba": "RGBA",
        "ycbcr": "YCbCr",

        # Text / Subtitle (PyAV codecs)
        "ass": "ass",
        "mov_text": "mov_text",
        "srt": "subrip",
        "vtt": "webvtt",

        # Video (PyAV codecs)
        "av1": "libaom-av1",
        "ffv1": "ffv1",
        "h264": "libx264",
        "h265": "libx265",
        "mjpeg": "mjpeg",
        "prores_ks": "prores_ks",
        "vp8": "libvpx",
        "vp9": "libvpx-vp9"
    }
