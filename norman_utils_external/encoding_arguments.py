class EncodingArguments:
    Arguments_Map = {
        "audio": {
            "aac": {
                "audio": {
                    "bit_depth": 32,
                    "bit_rate": 128000,
                    "channels": 1,
                    "frame_size": 1024,
                    "sample_rate": 48000
                }
            },
            "flac": {
                "audio": {
                    "bit_depth": 16,
                    "channels": 2,
                    "compression_level": 5,
                    "frame_size": 4096,
                    "sample_rate": 48000
                }
            },
            "mp3": {
                "audio": {
                    "bit_depth": 32,
                    "bit_rate": 128000,
                    "channels": 2,
                    "frame_size": 1152,
                    "sample_rate": 48000
                }
            },
            "ogg": {
                "audio": {
                    "bit_depth": 32,
                    "bit_rate": 96000,
                    "channels": 2,
                    "frame_size": 960,
                    "sample_rate": 48000
                }
            },
            "wav": {
                "audio": {
                    "bit_depth": 16,
                    "channels": 2,
                    "frame_size": 1024,
                    "sample_rate": 48000
                }
            },
        },
        "image": {
            "jpg": {
                "image": {
                    "bit_depth": 8,
                    "channels": 3
                }
            },
            "png": {
                "image": {
                    "bit_depth": 8,
                    "channels": 4
                }
            },
            "webp": {
                "image": {
                    "bit_depth": 8,
                    "channels": 3
                }
            },
        },
        "text": {
            "docx": {
                "text": {
                    "bit_depth": 8,
                    "channels": 1
                }
            },
            "pdf": {
                "text": {
                    "bit_depth": 8,
                    "channels": 1
                }
            },
            "txt": {
                "text": {
                    "bit_depth": 8,
                    "channels": 1
                }
            },
        },
        "video": {
            "mkv": {
                "audio": {
                    "bit_depth": 32,
                    "bit_rate": 96000,
                    "channels": 2,
                    "frame_size": 960,
                    "sample_rate": 48000
                },
                "text": {
                    "bit_depth": 8,
                    "channels": 1
                },
                "video": {
                    "bit_depth": 8,
                    "channels": 3,
                    "frame_rate": 30
                }
            },
            "mov": {
                "audio": {
                    "bit_depth": 32,
                    "bit_rate": 128000,
                    "channels": 2,
                    "frame_size": 1024,
                    "sample_rate": 48000
                },
                "text": {
                    "bit_depth": 8,
                    "channels": 1
                },
                "video": {
                    "bit_depth": 8,
                    "channels": 3,
                    "frame_rate": 30
                }
            },
            "mp4": {
                "audio": {
                    "bit_depth": 32,
                    "bit_rate": 128000,
                    "channels": 2,
                    "frame_size": 1024,
                    "sample_rate": 48000
                },
                "text": {
                    "bit_depth": 8,
                    "channels": 1
                },
                "video": {
                    "bit_depth": 8,
                    "channels": 3,
                    "frame_rate": 30
                }
            },
            "ogg": {
                "audio": {
                    "bit_depth": 32,
                    "bit_rate": 96000,
                    "channels": 2,
                    "frame_size": 960,
                    "sample_rate": 48000
                },
                "text": {
                    "bit_depth": 8,
                    "channels": 1
                },
                "video": {
                    "bit_depth": 8,
                    "channels": 3,
                    "frame_rate": 30
                }
            },
            "webm": {
                "audio": {
                    "bit_depth": 32,
                    "bit_rate": 96000,
                    "channels": 2,
                    "frame_size": 960,
                    "sample_rate": 48000
                },
                "text": {
                    "bit_depth": 8,
                    "channels": 1
                },
                "video": {
                    "bit_depth": 8,
                    "channels": 3,
                    "frame_rate": 30
                }
            }
        }
    }