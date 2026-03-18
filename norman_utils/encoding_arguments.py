from norman_objects.shared.encoding.channel_encoding import ChannelEncoding
from norman_objects.shared.encoding.container_encoding import ContainerEncoding
from norman_objects.shared.modality.channel_modality import ChannelModality
from norman_objects.shared.modality.container_modality import ContainerModality


class EncodingArguments:
    Arguments_Map = {
        ContainerModality.Audio: {
            ContainerEncoding.Aac: {
                ChannelModality.Audio: {
                    ChannelEncoding.Aac: {
                        "bit_depth": 32,
                        "bit_rate": 128000,
                        "channels": 2,
                        "frame_layout": "stereo",
                        "frame_size": 1024,
                        "sample_rate": 48000
                    }
                }
            },
            ContainerEncoding.Flac: {
                ChannelModality.Audio: {
                    ChannelEncoding.Flac: {
                        "bit_depth": 16,
                        "channels": 2,
                        "compression_level": 5,
                        "frame_layout": "stereo",
                        "frame_size": 4096,
                        "sample_rate": 48000
                    }
                }
            },
            ContainerEncoding.Mp3: {
                ChannelModality.Audio: {
                    ChannelEncoding.Mp3: {
                        "bit_depth": 32,
                        "bit_rate": 192000,
                        "channels": 2,
                        "frame_layout": "stereo",
                        "frame_size": 1152,
                        "sample_rate": 44100
                    },
                    ChannelEncoding.Mp3Vbr: {
                        "bit_depth": 32,
                        "bit_rate": 192000,
                        "channels": 2,
                        "frame_layout": "stereo",
                        "frame_size": 1152,
                        "sample_rate": 44100
                    }
                }
            },
            ContainerEncoding.Ogg: {
                ChannelModality.Audio: {
                    ChannelEncoding.Flac: {
                        "bit_depth": 16,
                        "channels": 2,
                        "compression_level": 5,
                        "frame_layout": "stereo",
                        "frame_size": 4096,
                        "sample_rate": 48000
                    },
                    ChannelEncoding.Opus: {
                        "bit_depth": 32,
                        "bit_rate": 96000,
                        "channels": 2,
                        "frame_layout": "stereo",
                        "frame_size": 960,
                        "sample_rate": 48000
                    },
                    ChannelEncoding.Vorbis: {
                        "bit_depth": 32,
                        "bit_rate": 112000,
                        "channels": 2,
                        "frame_layout": "stereo",
                        "frame_size": 4096,
                        "sample_rate": 44100
                    },
                }
            },
            ContainerEncoding.Wav: {
                ChannelModality.Audio: {
                    ChannelEncoding.PcmF32Le: {
                        "bit_depth": 32,
                        "channels": 2,
                        "frame_layout": "stereo",
                        "frame_size": 1024,
                        "sample_rate": 48000
                    },
                    ChannelEncoding.PcmS16Le: {
                        "bit_depth": 16,
                        "channels": 2,
                        "frame_layout": "stereo",
                        "frame_size": 1024,
                        "sample_rate": 48000
                    },
                    ChannelEncoding.PcmS24Le: {
                        "bit_depth": 24,  # FFmpeg uses 32-bit samples (4 bytes) to represent 24-bit PCM, due to integer representation constraints in memory, but writes 24 bits (3 bytes) to disk per sample
                        "channels": 2,
                        "frame_layout": "stereo",
                        "frame_size": 1024,
                        "sample_rate": 48000
                    },
                    ChannelEncoding.PcmS32Le: {
                        "bit_depth": 32,
                        "channels": 2,
                        "frame_layout": "stereo",
                        "frame_size": 1024,
                        "sample_rate": 48000
                    }
                }
            }
        },
        ContainerModality.Float: {
            ContainerEncoding.Txt: {
                ChannelModality.Float: {
                    ChannelEncoding.Utf8: {
                        "bit_depth": 8,
                        "channels": 1
                    }
                }
            }
        },
        ContainerModality.Image: {
            ContainerEncoding.Jpg: {
                ChannelModality.Image: {
                    ChannelEncoding.Cmyk: {
                        "bit_depth": 8,
                        "channels": 4,
                        "quality": 75
                    },
                    ChannelEncoding.L: {
                        "bit_depth": 8,
                        "channels": 1,
                        "quality": 75
                    },
                    ChannelEncoding.Rgb: {
                        "bit_depth": 8,
                        "channels": 3,
                        "quality": 75
                    },
                    ChannelEncoding.YCbCr: {
                        "bit_depth": 8,
                        "channels": 3,
                        "quality": 75
                    }
                }
            },
            ContainerEncoding.Png: {
                ChannelModality.Image: {
                    ChannelEncoding.One: {
                        "bit_depth": 1,
                        "channels": 1,
                        "compression_level": 6
                    },
                    ChannelEncoding.L: {
                        "bit_depth": 8,
                        "channels": 1,
                        "compression_level": 6
                    },
                    ChannelEncoding.P: {
                        "bit_depth": 8,
                        "channels": 1,
                        "compression_level": 6
                    },
                    ChannelEncoding.Rgb: {
                        "bit_depth": 8,
                        "channels": 3,
                        "compression_level": 6
                    },
                    ChannelEncoding.Rgba: {
                        "bit_depth": 8,
                        "channels": 4,
                        "compression_level": 6
                    }
                }
            },
            ContainerEncoding.WebP: {
                ChannelModality.Image: {
                    ChannelEncoding.Rgb: {
                        "bit_depth": 8,
                        "channels": 3,
                        "quality": 80
                    },
                    ChannelEncoding.Rgba: {
                        "bit_depth": 8,
                        "channels": 4,
                        "quality": 80
                    }
                }
            }
        },
        ContainerModality.Integer: {
            ContainerEncoding.Txt: {
                ChannelModality.Integer: {
                    ChannelEncoding.Utf8: {
                        "bit_depth": 8,
                        "channels": 1
                    }
                }
            }
        },
        ContainerModality.Text: {
            ContainerEncoding.DocX: {
                ChannelModality.Text: {
                    ChannelEncoding.Utf8: {
                        "bit_depth": 8,
                        "channels": 1
                    },
                    ChannelEncoding.Utf16: {
                        "bit_depth": 16,
                        "channels": 1
                    }
                }
            },
            ContainerEncoding.Pdf: {
                ChannelModality.Text: {
                    ChannelEncoding.Utf8: {
                        "bit_depth": 8,
                        "channels": 1
                    },
                    ChannelEncoding.Utf16: {
                        "bit_depth": 16,
                        "channels": 1
                    }
                }
            },
            ContainerEncoding.Txt: {
                ChannelModality.Text: {
                    ChannelEncoding.Utf8: {
                        "bit_depth": 8,
                        "channels": 1
                    },
                    ChannelEncoding.Utf16: {
                        "bit_depth": 16,
                        "channels": 1
                    }
                }
            }
        },
        ContainerModality.Video: {
            ContainerEncoding.Mkv: {
                ChannelModality.Audio: {
                    ChannelEncoding.Aac: {
                        "bit_depth": 32,
                        "bit_rate": 128000,
                        "channels": 2,
                        "frame_layout": "stereo",
                        "frame_size": 1024,
                        "sample_rate": 48000
                    },
                    ChannelEncoding.Flac: {
                        "bit_depth": 16,
                        "channels": 2,
                        "compression_level": 5,
                        "frame_layout": "stereo",
                        "frame_size": 4096,
                        "sample_rate": 48000
                    },
                    ChannelEncoding.Mp3: {
                        "bit_depth": 32,
                        "bit_rate": 192000,
                        "channels": 2,
                        "frame_layout": "stereo",
                        "frame_size": 1152,
                        "sample_rate": 48000  # standalone audio uses 44100 (CD origin), but video containers standardise on 48kHz to avoid resampling against the video timeline
                    },
                    ChannelEncoding.Opus: {
                        "bit_depth": 32,
                        "bit_rate": 96000,
                        "channels": 2,
                        "frame_layout": "stereo",
                        "frame_size": 960,
                        "sample_rate": 48000
                    },
                    ChannelEncoding.PcmF32Le: {
                        "bit_depth": 32,
                        "channels": 2,
                        "frame_layout": "stereo",
                        "frame_size": 1024,
                        "sample_rate": 48000
                    },
                    ChannelEncoding.PcmS16Le: {
                        "bit_depth": 16,
                        "channels": 2,
                        "frame_layout": "stereo",
                        "frame_size": 1024,
                        "sample_rate": 48000
                    },
                    ChannelEncoding.PcmS24Le: {
                        "bit_depth": 24,
                        "channels": 2,
                        "frame_layout": "stereo",
                        "frame_size": 1024,
                        "sample_rate": 48000
                    },
                    ChannelEncoding.PcmS32Le: {
                        "bit_depth": 32,
                        "channels": 2,
                        "frame_layout": "stereo",
                        "frame_size": 1024,
                        "sample_rate": 48000
                    },
                    ChannelEncoding.Vorbis: {
                        "bit_depth": 32,
                        "bit_rate": 112000,
                        "channels": 2,
                        "frame_layout": "stereo",
                        "frame_size": 4096,
                        "sample_rate": 48000  # standalone audio uses 44100 (CD origin), but video containers standardise on 48kHz to avoid resampling against the video timeline
                    }
                },
                ChannelModality.Text: {
                    ChannelEncoding.Ass: {
                        "bit_depth": 8,
                        "channels": 1
                    },
                    ChannelEncoding.Srt: {
                        "bit_depth": 8,
                        "channels": 1
                    },
                    ChannelEncoding.Vtt: {
                        "bit_depth": 8,
                        "channels": 1
                    }
                },
                ChannelModality.Video: {
                    ChannelEncoding.Av1: {
                        "bit_depth": 8,
                        "bit_rate": 1000000,
                        "channels": 3,
                        "crf": 30,
                        "frame_rate": 30,
                        "gop_size": 12
                    },
                    ChannelEncoding.Ffv1: {
                        "bit_depth": 8,
                        "channels": 3,
                        "frame_rate": 30,
                        "gop_size": 1
                    },
                    ChannelEncoding.H264: {
                        "bit_depth": 8,
                        "bit_rate": 2000000,
                        "channels": 3,
                        "crf": 23,
                        "frame_rate": 30,
                        "gop_size": 12,
                        "preset": "medium"
                    },
                    ChannelEncoding.H265: {
                        "bit_depth": 8,
                        "bit_rate": 1500000,
                        "channels": 3,
                        "crf": 28,
                        "frame_rate": 30,
                        "gop_size": 12,
                        "preset": "medium"
                    },
                    ChannelEncoding.Vp8: {
                        "bit_depth": 8,
                        "bit_rate": 2000000,
                        "channels": 3,
                        "frame_rate": 30,
                        "gop_size": 12
                    },
                    ChannelEncoding.Vp9: {
                        "bit_depth": 8,
                        "bit_rate": 1500000,
                        "channels": 3,
                        "crf": 31,
                        "frame_rate": 30,
                        "gop_size": 12
                    }
                }
            },
            ContainerEncoding.Mov: {
                ChannelModality.Audio: {
                    ChannelEncoding.Aac: {
                        "bit_depth": 32,
                        "bit_rate": 128000,
                        "channels": 2,
                        "frame_layout": "stereo",
                        "frame_size": 1024,
                        "sample_rate": 48000
                    },
                    ChannelEncoding.Alac: {
                        "bit_depth": 16,
                        "channels": 2,
                        "frame_layout": "stereo",
                        "frame_size": 4096,
                        "sample_rate": 48000
                    },
                    ChannelEncoding.Mp3: {
                        "bit_depth": 32,
                        "bit_rate": 192000,
                        "channels": 2,
                        "frame_layout": "stereo",
                        "frame_size": 1152,
                        "sample_rate": 48000  # standalone audio uses 44100 (CD origin), but video containers standardise on 48kHz to avoid resampling against the video timeline
                    },
                    ChannelEncoding.PcmF32Le: {
                        "bit_depth": 32,
                        "channels": 2,
                        "frame_layout": "stereo",
                        "frame_size": 1024,
                        "sample_rate": 48000
                    },
                    ChannelEncoding.PcmS16Le: {
                        "bit_depth": 16,
                        "channels": 2,
                        "frame_layout": "stereo",
                        "frame_size": 1024,
                        "sample_rate": 48000
                    },
                    ChannelEncoding.PcmS24Le: {
                        "bit_depth": 24,
                        "channels": 2,
                        "frame_layout": "stereo",
                        "frame_size": 1024,
                        "sample_rate": 48000
                    },
                    ChannelEncoding.PcmS32Le: {
                        "bit_depth": 32,
                        "channels": 2,
                        "frame_layout": "stereo",
                        "frame_size": 1024,
                        "sample_rate": 48000
                    }
                },
                ChannelModality.Text: {
                    ChannelEncoding.MovText: {
                        "bit_depth": 8,
                        "channels": 1
                    }
                },
                ChannelModality.Video: {
                    ChannelEncoding.H264: {
                        "bit_depth": 8,
                        "bit_rate": 2000000,
                        "channels": 3,
                        "crf": 23,
                        "frame_rate": 30,
                        "gop_size": 12,
                        "preset": "medium"
                    },
                    ChannelEncoding.H265: {
                        "bit_depth": 8,
                        "bit_rate": 1500000,
                        "channels": 3,
                        "crf": 28,
                        "frame_rate": 30,
                        "gop_size": 12,
                        "preset": "medium"
                    },
                    ChannelEncoding.Mjpeg: {
                        "bit_depth": 8,
                        "bit_rate": 10000000,
                        "channels": 3,
                        "frame_rate": 30,
                        "gop_size": 1
                    },
                    ChannelEncoding.ProresKs: {
                        "bit_depth": 10,
                        "channels": 3,
                        "frame_rate": 30,
                        "gop_size": 1
                    }
                }
            },
            ContainerEncoding.Mp4: {
                ChannelModality.Audio: {
                    ChannelEncoding.Aac: {
                        "bit_depth": 32,
                        "bit_rate": 128000,
                        "channels": 2,
                        "frame_layout": "stereo",
                        "frame_size": 1024,
                        "sample_rate": 48000
                    },
                    ChannelEncoding.Alac: {
                        "bit_depth": 16,
                        "channels": 2,
                        "frame_layout": "stereo",
                        "frame_size": 4096,
                        "sample_rate": 48000
                    },
                    ChannelEncoding.Mp3: {
                        "bit_depth": 32,
                        "bit_rate": 192000,
                        "channels": 2,
                        "frame_layout": "stereo",
                        "frame_size": 1152,
                        "sample_rate": 48000  # standalone audio uses 44100 (CD origin), but video containers standardise on 48kHz to avoid resampling against the video timeline
                    }
                },
                ChannelModality.Text: {
                    ChannelEncoding.MovText: {
                        "bit_depth": 8,
                        "channels": 1
                    }
                },
                ChannelModality.Video: {
                    ChannelEncoding.Av1: {
                        "bit_depth": 8,
                        "bit_rate": 1000000,
                        "channels": 3,
                        "crf": 30,
                        "frame_rate": 30,
                        "gop_size": 12
                    },
                    ChannelEncoding.H264: {
                        "bit_depth": 8,
                        "bit_rate": 2000000,
                        "channels": 3,
                        "crf": 23,
                        "frame_rate": 30,
                        "gop_size": 12,
                        "preset": "medium"
                    },
                    ChannelEncoding.H265: {
                        "bit_depth": 8,
                        "bit_rate": 1500000,
                        "channels": 3,
                        "crf": 28,
                        "frame_rate": 30,
                        "gop_size": 12,
                        "preset": "medium"
                    }
                }
            },
            ContainerEncoding.WebM: {
                ChannelModality.Audio: {
                    ChannelEncoding.Opus: {
                        "bit_depth": 32,
                        "bit_rate": 96000,
                        "channels": 2,
                        "frame_layout": "stereo",
                        "frame_size": 960,
                        "sample_rate": 48000
                    },
                    ChannelEncoding.Vorbis: {
                        "bit_depth": 32,
                        "bit_rate": 112000,
                        "channels": 2,
                        "frame_layout": "stereo",
                        "frame_size": 4096,
                        "sample_rate": 48000  # standalone audio uses 44100 (CD origin), but video containers standardise on 48kHz to avoid resampling against the video timeline
                    }
                },
                ChannelModality.Text: {
                    ChannelEncoding.Vtt: {
                        "bit_depth": 8,
                        "channels": 1
                    }
                },
                ChannelModality.Video: {
                    ChannelEncoding.Av1: {
                        "bit_depth": 8,
                        "bit_rate": 1000000,
                        "channels": 3,
                        "crf": 30,
                        "frame_rate": 30,
                        "gop_size": 12
                    },
                    ChannelEncoding.Vp8: {
                        "bit_depth": 8,
                        "bit_rate": 2000000,
                        "channels": 3,
                        "frame_rate": 30,
                        "gop_size": 12
                    },
                    ChannelEncoding.Vp9: {
                        "bit_depth": 8,
                        "bit_rate": 1500000,
                        "channels": 3,
                        "crf": 31,
                        "frame_rate": 30,
                        "gop_size": 12
                    }
                }
            }
        }
    }
