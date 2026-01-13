class EncodingCombinations:
    Encoding_Map = {
        "audio": {
            "aac": {
                "audio": {
                    "aac": {
                        "fltp"
                    }
                }
            },
            "flac": {
                "audio": {
                    "flac": {
                        "s16",
                        "s32"
                    }
                }
            },
            "mp3": {
                "audio": {
                    "mp3": {
                        "fltp",
                        "s16p",
                        "s32p"
                    },
                    "mp3_vbr": {
                        "fltp",
                        "s16p",
                        "s32p"
                    }
                }
            },
            "ogg": {
                "audio": {
                    "flac": {
                        "s16",
                        "s32"
                    },
                    "opus": {
                        "flt",
                        "s16"
                    },
                    "vorbis": {
                        "fltp"
                    },
                }
            },
            "wav": {
                "audio": {
                    "pcm_f32le": {
                        "flt"
                    },
                    "pcm_s16le": {
                        "s16"
                    },
                    "pcm_s24le": {
                        "s32" # FFmpeg uses 32-bit samples to represent 24-bit PCM
                    },
                    "pcm_s32le": {
                        "s32"
                    }
                }
            }
        },
        "image": {
            "jpg": {
                "image": {
                    "gray": {
                        "gray8"
                    },
                    "rgb": {
                        "rgb8"
                    },
                    "yuv420": {
                        "yuv420p"
                    },
                    "yuv444": {
                        "yuv444p"
                    }
                }
            },
            "png": {
                "image": {
                    "gray": {
                        "gray8",
                        "gray16"
                    },
                    "graya": {
                        "ya8",
                        "ya16"
                    },
                    "indexed": {
                        "palette8"
                    },
                    "rgb": {
                        "rgba8",
                        "rgb16"
                    },
                    "rgba": {
                        "rgba8",
                        "rgb16"
                    }
                }
            },
            "webp": {
                "image": {
                    "gray": {
                        "gray8"
                    },
                    # lossless
                    "rgb": {
                        "rgb8"
                    },
                    # lossless + alpha
                    "rgba": {
                        "rgba8"
                    },
                    # lossy
                    "yuv420": {
                        "yuv420p"
                    },
                    "yuva420": {
                        "yuva420p"
                    }
                }
            }
        },
        "text": {
            "docx": {
                "text": {
                    "utf8": {
                        "u8"
                    },
                    "utf16": {
                        "u16be",
                        "u16le"
                    }
                }
            },
            "pdf": {
                "text": {
                    "utf8": {
                        "u8"
                    },
                    "utf16": {
                        "u16be",
                        "u16le"
                    }
                }
            },
            "txt": {
                "text": {
                    "utf8": {
                        "u8"
                    },
                    "utf16": {
                        "u16be",
                        "u16le"
                    }
                }
            }
        },
        "video": {
            "mkv": {
                "audio": {
                    "aac": {
                         "fltp"
                    },
                    "flac": {
                        "s16",
                        "s32"
                    },
                    "mp3": {
                        "fltp",
                        "s16p",
                        "s32p"
                    },
                    "opus": {
                        "flt",
                        "s16"
                    },
                    "pcm_f32le": {
                        "flt"
                    },
                    "pcm_s16le": {
                        "s16"
                    },
                    "pcm_s24le": {
                        "s32"  # FFmpeg uses 32-bit samples to represent 24-bit PCM
                    },
                    "pcm_s32le": {
                        "s32"
                    },
                    "vorbis": {
                        "fltp"
                    }
                },
                "text": {
                    "ass": {
                        "utf8"
                    },
                    "srt": {
                        "utf8"
                    },
                    "vtt": {
                        "utf8"
                    }
                },
                "video": {
                    "av1": {
                        "yuv420p",
                        "yuv444p"
                    },
                    "ffv1": {
                        "gbrp",
                        "yuv420p",
                        "yuv422p",
                        "yuv444p"
                    },
                    "h264": {
                        "yuv420p",
                        "yuv444p"
                    },
                    "h265": {
                        "gbrp",
                        "yuv420p",
                        "yuv444p"
                    },
                    "vp8": {
                        "yuv420p"
                    },
                    "vp9": {
                        "yuv420p"
                    }
                }
            },
            "mov": {
                "audio": {
                    "aac": {
                        "fltp"
                    },
                    "alac": {
                        "s16",
                        "s32"
                    },
                    "mp3": {
                        "fltp",
                        "s16p",
                        "s32p"
                    },
                    "pcm_f32le": {
                        "flt"
                    },
                    "pcm_s16le": {
                        "s16"
                    },
                    "pcm_s24le": {
                        "s32"  # FFmpeg uses 32-bit samples to represent 24-bit PCM
                    },
                    "pcm_s32le": {
                        "s32"
                    },
                },
                "text": {
                     "mov_text": {
                        "utf8"
                    }
                },
                "video": {
                    "h264": {
                        "nv12",
                        "nv16",
                        "nv21",
                        "yuv420p",
                        "yuv422p",
                        "yuv444p",
                        "yuvj420p",
                        "yuvj422p",
                        "yuvj444p"
                    },
                    "h265": {
                        "gbrp",
                        "gbrp10le",
                        "gray",
                        "gray10le",
                        "yuv420p",
                        "yuv420p10le",
                        "yuv422p",
                        "yuv422p10le",
                        "yuv444p",
                        "yuv444p10le"
                    },
                    "motion-jpeg": {
                        "yuv420p",
                        "yuv422p",
                        "yuv444p",
                        "yuvj420p",
                        "yuvj422p",
                        "yuvj444p"
                    },
                    "prores": {
                        "yuv422p10le",
                        "yuv444p10le",
                        "yuva444p10le"
                    }
                }
            },
            "mp4": {
                "audio": {
                    "aac": {
                        "fltp"
                    },
                    "alac": {
                        "s16p",
                        "s32p"
                    },
                    "flac": {
                        "s16",
                        "s32"
                    },
                    "mp3": {
                        "fltp",
                        "s16p",
                        "s32p"
                    },
                    "opus": {
                        "flt",
                        "s16"
                    },
                    "vorbis": {
                        "fltp"
                    },
                },
                "text": {
                    "mov_text": {
                        "utf8"
                    }
                },
                "video": {
                    "av1": {
                        "gbrp",
                        "yuv420p",
                        "yuv444p"
                    },
                    "h264": {
                        "yuv420p"
                    },
                    "h265": {
                        "gbrp",
                        "yuv420p",
                        "yuv444p"
                    }
                }
            },
            "ogg": {
                "audio": {
                    "flac": {
                        "s16",
                        "s32"
                    },
                    "opus": {
                        "flt",
                        "s16"
                    },
                    "vorbis": {
                        "fltp"
                    }
                },
                "text": {
                    "kate": {
                        "utf8"
                    }
                },
                "video": {
                    "theora": {
                        "yuv420p",
                        "yuv422p",
                        "yuv444p"
                    }
                },
            },
            "webm": {
                "audio": {
                    "opus": {
                        "flt",
                        "s16"
                    },
                    "vorbis": {
                        "fltp"
                    }
                },
                "text": {
                    "vtt": {
                        "utf8"
                    }
                },
                "video": {
                    "av1": {
                        "yuv420p"
                    },
                    "vp8": {
                        "yuv420p",
                        "yuva420p"
                    },
                    "vp9": {
                        "yuv420p",
                        "yuva420p"
                    }
                }
            }
        }
    }