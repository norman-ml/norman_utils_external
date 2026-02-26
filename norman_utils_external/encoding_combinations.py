class EncodingCombinations:
    Combinations_Map = {
        "Audio": {
            "aac": {
                "Audio": {
                    "aac": {
                        "fltp"
                    }
                }
            },
            "flac": {
                "Audio": {
                    "flac": {
                        "s16",
                        "s32"
                    }
                }
            },
            "mp3": {
                "Audio": {
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
                "Audio": {
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
                "Audio": {
                    "pcm_f32le": {
                        "flt"
                    },
                    "pcm_s16le": {
                        "s16"
                    },
                    "pcm_s24le": {
                        "s32" # FFmpeg uses 32-bit samples (4 bytes) to represent 24-bit PCM, due to integer representation constraints in memory
                    },
                    "pcm_s32le": {
                        "s32"
                    }
                }
            }
        },
        "File": {
            "bin": {
                "File": {
                    "utf8": {
                        "u8"
                    }
                }
            },
            "pt": {
                "File": {
                    "utf8": {
                        "u8"
                    }
                }
            },
            "zip": {
                "File": {
                    "utf8": {
                        "u8"
                    }
                }
            }
        },
        "Float": {
            "txt": {
                "Float": {
                    "utf8": {
                        "u8"
                    }
                }
            }
        },
        "Image": {
            "jpg": {
                "Image": {
                    "cmyk": {
                        "u8"
                    },
                    "l": {
                        "u8"
                    },
                    "rgb": {
                        "u8"
                    },
                    "ycbcr": {
                        "u8"
                    }
                }
            },
            "png": {
                "Image": {
                    "1": {
                        "u8"
                    },
                    "l": {
                        "u8"
                    },
                    "p": {
                        "u8"
                    },
                    "rgb": {
                        "u8"
                    },
                    "rgba": {
                        "u8"
                    }
                }
            },
            "webp": {
                "Image": {
                    "rgb": {
                        "u8"
                    },
                    "rgba": {
                        "u8"
                    }
                }
            }
        },
        "Integer": {
            "txt": {
                "Integer": {
                    "utf8": {
                        "u8"
                    }
                }
            }
        },
        "Text": {
            "docx": {
                "Text": {
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
                "Text": {
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
                "Text": {
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
        "Video": {
            "mkv": {
                "Audio": {
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
                        "s32"  # FFmpeg uses 32-bit samples (4 bytes) to represent 24-bit PCM, due to integer representation constraints in memory
                    },
                    "pcm_s32le": {
                        "s32"
                    },
                    "vorbis": {
                        "fltp"
                    }
                },
                "Text": {
                    "ass": {
                        "u8"
                    },
                    "srt": {
                        "u8"
                    },
                    "vtt": {
                        "u8"
                    }
                },
                "Video": {
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
                "Audio": {
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
                        "s32"  # FFmpeg uses 32-bit samples (4 bytes) to represent 24-bit PCM, due to integer representation constraints in memory
                    },
                    "pcm_s32le": {
                        "s32"
                    },
                },
                "Text": {
                     "mov_text": {
                        "u8"
                    }
                },
                "Video": {
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
                    "mjpeg": {
                        "yuv420p",
                        "yuv422p",
                        "yuv444p",
                        "yuvj420p",
                        "yuvj422p",
                        "yuvj444p"
                    },
                    "prores_ks": {
                        "yuv422p10le",
                        "yuv444p10le",
                        "yuva444p10le"
                    }
                }
            },
            "mp4": {
                "Audio": {
                    "aac": {
                        "fltp"
                    },
                    "alac": {
                        "s16p",
                        "s32p"
                    },
                    "mp3": {
                        "fltp",
                        "s16p",
                        "s32p"
                    }
                },
                "Text": {
                    "mov_text": {
                        "u8"
                    }
                },
                "Video": {
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
            "webm": {
                "Audio": {
                    "opus": {
                        "flt",
                        "s16"
                    },
                    "vorbis": {
                        "fltp"
                    }
                },
                "Text": {
                    "vtt": {
                        "u8"
                    }
                },
                "Video": {
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