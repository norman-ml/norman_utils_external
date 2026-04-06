from norman_objects.shared.encoding.channel_encoding import ChannelEncoding
from norman_objects.shared.encoding.container_encoding import ContainerEncoding
from norman_objects.shared.encoding.sample_encoding import SampleEncoding
from norman_objects.shared.encoding.tensor_encoding import TensorEncoding
from norman_objects.shared.modality.channel_modality import ChannelModality
from norman_objects.shared.modality.container_modality import ContainerModality
from norman_objects.shared.representation.parameter_representation import ParameterRepresentation


class EncodingDefaults:
    Container_Map = {
        ContainerModality.Audio: ContainerEncoding.Mp3,
        ContainerModality.Image: ContainerEncoding.Jpg,
        ContainerModality.Text: ContainerEncoding.Txt,
        ContainerModality.Video: ContainerEncoding.Mp4
    }

    Channel_Map = {
        ContainerModality.Audio: {
            ContainerEncoding.Aac: [
                ParameterRepresentation(
                    channel_modality=ChannelModality.Audio,
                    channel_encoding=ChannelEncoding.Aac,
                    sample_encoding=SampleEncoding.FltP,
                    tensor_encoding=TensorEncoding.Float32
                )
            ],
            ContainerEncoding.Flac: [
                ParameterRepresentation(
                    channel_modality=ChannelModality.Audio,
                    channel_encoding=ChannelEncoding.Flac,
                    sample_encoding=SampleEncoding.S16,
                    tensor_encoding=TensorEncoding.Float32
                )
            ],
            ContainerEncoding.Mp3: [
                ParameterRepresentation(
                    channel_modality=ChannelModality.Audio,
                    channel_encoding=ChannelEncoding.Mp3,
                    sample_encoding=SampleEncoding.FltP,
                    tensor_encoding=TensorEncoding.Float32
                )
            ],
            ContainerEncoding.Ogg: [
                ParameterRepresentation(
                    channel_modality=ChannelModality.Audio,
                    channel_encoding=ChannelEncoding.Opus,
                    sample_encoding=SampleEncoding.Flt,
                    tensor_encoding=TensorEncoding.Float32
                )
            ],
            ContainerEncoding.Wav: [
                ParameterRepresentation(
                    channel_modality=ChannelModality.Audio,
                    channel_encoding=ChannelEncoding.PcmS16Le,
                    sample_encoding=SampleEncoding.S16,
                    tensor_encoding=TensorEncoding.Float32
                )
            ]
        },
        ContainerModality.File: {
            ContainerEncoding.Bin: [
                ParameterRepresentation(
                    channel_modality=ChannelModality.Text,
                    channel_encoding=ChannelEncoding.Utf8,
                    sample_encoding=SampleEncoding.U8,
                    tensor_encoding=TensorEncoding.Float32
                )
            ],
            ContainerEncoding.Pt: [
                ParameterRepresentation(
                    channel_modality=ChannelModality.Text,
                    channel_encoding=ChannelEncoding.Utf8,
                    sample_encoding=SampleEncoding.U8,
                    tensor_encoding=TensorEncoding.Float32
                )
            ],
            ContainerEncoding.Zip: [
                ParameterRepresentation(
                    channel_modality=ChannelModality.Text,
                    channel_encoding=ChannelEncoding.Utf8,
                    sample_encoding=SampleEncoding.U8,
                    tensor_encoding=TensorEncoding.Float32
                )
            ]
        },
        ContainerModality.Float: {
            ContainerEncoding.Txt: [
                ParameterRepresentation(
                    channel_modality=ChannelModality.Float,
                    channel_encoding=ChannelEncoding.Utf8,
                    sample_encoding=SampleEncoding.U8,
                    tensor_encoding=TensorEncoding.Float32
                )
            ]
        },
        ContainerModality.Image: {
            ContainerEncoding.Jpg: [
                ParameterRepresentation(
                    channel_modality=ChannelModality.Image,
                    channel_encoding=ChannelEncoding.Rgb,
                    sample_encoding=SampleEncoding.U8,
                    tensor_encoding=TensorEncoding.Uint8
                )
            ],
            ContainerEncoding.Png: [
                ParameterRepresentation(
                    channel_modality=ChannelModality.Image,
                    channel_encoding=ChannelEncoding.Rgba,
                    sample_encoding=SampleEncoding.U8,
                    tensor_encoding=TensorEncoding.Uint8
                )
            ],
            ContainerEncoding.WebP: [
                ParameterRepresentation(
                    channel_modality=ChannelModality.Image,
                    channel_encoding=ChannelEncoding.Rgb,
                    sample_encoding=SampleEncoding.U8,
                    tensor_encoding=TensorEncoding.Uint8
                )
            ]
        },
        ContainerModality.Integer: {
            ContainerEncoding.Txt: [
                ParameterRepresentation(
                    channel_modality=ChannelModality.Integer,
                    channel_encoding=ChannelEncoding.Utf8,
                    sample_encoding=SampleEncoding.U8,
                    tensor_encoding=TensorEncoding.Int32
                )
            ]
        },
        ContainerModality.Text: {
            ContainerEncoding.DocX: [
                ParameterRepresentation(
                    channel_modality=ChannelModality.Text,
                    channel_encoding=ChannelEncoding.Utf8,
                    sample_encoding=SampleEncoding.U8,
                    tensor_encoding=TensorEncoding.Int64
                )
            ],
            ContainerEncoding.Pdf: [
                ParameterRepresentation(
                    channel_modality=ChannelModality.Text,
                    channel_encoding=ChannelEncoding.Utf8,
                    sample_encoding=SampleEncoding.U8,
                    tensor_encoding=TensorEncoding.Int64
                )
            ],
            ContainerEncoding.Txt: [
                ParameterRepresentation(
                    channel_modality=ChannelModality.Text,
                    channel_encoding=ChannelEncoding.Utf8,
                    sample_encoding=SampleEncoding.U8,
                    tensor_encoding=TensorEncoding.Int64
                )
            ]
        },
        ContainerModality.Video: {
            ContainerEncoding.Mkv: [
                ParameterRepresentation(
                    channel_modality=ChannelModality.Audio,
                    channel_encoding=ChannelEncoding.Opus,
                    sample_encoding=SampleEncoding.Flt,
                    tensor_encoding=TensorEncoding.Float32
                ),
                ParameterRepresentation(
                    channel_modality=ChannelModality.Text,
                    channel_encoding=ChannelEncoding.Srt,
                    sample_encoding=SampleEncoding.U8,
                    tensor_encoding=TensorEncoding.Int64
                ),
                ParameterRepresentation(
                    channel_modality=ChannelModality.Video,
                    channel_encoding=ChannelEncoding.H264,
                    sample_encoding=SampleEncoding.Yuv420P,
                    tensor_encoding=TensorEncoding.Float32
                )
            ],
            ContainerEncoding.Mov: [
                ParameterRepresentation(
                    channel_modality=ChannelModality.Audio,
                    channel_encoding=ChannelEncoding.Aac,
                    sample_encoding=SampleEncoding.FltP,
                    tensor_encoding=TensorEncoding.Float32
                ),
                ParameterRepresentation(
                    channel_modality=ChannelModality.Text,
                    channel_encoding=ChannelEncoding.MovText,
                    sample_encoding=SampleEncoding.U8,
                    tensor_encoding=TensorEncoding.Int64
                ),
                ParameterRepresentation(
                    channel_modality=ChannelModality.Video,
                    channel_encoding=ChannelEncoding.H264,
                    sample_encoding=SampleEncoding.Yuv420P,
                    tensor_encoding=TensorEncoding.Float32
                )
            ],
            ContainerEncoding.Mp4: [
                ParameterRepresentation(
                    channel_modality=ChannelModality.Audio,
                    channel_encoding=ChannelEncoding.Aac,
                    sample_encoding=SampleEncoding.FltP,
                    tensor_encoding=TensorEncoding.Float32
                ),
                ParameterRepresentation(
                    channel_modality=ChannelModality.Text,
                    channel_encoding=ChannelEncoding.MovText,
                    sample_encoding=SampleEncoding.U8,
                    tensor_encoding=TensorEncoding.Int64
                ),
                ParameterRepresentation(
                    channel_modality=ChannelModality.Video,
                    channel_encoding=ChannelEncoding.H264,
                    sample_encoding=SampleEncoding.Yuv420P,
                    tensor_encoding=TensorEncoding.Float32
                )
            ],
            ContainerEncoding.WebM: [
                ParameterRepresentation(
                    channel_modality=ChannelModality.Audio,
                    channel_encoding=ChannelEncoding.Opus,
                    sample_encoding=SampleEncoding.Flt,
                    tensor_encoding=TensorEncoding.Float32
                ),
                ParameterRepresentation(
                    channel_modality=ChannelModality.Text,
                    channel_encoding=ChannelEncoding.Vtt,
                    sample_encoding=SampleEncoding.U8,
                    tensor_encoding=TensorEncoding.Int64
                ),
                ParameterRepresentation(
                    channel_modality=ChannelModality.Video,
                    channel_encoding=ChannelEncoding.Vp9,
                    sample_encoding=SampleEncoding.Yuv420P,
                    tensor_encoding=TensorEncoding.Float32
                )
            ]
        }
    }