# As there are multiple encoders for each canonical encoding name
# We chose the best implementation we could find within reasonable research time
from norman_objects.shared.codecs.channel_codec import ChannelCodec
from norman_objects.shared.codecs.container_codec import ContainerCodec
from norman_objects.shared.encoding.channel_encoding import ChannelEncoding
from norman_objects.shared.encoding.container_encoding import ContainerEncoding


class CodecMapping:

    Container_Encoders = {
        # Audio (PyAV formats)
        ContainerEncoding.Aac: ContainerCodec.Adts,
        ContainerEncoding.Flac: ContainerCodec.Flac,
        ContainerEncoding.Mp3: ContainerCodec.Mp3,
        ContainerEncoding.Ogg: ContainerCodec.Ogg,
        ContainerEncoding.Wav: ContainerCodec.Wav,

        # Image (Pillow formats)
        ContainerEncoding.Jpg: ContainerCodec.Jpeg,
        ContainerEncoding.Png: ContainerCodec.Png,
        ContainerEncoding.WebP: ContainerCodec.WebP,

        # Video (PyAV formats)
        ContainerEncoding.Mkv: ContainerCodec.Matroska,
        ContainerEncoding.Mov: ContainerCodec.Mov,
        ContainerEncoding.Mp4: ContainerCodec.Mp4,
        ContainerEncoding.WebM: ContainerCodec.WebM
    }

    Container_Decoders = {
        # Audio (PyAV formats)
        ContainerCodec.Aac: ContainerEncoding.Aac,
        ContainerCodec.Adts: ContainerEncoding.Aac,
        ContainerCodec.Flac: ContainerEncoding.Flac,
        ContainerCodec.Mp3: ContainerEncoding.Mp3,
        ContainerCodec.Ogg: ContainerEncoding.Ogg,
        ContainerCodec.Wav: ContainerEncoding.Wav,

        # Image (Pillow formats)
        ContainerCodec.Jpeg: ContainerEncoding.Jpg,
        ContainerCodec.Png: ContainerEncoding.Png,
        ContainerCodec.WebP: ContainerEncoding.WebP,

        # Video (PyAV formats)
        ContainerCodec.Matroska: ContainerEncoding.Mkv,
        ContainerCodec.MatroskaWebm: ContainerEncoding.Mkv,
        ContainerCodec.Mov: ContainerEncoding.Mov,
        ContainerCodec.MovMp4M4a3gp3g2Mj2: ContainerEncoding.Mp4,
        ContainerCodec.Mp4: ContainerEncoding.Mp4,
        ContainerCodec.WebM: ContainerEncoding.WebM
    }

    Channel_Encoders = {
        # Audio (PyAV codecs)
        ChannelEncoding.Aac: ChannelCodec.Aac,
        ChannelEncoding.Alac: ChannelCodec.Alac,
        ChannelEncoding.Flac: ChannelCodec.Flac,
        ChannelEncoding.Mp3: ChannelCodec.LibMp3Lame,
        ChannelEncoding.Mp3Vbr: ChannelCodec.LibMp3Lame,
        ChannelEncoding.Opus: ChannelCodec.LibOpus,
        ChannelEncoding.PcmF32Le: ChannelCodec.PcmF32Le,
        ChannelEncoding.PcmS16Le: ChannelCodec.PcmS16Le,
        ChannelEncoding.PcmS24Le: ChannelCodec.PcmS24Le,
        ChannelEncoding.PcmS32Le: ChannelCodec.PcmS32Le,
        ChannelEncoding.Vorbis: ChannelCodec.LibVorbis,

        # Image (Pillow modes)
        ChannelEncoding.One: ChannelCodec.One,
        ChannelEncoding.Cmyk: ChannelCodec.Cmyk,
        ChannelEncoding.L: ChannelCodec.L,
        ChannelEncoding.P: ChannelCodec.P,
        ChannelEncoding.Rgb: ChannelCodec.Rgb,
        ChannelEncoding.Rgba: ChannelCodec.Rgba,
        ChannelEncoding.YCbCr: ChannelCodec.YCbCr,

        # Text / Subtitle (PyAV codecs)
        ChannelEncoding.Ass: ChannelCodec.Ass,
        ChannelEncoding.MovText: ChannelCodec.MovText,
        ChannelEncoding.Srt: ChannelCodec.Subrip,
        ChannelEncoding.Vtt: ChannelCodec.Webvtt,
        # "kate": "???" # TODO: build ffmpeg on vm with kate codecs and rebundle ami to enable support

        # Video (PyAV codecs)
        ChannelEncoding.Av1: ChannelCodec.LibaomAv1,
        ChannelEncoding.Ffv1: ChannelCodec.Ffv1,
        ChannelEncoding.H264: ChannelCodec.Libx264,
        ChannelEncoding.H265: ChannelCodec.Libx265,
        ChannelEncoding.Mjpeg: ChannelCodec.Mjpeg,
        ChannelEncoding.ProresKs: ChannelCodec.ProresKs,
        ChannelEncoding.Vp8: ChannelCodec.Libvpx,
        ChannelEncoding.Vp9: ChannelCodec.LibvpxVp9
    }

    Channel_Decoders = {
        # Audio (PyAV codecs)
        ChannelCodec.Aac: ChannelEncoding.Aac,
        ChannelCodec.AacFixed: ChannelEncoding.Aac,
        ChannelCodec.AacLatm: ChannelEncoding.Aac,
        ChannelCodec.Alac: ChannelEncoding.Alac,
        ChannelCodec.Flac: ChannelEncoding.Flac,
        ChannelCodec.Mp3: ChannelEncoding.Mp3,
        ChannelCodec.Mp3Adu: ChannelEncoding.Mp3,
        ChannelCodec.Mp3AduFloat: ChannelEncoding.Mp3,
        ChannelCodec.Mp3Float: ChannelEncoding.Mp3,
        ChannelCodec.Mp3On4: ChannelEncoding.Mp3,
        ChannelCodec.Mp3On4Float: ChannelEncoding.Mp3,
        ChannelCodec.LibOpus: ChannelEncoding.Opus,
        ChannelCodec.Opus: ChannelEncoding.Opus,
        ChannelCodec.PcmF32Be: ChannelEncoding.PcmF32Le,
        ChannelCodec.PcmF32Le: ChannelEncoding.PcmF32Le,
        ChannelCodec.PcmS16Be: ChannelEncoding.PcmS16Le,
        ChannelCodec.PcmS16BePlanar: ChannelEncoding.PcmS16Le,
        ChannelCodec.PcmS16Le: ChannelEncoding.PcmS16Le,
        ChannelCodec.PcmS16LePlanar: ChannelEncoding.PcmS16Le,
        ChannelCodec.PcmS24Be: ChannelEncoding.PcmS24Le,
        ChannelCodec.PcmS24Le: ChannelEncoding.PcmS24Le,
        ChannelCodec.PcmS24LePlanar: ChannelEncoding.PcmS24Le,
        ChannelCodec.PcmS32Be: ChannelEncoding.PcmS32Le,
        ChannelCodec.PcmS32Le: ChannelEncoding.PcmS32Le,
        ChannelCodec.PcmS32LePlanar: ChannelEncoding.PcmS32Le,
        ChannelCodec.LibVorbis: ChannelEncoding.Vorbis,
        ChannelCodec.Vorbis: ChannelEncoding.Vorbis,

        # Image (Pillow modes)
        ChannelCodec.One: ChannelEncoding.One,
        ChannelCodec.Cmyk: ChannelEncoding.Cmyk,
        ChannelCodec.L: ChannelEncoding.L,
        ChannelCodec.P: ChannelEncoding.P,
        ChannelCodec.Rgb: ChannelEncoding.Rgb,
        ChannelCodec.Rgba: ChannelEncoding.Rgba,
        ChannelCodec.YCbCr: ChannelEncoding.YCbCr,

        # Text / Subtitle (PyAV codecs)
        ChannelCodec.Ass: ChannelEncoding.Ass,
        ChannelCodec.Ssa: ChannelEncoding.Ass,
        ChannelCodec.MovText: ChannelEncoding.MovText,
        ChannelCodec.Srt: ChannelEncoding.Srt,
        ChannelCodec.Subrip: ChannelEncoding.Srt,
        ChannelCodec.Webvtt: ChannelEncoding.Vtt,

        # Video (PyAV codecs)
        ChannelCodec.Av1: ChannelEncoding.Av1,
        ChannelCodec.Av1Cuvid: ChannelEncoding.Av1,
        ChannelCodec.LibaomAv1: ChannelEncoding.Av1,
        ChannelCodec.LibDav1d: ChannelEncoding.Av1,
        ChannelCodec.Ffv1: ChannelEncoding.Ffv1,
        ChannelCodec.H264: ChannelEncoding.H264,
        ChannelCodec.H264Cuvid: ChannelEncoding.H264,
        ChannelCodec.H264V4l2m2m: ChannelEncoding.H264,
        ChannelCodec.LibOpenH264: ChannelEncoding.H264,
        ChannelCodec.Hevc: ChannelEncoding.H265,
        ChannelCodec.HevcCuvid: ChannelEncoding.H265,
        ChannelCodec.HevcV4l2m2m: ChannelEncoding.H265,
        ChannelCodec.Mjpeg: ChannelEncoding.Mjpeg,
        ChannelCodec.MjpegB: ChannelEncoding.Mjpeg,
        ChannelCodec.MjpegCuvid: ChannelEncoding.Mjpeg,
        ChannelCodec.Prores: ChannelEncoding.ProresKs,
        ChannelCodec.ProresAw: ChannelEncoding.ProresKs,
        ChannelCodec.ProresKs: ChannelEncoding.ProresKs,
        ChannelCodec.ProresRaw: ChannelEncoding.ProresKs,
        ChannelCodec.Theora: ChannelEncoding.Vp8,
        ChannelCodec.Libvpx: ChannelEncoding.Vp8,
        ChannelCodec.Vp8: ChannelEncoding.Vp8,
        ChannelCodec.Vp8Cuvid: ChannelEncoding.Vp8,
        ChannelCodec.Vp8V4l2m2m: ChannelEncoding.Vp8,
        ChannelCodec.LibvpxVp9: ChannelEncoding.Vp9,
        ChannelCodec.Vp9: ChannelEncoding.Vp9,
        ChannelCodec.Vp9Cuvid: ChannelEncoding.Vp9,
        ChannelCodec.Vp9V4l2m2m: ChannelEncoding.Vp9
    }
