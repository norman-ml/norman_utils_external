class EncodingDefaults:
    Container_Map = {
        "Audio": "mp3",
        "Image": "jpg",
        "Text": "txt",
        "Video": "mp4"
    }

    Channel_Map = {
        "Audio": {
            "aac": {
                "Audio": {
                    "channel": "aac",
                    "sample": "fltp",
                    "tensor": "float32"
                }
            },
            "flac": {
                "Audio": {
                    "channel": "flac",
                    "sample": "s16",
                    "tensor": "float32"
                }
            },
            "mp3": {
                "Audio": {
                    "channel": "mp3",
                    "sample": "fltp",
                    "tensor": "float32"
                }
            },
            "ogg": {
                "Audio": {
                    "channel": "opus",
                    "sample": "flt",
                    "tensor": "float32"
                }
            },
            "wav": {
                "Audio": {
                    "channel": "pcm_s16le",
                    "sample": "s16",
                    "tensor": "float32"
                }
            }
        },
        "Float": {
            "txt": {
                "Float": {
                    "channel": "utf8",
                    "sample": "u8",
                    "tensor": "float32"
                }
            }
        },
        "Image": {
            "jpg": {
                "Image": {
                    "channel": "RGB",
                    "sample": "uint8",
                    "tensor": "uint8"
                }
            },
            "png": {
                "Image": {
                    "channel": "RGBA",
                    "sample": "uint8",
                    "tensor": "uint8"
                }
            },
            "webp": {
                "Image": {
                    "channel": "RGB",
                    "sample": "uint8",
                    "tensor": "uint8"
                }
            }
        },
        "Integer": {
            "txt": {
                "Integer": {
                    "channel": "utf8",
                    "sample": "u8",
                    "tensor": "int32"
                }
            }
        },
        "Text": {
            "docx": {
                "Text": {
                    "channel": "utf8",
                    "sample": "u8",
                    "tensor": "int64"
                }
            },
            "pdf": {
                "Text": {
                    "channel": "utf8",
                    "sample": "u8",
                    "tensor": "int64"
                }
            },
            "txt": {
                "Text": {
                    "channel": "utf8",
                    "sample": "u8",
                    "tensor": "int64"
                }
            }
        },
        "Video": {
            "mkv": {
                "Audio": {
                    "channel": "opus",
                    "sample": "flt",
                    "tensor": "float32"
                },
                "Text": {
                    "channel": "srt",
                    "sample": "utf8",
                    "tensor": "int64"
                },
                "Video": {
                    "channel": "h264",
                    "sample": "yuv420p",
                    "tensor": "float32"
                }
            },
            "mov": {
                "Audio": {
                    "channel": "aac",
                    "sample": "fltp",
                    "tensor": "float32"
                },
                "Text": {
                    "channel": "mov_text",
                    "sample": "utf8",
                    "tensor": "int64"
                },
                "Video": {
                    "channel": "h264",
                    "sample": "yuv420p",
                    "tensor": "float32"
                }
            },
            "mp4": {
                "Audio": {
                    "channel": "aac",
                    "sample": "fltp",
                    "tensor": "float32"
                },
                "Text": {
                    "channel": "mov_text",
                    "sample": "utf8",
                    "tensor": "int64"
                },
                "Video": {
                    "channel": "h264",
                    "sample": "yuv420p",
                    "tensor": "float32"
                }
            },
            "webm": {
                "Audio": {
                    "channel": "opus",
                    "sample": "flt",
                    "tensor": "float32"
                },
                "Text": {
                    "channel": "vtt",
                    "sample": "utf8",
                    "tensor": "int64"
                },
                "Video": {
                    "channel": "vp9",
                    "sample": "yuv420p",
                    "tensor": "float32"
                }
            }
        }
    }