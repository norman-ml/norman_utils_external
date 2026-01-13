class EncodingDefaults:
    Container_Encodings = {
        "audio": "mp3",
        "image": "jpg",
        "text": "txt",
        "video": "mp4"
    }

    Channel_Encodings = {
        "audio": {
            "aac": {
                "audio": {
                    "channel": "aac",
                    "sample": "fltp",
                    "tensor": "torch.float32"
                }
            },
            "flac": {
                "audio": {
                    "channel": "flac",
                    "sample": "s16",
                    "tensor": "torch.float32"
                }
            },
            "mp3": {
                "audio": {
                    "channel": "mp3",
                    "sample": "fltp",
                    "tensor": "torch.float32"
                }
            },
            "ogg": {
                "audio": {
                    "channel": "opus",
                    "sample": "flt",
                    "tensor": "torch.float32"
                }
            },
            "wav": {
                "audio": {
                    "channel": "pcm_s16le",
                    "sample": "s16",
                    "tensor": "torch.float32"
                }
            }
        },
        "image": {
            "jpg": {
                "image": {
                    "channel": "rgb",
                    "sample": "rgb8",
                    "tensor": "torch.float32"
                }
            },
            "png": {
                "image": {
                    "channel": "rgb",
                    "sample": "rgba8",
                    "tensor": "torch.float32"
                }
            },
            "webp": {
                "image": {
                    "channel": "rgb",
                    "sample": "rgb8",
                    "tensor": "torch.float32"
                }
            }
        },
        "text": {
            "docx": {
                "text": {
                    "channel": "utf8",
                    "sample": "u8",
                    "tensor": "torch.int64"
                }
            },
            "pdf": {
                "text": {
                    "channel": "utf8",
                    "sample": "u8",
                    "tensor": "torch.int64"
                }
            },
            "txt": {
                "text": {
                    "channel": "utf8",
                    "sample": "u8",
                    "tensor": "torch.int64"
                }
            }
        },
        "video": {
            "mkv": {
                "audio": {
                    "channel": "opus",
                    "sample": "flt",
                    "tensor": "torch.float32"
                },
                "text": {
                    "channel": "srt",
                    "sample": "utf8",
                    "tensor": "torch.int64"
                },
                "video": {
                    "channel": "h264",
                    "sample": "yuv420p",
                    "tensor": "torch.float32"
                }
            },
            "mov": {
                "audio": {
                    "channel": "aac",
                    "sample": "fltp",
                    "tensor": "torch.float32"
                },
                "text": {
                    "channel": "mov_text",
                    "sample": "utf8",
                    "tensor": "torch.int64"
                },
                "video": {
                    "channel": "h264",
                    "sample": "yuv420p",
                    "tensor": "torch.float32"
                }
            },
            "mp4": {
                "audio": {
                    "channel": "aac",
                    "sample": "fltp",
                    "tensor": "torch.float32"
                },
                "text": {
                    "channel": "mov_text",
                    "sample": "utf8",
                    "tensor": "torch.int64"
                },
                "video": {
                    "channel": "h264",
                    "sample": "yuv420p",
                    "tensor": "torch.float32"
                }
            },
            "ogg": {
                "audio": {
                    "channel": "opus",
                    "sample": "flt",
                    "tensor": "torch.float32"
                },
                "text": {
                    "channel": "kate",
                    "sample": "utf8",
                    "tensor": "torch.int64"
                },
                "video": {
                    "channel": "theora",
                    "sample": "yuv420p",
                    "tensor": "torch.float32"
                }
            },
            "webm": {
                "audio": {
                    "channel": "opus",
                    "sample": "flt",
                    "tensor": "torch.float32"
                },
                "text": {
                    "channel": "vtt",
                    "sample": "utf8",
                    "tensor": "torch.int64"
                },
                "video": {
                    "channel": "vp9",
                    "sample": "yuv420p",
                    "tensor": "torch.float32"
                }
            }
        }
    }