class EncodingDefaults:
    Container_Map = {
        "audio": "mp3",
        "image": "jpg",
        "text": "txt",
        "video": "mp4"
    }

    Channel_Map = {
        "audio": {
            "aac": {
                "audio": {
                    "channel": "aac",
                    "sample": "fltp",
                    "tensor": "float32"
                }
            },
            "flac": {
                "audio": {
                    "channel": "flac",
                    "sample": "s16",
                    "tensor": "float32"
                }
            },
            "mp3": {
                "audio": {
                    "channel": "mp3",
                    "sample": "fltp",
                    "tensor": "float32"
                }
            },
            "ogg": {
                "audio": {
                    "channel": "opus",
                    "sample": "flt",
                    "tensor": "float32"
                }
            },
            "wav": {
                "audio": {
                    "channel": "pcm_s16le",
                    "sample": "s16",
                    "tensor": "float32"
                }
            }
        },
        "image": {
            "jpg": {
                "image": {
                    "channel": "RGB",
                    "sample": "uint8",
                    "tensor": "uint8"
                }
            },
            "png": {
                "image": {
                    "channel": "RGBA",
                    "sample": "uint8",
                    "tensor": "uint8"
                }
            },
            "webp": {
                "image": {
                    "channel": "RGB",
                    "sample": "uint8",
                    "tensor": "uint8"
                }
            }
        },
        "text": {
            "docx": {
                "text": {
                    "channel": "utf8",
                    "sample": "u8",
                    "tensor": "int64"
                }
            },
            "pdf": {
                "text": {
                    "channel": "utf8",
                    "sample": "u8",
                    "tensor": "int64"
                }
            },
            "txt": {
                "text": {
                    "channel": "utf8",
                    "sample": "u8",
                    "tensor": "int64"
                }
            }
        },
        "video": {
            "mkv": {
                "audio": {
                    "channel": "opus",
                    "sample": "flt",
                    "tensor": "float32"
                },
                "text": {
                    "channel": "srt",
                    "sample": "utf8",
                    "tensor": "int64"
                },
                "video": {
                    "channel": "h264",
                    "sample": "yuv420p",
                    "tensor": "float32"
                }
            },
            "mov": {
                "audio": {
                    "channel": "aac",
                    "sample": "fltp",
                    "tensor": "float32"
                },
                "text": {
                    "channel": "mov_text",
                    "sample": "utf8",
                    "tensor": "int64"
                },
                "video": {
                    "channel": "h264",
                    "sample": "yuv420p",
                    "tensor": "float32"
                }
            },
            "mp4": {
                "audio": {
                    "channel": "aac",
                    "sample": "fltp",
                    "tensor": "float32"
                },
                "text": {
                    "channel": "mov_text",
                    "sample": "utf8",
                    "tensor": "int64"
                },
                "video": {
                    "channel": "h264",
                    "sample": "yuv420p",
                    "tensor": "float32"
                }
            },
            "webm": {
                "audio": {
                    "channel": "opus",
                    "sample": "flt",
                    "tensor": "float32"
                },
                "text": {
                    "channel": "vtt",
                    "sample": "utf8",
                    "tensor": "int64"
                },
                "video": {
                    "channel": "vp9",
                    "sample": "yuv420p",
                    "tensor": "float32"
                }
            }
        }
    }