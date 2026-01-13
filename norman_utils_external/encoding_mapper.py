class EncodingMapper:
    Encoding_Map = {
        "audio": {
            "aac": {
                "audio": {
                    "aac": [
                        "flt",
                        "fltp",
                        "s16",
                        "s16p",
                        "s32",
                        "s32p"
                    ],
                    "aac_lc": [
                        "flt",
                        "fltp",
                        "s16",
                        "s16p",
                        "s32",
                        "s32p"
                    ],
                    "aac_he": [
                        "flt",
                        "fltp",
                        "s16",
                        "s16p"
                    ]
                }
            },
            "ac3": {
                "audio": {
                    "ac3": [
                        "s16",
                        "s16p",
                        "s32",
                        "s32p"
                    ]
                }
            },
            "flac": {
                "audio": {
                    "flac": [
                        "flt",
                        "s16",
                        "s24",
                        "s32"
                    ]
                }
            },
            "opus": {
                "audio": {
                    "opus": [
                        "flt",
                        "fltp",
                        "s16"
                    ]
                }
            },
            "mp3": {
                "audio": {
                    "mp3": [
                        "flt",
                        "fltp",
                        "s16",
                        "s16p"
                    ],
                    "mp3_vbr": [
                        "flt",
                        "fltp",
                        "s16",
                        "s16p",
                    ]
                }
            },
            "vorbis": {
                "audio": {
                    "vorbis": [
                        "flt",
                        "fltp",
                        "s16"
                    ]
                }
            },
            "wav": {
                "audio": {
                    "pcm": [
                        "pcm_f32le",
                        "pcm_s16le",
                        "pcm_s24le",
                        "pcm_s32le"
                    ]
                }
            }
        },
        "image": {
            "jpg": {
                "image": {
                    "gray": [
                        "gray8"
                    ],
                    "rgb": [
                        "rgb8"
                    ],
                    "yuv420": [
                        "yuv420p"
                    ],
                    "yuv444": [
                        "yuv444p"
                    ]
                }
            },
            "png": {
                "image": {
                    "indexed": [
                        "palette8"
                    ],
                    "gray": [
                        "gray8"
                    ],
                    "rgb": [
                        "rgb8"
                    ],
                    "rgba": [
                        "rgba8"
                    ]
                }
            },
            "webp": {
                "image": {
                    "gray": [
                        "gray8"
                    ],
                    # lossless
                    "rgb": [
                        "rgb8"
                    ],
                    # lossless + alpha
                    "rgba": [
                        "rgba8"
                    ],
                    # lossy
                    "yuv420": [
                        "yuv420p"
                    ]
                }
            }
        },
        "text": {
            "txt": {
                "text": {
                    "utf8": [],
                    "utf16": []
                }
            },
            "pdf": {
                "text": {
                    "utf8": [],
                    "utf16": []
                }
            },
            "docx": {
                "text": {
                    "utf8": [],
                    "utf16": []
                }
            },
            "rtf": {
                "text": {
                    "utf8": [],
                    "utf16": []
                }
            }
        },
        "video": {
            "avi": {
                "audio": {
                    "ac3": [
                        "s16",
                        "s16p"
                    ],
                    "mp3": [
                        "s16",
                        "s16p"
                    ],
                    "pcm_s16le": [
                        "s16"
                    ]
                },
                "text": {},
                "video": {
                    "cinepak": [
                        "rgb8"
                    ],
                    "h264": [
                        "yuv420p"
                    ],
                    "dv": [
                        "yuv420p"
                    ],
                    "motion-jpeg": [
                        "yuv420p",
                        "rgb8"
                    ],
                    "mpeg4": [
                        "yuv420p"
                    ],
                }
            },
            "matroska": {
                "audio": {
                    "aac": [
                        "flt",
                        "fltp",
                        "s16",
                        "s16p",
                        "s32"
                    ],
                    "aac_he": [
                        "flt",
                        "fltp",
                        "s16"
                    ],
                    "ac3": [
                        "s16",
                        "s16p",
                        "s32",
                        "s32p"
                    ],
                    "flac": [
                        "flt",
                        "s16",
                        "s24",
                        "s32"
                    ],
                    "mp3": [
                        "flt",
                        "fltp",
                        "s16",
                        "s16p"
                    ],
                    "opus": [
                        "flt",
                        "fltp",
                        "s16"
                    ],
                    "pcm_s16le": [
                        "s16"
                    ],
                    "pcm_s24le": [
                        "s24"
                    ],
                    "vorbis": [
                        "flt",
                        "fltp",
                        "s16"
                    ]
                },
                "text": {
                    "ass": [
                        "utf8"
                    ],
                    "srt": [
                        "utf8"
                    ],
                    "vtt": [
                        "utf8"
                    ]
                },
                "video": {
                    "av1": [
                        "rgb8",
                        "yuv420p",
                        "yuv444p"
                    ],
                    "vp8": [
                        "yuv420p"
                    ],
                    "h264": [
                        "rgb8",
                        "yuv420p",
                        "yuv444p"
                    ],
                    "h265": [
                        "rgb8",
                        "yuv420p",
                        "yuv444p"
                    ],
                    "vp9": [
                        "yuv420p"
                    ]
                }
            },
            "mov": {
                "audio": {
                    "aac": [
                        "flt",
                        "fltp",
                        "s16",
                        "s16p",
                        "s32"
                    ],
                    "aac_he": [
                        "flt",
                        "fltp",
                        "s16"
                    ],
                    "alac": [
                        "s16",
                        "s24",
                        "s32"
                    ],
                    "mp3": [
                        "flt",
                        "fltp",
                        "s16",
                        "s16p"
                    ],
                    "pcm_s16le": [
                        "s16"
                    ]
                },
                "text": {
                    "ass": [
                        "utf8"
                    ],
                    "srt": [
                        "utf8"
                    ],
                    "vtt": [
                        "utf8"
                    ]
                },
                "video": {
                    "av1": [
                        "rgb8",
                        "yuv420p",
                        "yuv444p"
                    ],
                    "cinepak": [
                        "rgb8"
                    ],
                    "dv": [
                        "yuv420p"
                    ],
                    "h264": [
                        "rgb8",
                        "yuv420p",
                        "yuv444p"
                    ],
                    "h265": [
                        "rgb8",
                        "yuv420p",
                        "yuv444p"
                    ],
                    "motion-jpeg": [
                        "rgb8",
                        "yuv420p"
                    ],
                }
            },
            "mp4": {
                "audio": {
                    "aac": [
                        "flt",
                        "fltp",
                        "s16",
                        "s16p",
                        "s32",
                        "s32p"
                    ],
                    "aac_he": [
                        "flt",
                        "fltp",
                        "s16",
                        "s16p"
                    ],
                    "flac": [
                        "flt",
                        "s16",
                        "s24",
                        "s32"
                    ],
                    "mp3": [
                        "flt",
                        "fltp",
                        "s16",
                        "s16p"
                    ],
                    "opus": [
                        "flt",
                        "fltp",
                        "s16"
                    ]
                },
                "text": {
                    "ass": [
                        "utf8"
                    ],
                    "srt": [
                        "utf8"
                    ],
                    "vtt": [
                        "utf8"
                    ]
                },
                "video": {
                    "av1": [
                        "rgb8",
                        "yuv420p",
                        "yuv444p"
                    ],
                    "h264": [
                        "rgb8",
                        "yuv420p",
                        "yuv444p"
                    ],
                    "h265": [
                        "rgb8",
                        "yuv420p",
                        "yuv444p"
                    ],
                    "vp9": [
                        "yuv420p"
                    ]
                }
            },
            "ogg": {
                "audio": {
                    "flac": ["flt", "s16", "s24", "s32"],
                    "opus": ["flt", "fltp", "s16"],
                    "vorbis": ["flt", "fltp", "s16"]
                },
                "text": {
                    "vtt": [
                        "utf8"
                    ]
                },
                "video": {
                    "vp8": [
                        "yuv420p"
                    ],
                    "vp9": [
                        "yuv420p"
                    ]
                },
            },
            "webm": {
                "audio": {
                    "opus": ["flt", "fltp", "s16"],
                    "vorbis": ["flt", "fltp", "s16"]
                },
                "text": {
                    "vtt": [
                        "utf8"
                    ]
                },
                "video": {
                    "av1": [
                        "yuv420p"
                    ],
                    "vp8": [
                        "yuv420p"
                    ],
                    "vp9": [
                        "yuv420p"
                    ]
                }
            }
        }
    }