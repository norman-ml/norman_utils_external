from norman_objects.shared.encoding.channel_encoding import ChannelEncoding
from norman_objects.shared.encoding.container_encoding import ContainerEncoding
from norman_objects.shared.encoding.sample_encoding import SampleEncoding
from norman_objects.shared.encoding.tensor_encoding import TensorEncoding
from norman_objects.shared.modality.channel_modality import ChannelModality
from norman_objects.shared.modality.container_modality import ContainerModality


class EncodingDefaults:
    Container_Map = {
        ContainerModality.Audio: ContainerEncoding.Mp3,
        ContainerModality.Image: ContainerEncoding.Jpg,
        ContainerModality.Text: ContainerEncoding.Txt,
        ContainerModality.Video: ContainerEncoding.Mp4
    }

    Channel_Map = {
        ContainerModality.Audio: {
            ContainerEncoding.Aac: {
                ChannelModality.Audio: {
                    "channel": ChannelEncoding.Aac,
                    "sample": SampleEncoding.FltP,
                    "tensor": TensorEncoding.Float32
                }
            },
            ContainerEncoding.Flac: {
                ChannelModality.Audio: {
                    "channel": ChannelEncoding.Flac,
                    "sample": SampleEncoding.S16,
                    "tensor": TensorEncoding.Float32
                }
            },
            ContainerEncoding.Mp3: {
                ChannelModality.Audio: {
                    "channel": ChannelEncoding.Mp3,
                    "sample": SampleEncoding.FltP,
                    "tensor": TensorEncoding.Float32
                }
            },
            ContainerEncoding.Ogg: {
                ChannelModality.Audio: {
                    "channel": ChannelEncoding.Opus,
                    "sample": SampleEncoding.Flt,
                    "tensor": TensorEncoding.Float32
                }
            },
            ContainerEncoding.Wav: {
                ChannelModality.Audio: {
                    "channel": ChannelEncoding.PcmS16Le,
                    "sample": SampleEncoding.S16,
                    "tensor": TensorEncoding.Float32
                }
            }
        },
        ContainerModality.File: {
            ContainerEncoding.Bin: {
                ChannelModality.Text: {
                    "channel": ChannelEncoding.Utf8,
                    "sample": SampleEncoding.U8,
                    "tensor": TensorEncoding.Float32
                }
            },
            ContainerEncoding.Pt: {
                ChannelModality.Text: {
                    "channel": ChannelEncoding.Utf8,
                    "sample": SampleEncoding.U8,
                    "tensor": TensorEncoding.Float32
                }
            },
            ContainerEncoding.Zip: {
                ChannelModality.Text: {
                    "channel": ChannelEncoding.Utf8,
                    "sample": SampleEncoding.U8,
                    "tensor": TensorEncoding.Float32
                }
            }
        },
        ContainerModality.Float: {
            ContainerEncoding.Txt: {
                ChannelModality.Float: {
                    "channel": ChannelEncoding.Utf8,
                    "sample": SampleEncoding.U8,
                    "tensor": TensorEncoding.Float32
                }
            }
        },
        ContainerModality.Image: {
            ContainerEncoding.Jpg: {
                ChannelModality.Image: {
                    "channel": ChannelEncoding.Rgb,
                    "sample": SampleEncoding.U8,
                    "tensor": TensorEncoding.Uint8
                }
            },
            ContainerEncoding.Png: {
                ChannelModality.Image: {
                    "channel": ChannelEncoding.Rgba,
                    "sample": SampleEncoding.U8,
                    "tensor": TensorEncoding.Uint8
                }
            },
            ContainerEncoding.WebP: {
                ChannelModality.Image: {
                    "channel": ChannelEncoding.Rgb,
                    "sample": SampleEncoding.U8,
                    "tensor": TensorEncoding.Uint8
                }
            }
        },
        ContainerModality.Integer: {
            ContainerEncoding.Txt: {
                ChannelModality.Integer: {
                    "channel": ChannelEncoding.Utf8,
                    "sample": SampleEncoding.U8,
                    "tensor": TensorEncoding.Int32
                }
            }
        },
        ContainerModality.Text: {
            ContainerEncoding.DocX: {
                ChannelModality.Text: {
                    "channel": ChannelEncoding.Utf8,
                    "sample": SampleEncoding.U8,
                    "tensor": TensorEncoding.Int64
                }
            },
            ContainerEncoding.Pdf: {
                ChannelModality.Text: {
                    "channel": ChannelEncoding.Utf8,
                    "sample": SampleEncoding.U8,
                    "tensor": TensorEncoding.Int64
                }
            },
            ContainerEncoding.Txt: {
                ChannelModality.Text: {
                    "channel": ChannelEncoding.Utf8,
                    "sample": SampleEncoding.U8,
                    "tensor": TensorEncoding.Int64
                }
            }
        },
        ContainerModality.Video: {
            ContainerEncoding.Mkv: {
                ChannelModality.Audio: {
                    "channel": ChannelEncoding.Opus,
                    "sample": SampleEncoding.Flt,
                    "tensor": TensorEncoding.Float32
                },
                ChannelModality.Text: {
                    "channel": ChannelEncoding.Srt,
                    "sample": SampleEncoding.U8,
                    "tensor": TensorEncoding.Int64
                },
                ChannelModality.Video: {
                    "channel": ChannelEncoding.H264,
                    "sample": SampleEncoding.Yuv420P,
                    "tensor": TensorEncoding.Float32
                }
            },
            ContainerEncoding.Mov: {
                ChannelModality.Audio: {
                    "channel": ChannelEncoding.Aac,
                    "sample": SampleEncoding.FltP,
                    "tensor": TensorEncoding.Float32
                },
                ChannelModality.Text: {
                    "channel": ChannelEncoding.MovText,
                    "sample": SampleEncoding.U8,
                    "tensor": TensorEncoding.Int64
                },
                ChannelModality.Video: {
                    "channel": ChannelEncoding.H264,
                    "sample": SampleEncoding.Yuv420P,
                    "tensor": TensorEncoding.Float32
                }
            },
            ContainerEncoding.Mp4: {
                ChannelModality.Audio: {
                    "channel": ChannelEncoding.Aac,
                    "sample": SampleEncoding.FltP,
                    "tensor": TensorEncoding.Float32
                },
                ChannelModality.Text: {
                    "channel": ChannelEncoding.MovText,
                    "sample": SampleEncoding.U8,
                    "tensor": TensorEncoding.Int64
                },
                ChannelModality.Video: {
                    "channel": ChannelEncoding.H264,
                    "sample": SampleEncoding.Yuv420P,
                    "tensor": TensorEncoding.Float32
                }
            },
            ContainerEncoding.WebM: {
                ChannelModality.Audio: {
                    "channel": ChannelEncoding.Opus,
                    "sample": SampleEncoding.Flt,
                    "tensor": TensorEncoding.Float32
                },
                ChannelModality.Text: {
                    "channel": ChannelEncoding.Vtt,
                    "sample": SampleEncoding.U8,
                    "tensor": TensorEncoding.Int64
                },
                ChannelModality.Video: {
                    "channel": ChannelEncoding.Vp9,
                    "sample": SampleEncoding.Yuv420P,
                    "tensor": TensorEncoding.Float32
                }
            }
        }
    }