# As there are multiple encoders for each canonical encoding name
# We chose the best implementation we could find within reasonable research time
class CodecMapping:
    # Key = Norman encoding value
    # Value = Library codec name
    ContainerEncoders = {
        # Audio (PyAV formats)
        "aac": "adts",
        "flac": "flac",
        "mp3": "mp3",
        "ogg": "ogg",
        "wav": "wav",
        
        # Image (Pillow formats)
        "jpg": "jpeg",
        "png": "png",
        "webp": "webp",

        # Video (PyAV formats)
        "mkv": "matroska",
        "mov": "mov",
        "mp4": "mp4",
        "webm": "webm"
    }

    # Key = Library codec name
    # Value = Norman encoding value
    ContainerDecoders = {
        # Audio (PyAV formats)
        "aac": "aac",
        "adts": "aac",
        "flac": "flac",
        "mp3": "mp3",
        "ogg": "ogg",
        "wav": "wav",

        # Image (Pillow formats)
        "jpeg": "jpg",
        "png": "png",
        "webp": "webp",

        # Video (PyAV formats)
        "matroska": "mkv",
        "matroska,webm": "mkv",
        "mov": "mov",
        "mov,mp4,m4a,3gp,3g2,mj2": "mp4",
        "mp4": "mp4",
        "webm": "webm"
    }

    # Key = Norman encoding value
    # Value = Library codec name
    Channel_Encoders = {
        # Audio (PyAV codecs)
        "aac": "aac",
        "alac": "alac",
        "flac": "flac",
        "mp3": "libmp3lame",
        "mp3_vbr": "libmp3lame",
        "opus": "libopus",
        "pcm_f32le": "pcm_f32le",
        "pcm_s16le": "pcm_s16le",
        "pcm_s24le": "pcm_s24le",
        "pcm_s32le": "pcm_s32le",
        "vorbis": "libvorbis",

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
        # "kate": "???" # TODO: build ffmpeg on vm with kate codecs and rebundle ami to enable support

        # Video (PyAV codecs)
        "av1": "libaom-av1",
        "ffv1": "ffv1",
        "h264": "libx264",
        "h265": "libx265",
        "mjpeg": "mjpeg",
        "prores_ks": "prores_ks",
        "theora": "theora",  # Note: encoder not available in your build, only decoder
        "vp8": "libvpx",
        "vp9": "libvpx-vp9"
    }

    # Key = Library codec name
    # Value = Norman encoding value
    Channel_Decoders = {
        # Audio (PyAV codecs)
        "aac": "aac",
        "aac_fixed": "aac",
        "aac_latm": "aac",
        "alac": "alac",
        "flac": "flac",
        "mp3": "mp3",
        "mp3adu": "mp3",
        "mp3adufloat": "mp3",
        "mp3float": "mp3",
        "mp3on4": "mp3",
        "mp3on4float": "mp3",
        "libopus": "opus",
        "opus": "opus",
        "pcm_f32be": "pcm_f32le",
        "pcm_f32le": "pcm_f32le",
        "pcm_s16be": "pcm_s16le",
        "pcm_s16be_planar": "pcm_s16le",
        "pcm_s16le": "pcm_s16le",
        "pcm_s16le_planar": "pcm_s16le",
        "pcm_s24be": "pcm_s24le",
        "pcm_s24le": "pcm_s24le",
        "pcm_s24le_planar": "pcm_s24le",
        "pcm_s32be": "pcm_s32le",
        "pcm_s32le": "pcm_s32le",
        "pcm_s32le_planar": "pcm_s32le",
        "libvorbis": "vorbis",
        "vorbis": "vorbis",

        # Image (Pillow modes)
        "1": "1",
        "CMYK": "cmyk",
        "L": "l",
        "P": "p",
        "RGB": "rgb",
        "RGBA": "rgba",
        "YCbCr": "ycbcr",

        # Text / Subtitle (PyAV codecs)
        "ass": "ass",
        "ssa": "ass",
        "mov_text": "mov_text",
        "srt": "srt",
        "subrip": "srt",
        "webvtt": "vtt",

        # Video (PyAV codecs)
        "av1": "av1",
        "av1_cuvid": "av1",
        "libaom-av1": "av1",
        "libdav1d": "av1",
        "ffv1": "ffv1",
        "h264": "h264",
        "h264_cuvid": "h264",
        "h264_v4l2m2m": "h264",
        "libopenh264": "h264",
        "hevc": "h265",
        "hevc_cuvid": "h265",
        "hevc_v4l2m2m": "h265",
        "mjpeg": "mjpeg",
        "mjpegb": "mjpeg",
        "mjpeg_cuvid": "mjpeg",
        "prores": "prores_ks",
        "prores_aw": "prores_ks",
        "prores_ks": "prores_ks",
        "prores_raw": "prores_ks",
        "theora": "theora",
        "libvpx": "vp8",
        "vp8": "vp8",
        "vp8_cuvid": "vp8",
        "vp8_v4l2m2m": "vp8",
        "libvpx-vp9": "vp9",
        "vp9": "vp9",
        "vp9_cuvid": "vp9",
        "vp9_v4l2m2m": "vp9"
    }
