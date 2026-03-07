class EncodingArguments:
    Arguments_Map = {
        "Audio": {
            "aac": {
                "Audio": {
                    "aac": {
                        "bit_depth": 32,
                        "bit_rate": 128000,
                        "channels": 2,
                        "frame_layout": "stereo",
                        "frame_size": 1024,
                        "sample_rate": 48000
                    }
                }
            },
            "flac": {
                "Audio": {
                    "flac": {
                        "bit_depth": 16,
                        "channels": 2,
                        "compression_level": 5,
                        "frame_layout": "stereo",
                        "frame_size": 4096,
                        "sample_rate": 48000
                    }
                }
            },
            "mp3": {
                "Audio": {
                    "mp3": {
                        "bit_depth": 32,
                        "bit_rate": 192000,
                        "channels": 2,
                        "frame_layout": "stereo",
                        "frame_size": 1152,
                        "sample_rate": 44100
                    },
                    "mp3_vbr": {
                        "bit_depth": 32,
                        "bit_rate": 192000,
                        "channels": 2,
                        "frame_layout": "stereo",
                        "frame_size": 1152,
                        "sample_rate": 44100
                    }
                }
            },
            "ogg": {
                "Audio": {
                    "flac": {
                        "bit_depth": 16,
                        "channels": 2,
                        "compression_level": 5,
                        "frame_layout": "stereo",
                        "frame_size": 4096,
                        "sample_rate": 48000
                    },
                    "opus": {
                        "bit_depth": 32,
                        "bit_rate": 96000,
                        "channels": 2,
                        "frame_layout": "stereo",
                        "frame_size": 960,
                        "sample_rate": 48000
                    },
                    "vorbis": {
                        "bit_depth": 32,
                        "bit_rate": 112000,
                        "channels": 2,
                        "frame_layout": "stereo",
                        "frame_size": 4096,
                        "sample_rate": 44100
                    },
                }
            },
            "wav": {
                "Audio": {
                    "pcm_f32le": {
                        "bit_depth": 32,
                        "channels": 2,
                        "frame_layout": "stereo",
                        "frame_size": 1024,
                        "sample_rate": 48000
                    },
                    "pcm_s16le": {
                        "bit_depth": 16,
                        "channels": 2,
                        "frame_layout": "stereo",
                        "frame_size": 1024,
                        "sample_rate": 48000
                    },
                    "pcm_s24le": {
                        "bit_depth": 24, # FFmpeg uses 32-bit samples (4 bytes) to represent 24-bit PCM, due to integer representation constraints in memory, but writes 24 bits (3 bytes) to disk per sample
                        "channels": 2,
                        "frame_layout": "stereo",
                        "frame_size": 1024,
                        "sample_rate": 48000
                    },
                    "pcm_s32le": {
                        "bit_depth": 32,
                        "channels": 2,
                        "frame_layout": "stereo",
                        "frame_size": 1024,
                        "sample_rate": 48000
                    }
                }
            }
        },
        "Float": {
            "txt": {
                "Float": {
                    "utf8": {
                        "bit_depth": 8,
                        "channels": 1
                    }
                }
            }
        },
        "Image": {
            "jpg": {
                "Image": {
                    "cmyk": {
                        "bit_depth": 8,
                        "channels": 4,
                        "quality": 75
                    },
                    "l": {
                        "bit_depth": 8,
                        "channels": 1,
                        "quality": 75
                    },
                    "rgb": {
                        "bit_depth": 8,
                        "channels": 3,
                        "quality": 75
                    },
                    "ycbcr": {
                        "bit_depth": 8,
                        "channels": 3,
                        "quality": 75
                    }
                }
            },
            "png": {
                "Image": {
                    "1": {
                        "bit_depth": 1,
                        "channels": 1,
                        "compression_level": 6
                    },
                    "l": {
                        "bit_depth": 8,
                        "channels": 1,
                        "compression_level": 6
                    },
                    "p": {
                        "bit_depth": 8,
                        "channels": 1,
                        "compression_level": 6
                    },
                    "rgb": {
                        "bit_depth": 8,
                        "channels": 3,
                        "compression_level": 6
                    },
                    "rgba": {
                        "bit_depth": 8,
                        "channels": 4,
                        "compression_level": 6
                    }
                }
            },
            "webp": {
                "Image": {
                    "rgb": {
                        "bit_depth": 8,
                        "channels": 3,
                        "quality": 80
                    },
                    "rgba": {
                        "bit_depth": 8,
                        "channels": 4,
                        "quality": 80
                    }
                }
            }
        },
        "Integer": {
            "txt": {
                "Integer": {
                    "utf8": {
                        "bit_depth": 8,
                        "channels": 1
                    }
                }
            }
        },
        "Text": {
            "docx": {
                "Text": {
                    "utf8": {
                        "bit_depth": 8,
                        "channels": 1
                    },
                    "utf16": {
                        "bit_depth": 16,
                        "channels": 1
                    }
                }
            },
            "pdf": {
                "Text": {
                    "utf8": {
                        "bit_depth": 8,
                        "channels": 1
                    },
                    "utf16": {
                        "bit_depth": 16,
                        "channels": 1
                    }
                }
            },
            "txt": {
                "Text": {
                    "utf8": {
                        "bit_depth": 8,
                        "channels": 1
                    },
                    "utf16": {
                        "bit_depth": 16,
                        "channels": 1
                    }
                }
            }
        },
        "Video": {
            "mkv": {
                "Audio": {
                    "aac": {
                        "bit_depth": 32,
                        "bit_rate": 128000,
                        "channels": 2,
                        "frame_layout": "stereo",
                        "frame_size": 1024,
                        "sample_rate": 48000
                    },
                    "flac": {
                        "bit_depth": 16,
                        "channels": 2,
                        "compression_level": 5,
                        "frame_layout": "stereo",
                        "frame_size": 4096,
                        "sample_rate": 48000
                    },
                    "mp3": {
                        "bit_depth": 32,
                        "bit_rate": 192000,
                        "channels": 2,
                        "frame_layout": "stereo",
                        "frame_size": 1152,
                        "sample_rate": 48000 # standalone audio uses 44100 (CD origin), but video containers standardise on 48kHz to avoid resampling against the video timeline
                    },
                    "opus": {
                        "bit_depth": 32,
                        "bit_rate": 96000,
                        "channels": 2,
                        "frame_layout": "stereo",
                        "frame_size": 960,
                        "sample_rate": 48000
                    },
                    "pcm_f32le": {
                        "bit_depth": 32,
                        "channels": 2,
                        "frame_layout": "stereo",
                        "frame_size": 1024,
                        "sample_rate": 48000
                    },
                    "pcm_s16le": {
                        "bit_depth": 16,
                        "channels": 2,
                        "frame_layout": "stereo",
                        "frame_size": 1024,
                        "sample_rate": 48000
                    },
                    "pcm_s24le": {
                        "bit_depth": 24,
                        "channels": 2,
                        "frame_layout": "stereo",
                        "frame_size": 1024,
                        "sample_rate": 48000
                    },
                    "pcm_s32le": {
                        "bit_depth": 32,
                        "channels": 2,
                        "frame_layout": "stereo",
                        "frame_size": 1024,
                        "sample_rate": 48000
                    },
                    "vorbis": {
                        "bit_depth": 32,
                        "bit_rate": 112000,
                        "channels": 2,
                        "frame_layout": "stereo",
                        "frame_size": 4096,
                        "sample_rate": 48000 # standalone audio uses 44100 (CD origin), but video containers standardise on 48kHz to avoid resampling against the video timeline
                    }
                },
                "Text": {
                    "ass": {
                        "bit_depth": 8,
                        "channels": 1
                    },
                    "srt": {
                        "bit_depth": 8,
                        "channels": 1
                    },
                    "vtt": {
                        "bit_depth": 8,
                        "channels": 1
                    }
                },
                "Video": {
                    "av1": {
                        "bit_depth": 8,
                        "bit_rate": 1000000,
                        "channels": 3,
                        "crf": 30,
                        "frame_rate": 30,
                        "gop_size": 12
                    },
                    "ffv1": {
                        "bit_depth": 8,
                        "channels": 3,
                        "frame_rate": 30,
                        "gop_size": 1
                    },
                    "h264": {
                        "bit_depth": 8,
                        "bit_rate": 2000000,
                        "channels": 3,
                        "crf": 23,
                        "frame_rate": 30,
                        "gop_size": 12,
                        "preset": "medium"
                    },
                    "h265": {
                        "bit_depth": 8,
                        "bit_rate": 1500000,
                        "channels": 3,
                        "crf": 28,
                        "frame_rate": 30,
                        "gop_size": 12,
                        "preset": "medium"
                    },
                    "vp8": {
                        "bit_depth": 8,
                        "bit_rate": 2000000,
                        "channels": 3,
                        "frame_rate": 30,
                        "gop_size": 12
                    },
                    "vp9": {
                        "bit_depth": 8,
                        "bit_rate": 1500000,
                        "channels": 3,
                        "crf": 31,
                        "frame_rate": 30,
                        "gop_size": 12
                    }
                }
            },
            "mov": {
                "Audio": {
                    "aac": {
                        "bit_depth": 32,
                        "bit_rate": 128000,
                        "channels": 2,
                        "frame_layout": "stereo",
                        "frame_size": 1024,
                        "sample_rate": 48000
                    },
                    "alac": {
                        "bit_depth": 16,
                        "channels": 2,
                        "frame_layout": "stereo",
                        "frame_size": 4096,
                        "sample_rate": 48000
                    },
                    "mp3": {
                        "bit_depth": 32,
                        "bit_rate": 192000,
                        "channels": 2,
                        "frame_layout": "stereo",
                        "frame_size": 1152,
                        "sample_rate": 48000 # standalone audio uses 44100 (CD origin), but video containers standardise on 48kHz to avoid resampling against the video timeline
                    },
                    "pcm_f32le": {
                        "bit_depth": 32,
                        "channels": 2,
                        "frame_layout": "stereo",
                        "frame_size": 1024,
                        "sample_rate": 48000
                    },
                    "pcm_s16le": {
                        "bit_depth": 16,
                        "channels": 2,
                        "frame_layout": "stereo",
                        "frame_size": 1024,
                        "sample_rate": 48000
                    },
                    "pcm_s24le": {
                        "bit_depth": 24,
                        "channels": 2,
                        "frame_layout": "stereo",
                        "frame_size": 1024,
                        "sample_rate": 48000
                    },
                    "pcm_s32le": {
                        "bit_depth": 32,
                        "channels": 2,
                        "frame_layout": "stereo",
                        "frame_size": 1024,
                        "sample_rate": 48000
                    }
                },
                "Text": {
                    "mov_text": {
                        "bit_depth": 8,
                        "channels": 1
                    }
                },
                "Video": {
                    "h264": {
                        "bit_depth": 8,
                        "bit_rate": 2000000,
                        "channels": 3,
                        "crf": 23,
                        "frame_rate": 30,
                        "gop_size": 12,
                        "preset": "medium"
                    },
                    "h265": {
                        "bit_depth": 8,
                        "bit_rate": 1500000,
                        "channels": 3,
                        "crf": 28,
                        "frame_rate": 30,
                        "gop_size": 12,
                        "preset": "medium"
                    },
                    "mjpeg": {
                        "bit_depth": 8,
                        "bit_rate": 10000000,
                        "channels": 3,
                        "frame_rate": 30,
                        "gop_size": 1
                    },
                    "prores_ks": {
                        "bit_depth": 10,
                        "channels": 3,
                        "frame_rate": 30,
                        "gop_size": 1
                    }
                }
            },
            "mp4": {
                "Audio": {
                    "aac": {
                        "bit_depth": 32,
                        "bit_rate": 128000,
                        "channels": 2,
                        "frame_layout": "stereo",
                        "frame_size": 1024,
                        "sample_rate": 48000
                    },
                    "alac": {
                        "bit_depth": 16,
                        "channels": 2,
                        "frame_layout": "stereo",
                        "frame_size": 4096,
                        "sample_rate": 48000
                    },
                    "mp3": {
                        "bit_depth": 32,
                        "bit_rate": 192000,
                        "channels": 2,
                        "frame_layout": "stereo",
                        "frame_size": 1152,
                        "sample_rate": 48000 # standalone audio uses 44100 (CD origin), but video containers standardise on 48kHz to avoid resampling against the video timeline
                    }
                },
                "Text": {
                    "mov_text": {
                        "bit_depth": 8,
                        "channels": 1
                    }
                },
                "Video": {
                    "av1": {
                        "bit_depth": 8,
                        "bit_rate": 1000000,
                        "channels": 3,
                        "crf": 30,
                        "frame_rate": 30,
                        "gop_size": 12
                    },
                    "h264": {
                        "bit_depth": 8,
                        "bit_rate": 2000000,
                        "channels": 3,
                        "crf": 23,
                        "frame_rate": 30,
                        "gop_size": 12,
                        "preset": "medium"
                    },
                    "h265": {
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
            "webm": {
                "Audio": {
                    "opus": {
                        "bit_depth": 32,
                        "bit_rate": 96000,
                        "channels": 2,
                        "frame_layout": "stereo",
                        "frame_size": 960,
                        "sample_rate": 48000
                    },
                    "vorbis": {
                        "bit_depth": 32,
                        "bit_rate": 112000,
                        "channels": 2,
                        "frame_layout": "stereo",
                        "frame_size": 4096,
                        "sample_rate": 48000 # standalone audio uses 44100 (CD origin), but video containers standardise on 48kHz to avoid resampling against the video timeline
                    }
                },
                "Text": {
                    "vtt": {
                        "bit_depth": 8,
                        "channels": 1
                    }
                },
                "Video": {
                    "av1": {
                        "bit_depth": 8,
                        "bit_rate": 1000000,
                        "channels": 3,
                        "crf": 30,
                        "frame_rate": 30,
                        "gop_size": 12
                    },
                    "vp8": {
                        "bit_depth": 8,
                        "bit_rate": 2000000,
                        "channels": 3,
                        "frame_rate": 30,
                        "gop_size": 12
                    },
                    "vp9": {
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