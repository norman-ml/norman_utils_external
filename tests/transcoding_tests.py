import itertools
import os

from norman_utils.transcoders.audio.aac_transcoder import AacTranscoder
from norman_utils.transcoders.audio.mp3_transcoder import Mp3Transcoder
from norman_utils.transcoders.audio.wav_transcoder import WavTranscoder
from norman_utils.transcoders.image.jpg_transcoder import JpgTranscoder
from norman_utils.transcoders.image.png_transcoder import PngTranscoder
from norman_utils.transcoders.image.webp_transcoder import WebpTranscoder
from norman_utils.transcoders.video.video_transcoder import VideoTranscoder


def transcode_audio(input_path: str, output_path: str):
    if not os.path.exists(output_path):
        os.makedirs(output_path, exist_ok=True)

    transcoders = {
        "aac": AacTranscoder,
        "mp3": Mp3Transcoder,
        "wav": WavTranscoder
    }

    for source_format, target_format in itertools.permutations(transcoders.keys(), 2):
        source_file_path = f"{input_path}{os.sep}sample_input.{source_format}"
        target_file_path = f"{output_path}{os.sep}{source_format}_to.{target_format}"

        transcoder = transcoders[source_format]
        transcoding_method = getattr(transcoder, f"to_{target_format}")

        source_file = open(source_file_path, "rb")
        target_file = transcoding_method(source_file)
        with open(target_file_path, "wb") as disk_target_file:
            disk_target_file.write(target_file.getbuffer())

def transcode_image(input_path: str, output_path: str):
    if not os.path.exists(output_path):
        os.makedirs(output_path, exist_ok=True)

    transcoders = {
        "jpg": JpgTranscoder,
        "png": PngTranscoder,
        "webp": WebpTranscoder
    }

    for source_format, target_format in itertools.permutations(transcoders.keys(), 2):
        source_file_path = f"{input_path}{os.sep}sample_input.{source_format}"
        target_file_path = f"{output_path}{os.sep}{source_format}_to.{target_format}"

        transcoder = transcoders[source_format]
        transcoding_method = getattr(transcoder, f"to_{target_format}")

        source_file = open(source_file_path, "rb")
        target_file = transcoding_method(source_file)
        with open(target_file_path, "wb") as disk_target_file:
            disk_target_file.write(target_file.getbuffer())

def transcode_video(input_path: str, output_path: str):
    if not os.path.exists(output_path):
        os.makedirs(output_path, exist_ok=True)

    # It seems some formats do not come preinstalled with ffmpeg
    # formats = {
    #     "avi": {
    #         "container": ("avi",),
    #         "audio": ("mp3", "aac"),
    #         "video": ("libx264", "mpeg4")
    #     },
    #     "mkv": {
    #         "container": ("matroska",),
    #         "audio": ("aac", "libopus", "libvorbis", "mp3"),
    #         "video": ("libx264", "libx265", "libvpx", "libvpx-vp9")
    #     },
    #     "mov": {
    #         "container": ("mov",),
    #         "audio": ("aac", "alac", "pcm_s16le"),
    #         "video": ("libx264", "libx265", "prores", "dvsd")
    #     },
    #     "mp4": {
    #         "container": ("mp4",),
    #         "audio": ("aac", "mp3", "alac"),
    #         "video": ("libx264", "libx265", "mpeg4")
    #     },
    #     "webm": {
    #         "container": ("webm",),
    #         "audio": ("libopus", "libvorbis"),
    #         "video": ("libvpx", "libvpx-vp9")
    #     },
    #     "wmv": {
    #         "container": ("wmv",),
    #         "audio": ("wmav2",),
    #         "video": ("wmv2", "wmv3")
    #     }
    # }

    formats = {
        "mp4": {
            "container": ("mp4",),
            "audio": ("aac", "mp3", "alac"),
            "video": ("libx264", "libx265", "mpeg4")
        },
        "mkv": {
            "container": ("matroska",),
            "audio": ("aac", "libopus", "libvorbis", "mp3"),
            "video": ("libx264", "libx265", "libvpx", "libvpx-vp9")
        },
    }

    for source_file_suffix, target_file_suffix in itertools.permutations(formats.keys(), 2):
        for target_container_format in formats[target_file_suffix]["container"]:
            for target_audio_format in formats[target_file_suffix]["audio"]:
                for target_video_format in formats[target_file_suffix]["video"]:
                    print(source_file_suffix, target_file_suffix, target_container_format, target_audio_format, target_video_format)
                    source_file_path = f"{input_path}{os.sep}sample_input.{source_file_suffix}"
                    target_file_path = f"{output_path}{os.sep}{source_file_suffix}_to_{target_video_format}_{target_audio_format}.{target_file_suffix}"

                    source_file = open(source_file_path, "rb")
                    target_file = VideoTranscoder.transcode(source_file, target_container_format, target_video_format, target_audio_format)
                    with open(target_file_path, "wb") as disk_target_file:
                        disk_target_file.write(target_file.getbuffer())


if __name__ == "__main__":
    print("Starting")

    input_path = r"/tmp/sample_inputs"
    output_path = r"/tmp/sample_outputs"

    # transcode_audio(input_path, output_path)
    # transcode_image(input_path, output_path)
    transcode_video(input_path, output_path)


    print("Finished")
