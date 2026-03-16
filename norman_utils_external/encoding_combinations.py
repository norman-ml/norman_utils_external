from norman_objects.shared.encoding.channel_encoding import ChannelEncoding
from norman_objects.shared.encoding.container_encoding import ContainerEncoding
from norman_objects.shared.encoding.sample_encoding import SampleEncoding
from norman_objects.shared.modality.channel_modality import ChannelModality
from norman_objects.shared.modality.container_modality import ContainerModality


class EncodingCombinations:
    Combinations_Map = {
        ContainerModality.Audio: {
            ContainerEncoding.Aac: {
                ChannelModality.Audio: {
                    ChannelEncoding.Aac: {
                        SampleEncoding.FltP
                    }
                }
            },
            ContainerEncoding.Flac: {
                ChannelModality.Audio: {
                    ChannelEncoding.Flac: {
                        SampleEncoding.S16,
                        SampleEncoding.S32
                    }
                }
            },
            ContainerEncoding.Mp3: {
                ChannelModality.Audio: {
                    ChannelEncoding.Mp3: {
                        SampleEncoding.FltP,
                        SampleEncoding.S16P,
                        SampleEncoding.S32P
                    },
                    ChannelEncoding.Mp3Vbr: {
                        SampleEncoding.FltP,
                        SampleEncoding.S16P,
                        SampleEncoding.S32P
                    }
                }
            },
            ContainerEncoding.Ogg: {
                ChannelModality.Audio: {
                    ChannelEncoding.Flac: {
                        SampleEncoding.S16,
                        SampleEncoding.S32
                    },
                    ChannelEncoding.Opus: {
                        SampleEncoding.Flt,
                        SampleEncoding.S16
                    },
                    ChannelEncoding.Vorbis: {
                        SampleEncoding.FltP
                    },
                }
            },
            ContainerEncoding.Wav: {
                ChannelModality.Audio: {
                    ChannelEncoding.PcmF32Le: {
                        SampleEncoding.Flt
                    },
                    ChannelEncoding.PcmS16Le: {
                        SampleEncoding.S16
                    },
                    ChannelEncoding.PcmS24Le: {
                        SampleEncoding.S32  # FFmpeg uses 32-bit samples (4 bytes) to represent 24-bit PCM
                    },
                    ChannelEncoding.PcmS32Le: {
                        SampleEncoding.S32
                    }
                }
            }
        },
        ContainerModality.File: {
            ContainerEncoding.Bin: {
                ChannelModality.Text: {
                    ChannelEncoding.Utf8: {
                        SampleEncoding.U8
                    }
                }
            },
            ContainerEncoding.Pt: {
                ChannelModality.Text: {
                    ChannelEncoding.Utf8: {
                        SampleEncoding.U8
                    }
                }
            },
            ContainerEncoding.Zip: {
                ChannelModality.Text: {
                    ChannelEncoding.Utf8: {
                        SampleEncoding.U8
                    }
                }
            }
        },
        ContainerModality.Float: {
            ContainerEncoding.Txt: {
                ChannelModality.Float: {
                    ChannelEncoding.Utf8: {
                        SampleEncoding.U8
                    }
                }
            }
        },
        ContainerModality.Image: {
            ContainerEncoding.Jpg: {
                ChannelModality.Image: {
                    ChannelEncoding.Cmyk: {
                        SampleEncoding.U8
                    },
                    ChannelEncoding.L: {
                        SampleEncoding.U8
                    },
                    ChannelEncoding.Rgb: {
                        SampleEncoding.U8
                    },
                    ChannelEncoding.YCbCr: {
                        SampleEncoding.U8
                    }
                }
            },
            ContainerEncoding.Png: {
                ChannelModality.Image: {
                    ChannelEncoding.One: {
                        SampleEncoding.U8
                    },
                    ChannelEncoding.L: {
                        SampleEncoding.U8
                    },
                    ChannelEncoding.P: {
                        SampleEncoding.U8
                    },
                    ChannelEncoding.Rgb: {
                        SampleEncoding.U8
                    },
                    ChannelEncoding.Rgba: {
                        SampleEncoding.U8
                    }
                }
            },
            ContainerEncoding.WebP: {
                ChannelModality.Image: {
                    ChannelEncoding.Rgb: {
                        SampleEncoding.U8
                    },
                    ChannelEncoding.Rgba: {
                        SampleEncoding.U8
                    }
                }
            }
        },
        ContainerModality.Integer: {
            ContainerEncoding.Txt: {
                ChannelModality.Integer: {
                    ChannelEncoding.Utf8: {
                        SampleEncoding.U8
                    }
                }
            }
        },
        ContainerModality.Text: {
            ContainerEncoding.DocX: {
                ChannelModality.Text: {
                    ChannelEncoding.Utf8: {
                        SampleEncoding.U8
                    },
                    ChannelEncoding.Utf16: {
                        SampleEncoding.U16Be,
                        SampleEncoding.U16Le
                    }
                }
            },
            ContainerEncoding.Pdf: {
                ChannelModality.Text: {
                    ChannelEncoding.Utf8: {
                        SampleEncoding.U8
                    },
                    ChannelEncoding.Utf16: {
                        SampleEncoding.U16Be,
                        SampleEncoding.U16Le
                    }
                }
            },
            ContainerEncoding.Txt: {
                ChannelModality.Text: {
                    ChannelEncoding.Utf8: {
                        SampleEncoding.U8
                    },
                    ChannelEncoding.Utf16: {
                        SampleEncoding.U16Be,
                        SampleEncoding.U16Le
                    }
                }
            }
        },
        ContainerModality.Video: {
            ContainerEncoding.Mkv: {
                ChannelModality.Audio: {
                    ChannelEncoding.Aac: {
                        SampleEncoding.FltP
                    },
                    ChannelEncoding.Flac: {
                        SampleEncoding.S16,
                        SampleEncoding.S32
                    },
                    ChannelEncoding.Mp3: {
                        SampleEncoding.FltP,
                        SampleEncoding.S16P,
                        SampleEncoding.S32P
                    },
                    ChannelEncoding.Opus: {
                        SampleEncoding.Flt,
                        SampleEncoding.S16
                    },
                    ChannelEncoding.PcmF32Le: {
                        SampleEncoding.Flt
                    },
                    ChannelEncoding.PcmS16Le: {
                        SampleEncoding.S16
                    },
                    ChannelEncoding.PcmS24Le: {
                        SampleEncoding.S32  # FFmpeg uses 32-bit samples (4 bytes) to represent 24-bit PCM
                    },
                    ChannelEncoding.PcmS32Le: {
                        SampleEncoding.S32
                    },
                    ChannelEncoding.Vorbis: {
                        SampleEncoding.FltP
                    }
                },
                ChannelModality.Text: {
                    ChannelEncoding.Ass: {
                        SampleEncoding.U8
                    },
                    ChannelEncoding.Srt: {
                        SampleEncoding.U8
                    },
                    ChannelEncoding.Vtt: {
                        SampleEncoding.U8
                    }
                },
                ChannelModality.Video: {
                    ChannelEncoding.Av1: {
                        SampleEncoding.Yuv420P,
                        SampleEncoding.Yuv444P
                    },
                    ChannelEncoding.Ffv1: {
                        SampleEncoding.GbrP,
                        SampleEncoding.Yuv420P,
                        SampleEncoding.Yuv422P,
                        SampleEncoding.Yuv444P
                    },
                    ChannelEncoding.H264: {
                        SampleEncoding.Yuv420P,
                        SampleEncoding.Yuv444P
                    },
                    ChannelEncoding.H265: {
                        SampleEncoding.GbrP,
                        SampleEncoding.Yuv420P,
                        SampleEncoding.Yuv444P
                    },
                    ChannelEncoding.Vp8: {
                        SampleEncoding.Yuv420P
                    },
                    ChannelEncoding.Vp9: {
                        SampleEncoding.Yuv420P
                    }
                }
            },
            ContainerEncoding.Mov: {
                ChannelModality.Audio: {
                    ChannelEncoding.Aac: {
                        SampleEncoding.FltP
                    },
                    ChannelEncoding.Alac: {
                        SampleEncoding.S16,
                        SampleEncoding.S32
                    },
                    ChannelEncoding.Mp3: {
                        SampleEncoding.FltP,
                        SampleEncoding.S16P,
                        SampleEncoding.S32P
                    },
                    ChannelEncoding.PcmF32Le: {
                        SampleEncoding.Flt
                    },
                    ChannelEncoding.PcmS16Le: {
                        SampleEncoding.S16
                    },
                    ChannelEncoding.PcmS24Le: {
                        SampleEncoding.S32  # FFmpeg uses 32-bit samples (4 bytes) to represent 24-bit PCM
                    },
                    ChannelEncoding.PcmS32Le: {
                        SampleEncoding.S32
                    },
                },
                ChannelModality.Text: {
                    ChannelEncoding.MovText: {
                        SampleEncoding.U8
                    }
                },
                ChannelModality.Video: {
                    ChannelEncoding.H264: {
                        SampleEncoding.Nv12,
                        SampleEncoding.Nv16,
                        SampleEncoding.Nv21,
                        SampleEncoding.Yuv420P,
                        SampleEncoding.Yuv422P,
                        SampleEncoding.Yuv444P,
                        SampleEncoding.YuvJ420P,
                        SampleEncoding.YuvJ422P,
                        SampleEncoding.YuvJ444P
                    },
                    ChannelEncoding.H265: {
                        SampleEncoding.GbrP,
                        SampleEncoding.GbrP10Le,
                        SampleEncoding.Gray,
                        SampleEncoding.Gray10Le,
                        SampleEncoding.Yuv420P,
                        SampleEncoding.Yuv420P10Le,
                        SampleEncoding.Yuv422P,
                        SampleEncoding.Yuv422P10Le,
                        SampleEncoding.Yuv444P,
                        SampleEncoding.Yuv444P10Le
                    },
                    ChannelEncoding.Mjpeg: {
                        SampleEncoding.Yuv420P,
                        SampleEncoding.Yuv422P,
                        SampleEncoding.Yuv444P,
                        SampleEncoding.YuvJ420P,
                        SampleEncoding.YuvJ422P,
                        SampleEncoding.YuvJ444P
                    },
                    ChannelEncoding.ProresKs: {
                        SampleEncoding.Yuv422P10Le,
                        SampleEncoding.Yuv444P10Le,
                        SampleEncoding.YuvA444P10Le
                    }
                }
            },
            ContainerEncoding.Mp4: {
                ChannelModality.Audio: {
                    ChannelEncoding.Aac: {
                        SampleEncoding.FltP
                    },
                    ChannelEncoding.Alac: {
                        SampleEncoding.S16P,
                        SampleEncoding.S32P
                    },
                    ChannelEncoding.Mp3: {
                        SampleEncoding.FltP,
                        SampleEncoding.S16P,
                        SampleEncoding.S32P
                    }
                },
                ChannelModality.Text: {
                    ChannelEncoding.MovText: {
                        SampleEncoding.U8
                    }
                },
                ChannelModality.Video: {
                    ChannelEncoding.Av1: {
                        SampleEncoding.GbrP,
                        SampleEncoding.Yuv420P,
                        SampleEncoding.Yuv444P
                    },
                    ChannelEncoding.H264: {
                        SampleEncoding.Yuv420P
                    },
                    ChannelEncoding.H265: {
                        SampleEncoding.GbrP,
                        SampleEncoding.Yuv420P,
                        SampleEncoding.Yuv444P
                    }
                }
            },
            ContainerEncoding.WebM: {
                ChannelModality.Audio: {
                    ChannelEncoding.Opus: {
                        SampleEncoding.Flt,
                        SampleEncoding.S16
                    },
                    ChannelEncoding.Vorbis: {
                        SampleEncoding.FltP
                    }
                },
                ChannelModality.Text: {
                    ChannelEncoding.Vtt: {
                        SampleEncoding.U8
                    }
                },
                ChannelModality.Video: {
                    ChannelEncoding.Av1: {
                        SampleEncoding.Yuv420P
                    },
                    ChannelEncoding.Vp8: {
                        SampleEncoding.Yuv420P,
                        SampleEncoding.YuvA420P
                    },
                    ChannelEncoding.Vp9: {
                        SampleEncoding.Yuv420P,
                        SampleEncoding.YuvA420P
                    }
                }
            }
        }
    }