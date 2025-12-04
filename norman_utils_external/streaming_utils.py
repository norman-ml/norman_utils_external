import asyncio
from typing import Union, Iterable, AsyncIterable, TypeVar, Callable, AsyncGenerator, Protocol, Any, Literal, overload

T = TypeVar('T')
Processor = Union[Callable[[bytes], Any], Callable[[bytes], T]]

class AsyncBufferedReader(Protocol):
    async def read(self, chunk_size: int) -> bytes: ...

class BufferedReader(Protocol):
    def read(self, chunk_size: int) -> bytes: ...


class StreamingUtils:
    """
    Utility class providing helpers for working with streaming byte sources,
    supporting both synchronous and asynchronous producers.

    These functions are useful for:
    - Merging multiple byte streams (sync or async)
    - Reading from buffered readers in chunks
    - Applying transformations (processing functions) to each chunk
    - Yielding processed or raw output as an async generator

    Supports interaction with:
    - File-like objects exposing `.read()`
    - Async streaming sources (e.g., websocket streams, async file reads)
    - Iterables or async iterables of raw `bytes`

    **Methods**
    """

    @staticmethod
    async def chain_streams(*streams: Union[Iterable[bytes], AsyncIterable[bytes]]) -> AsyncGenerator[bytes, None]:
        """
        Chain multiple byte streams (sync or async) into a single asynchronous
        generator, yielding chunks from each stream in order.

        This function abstracts the difference between:
        - Synchronous iterables of bytes (`Iterable[bytes]`)
        - Asynchronous iterables of bytes (`AsyncIterable[bytes]`)

        making it easy to combine them uniformly.

        **Parameters**

        - **streams** (`*Iterable[bytes] | *AsyncIterable[bytes]`)
          Any number of streams. Each stream must yield raw `bytes`.
          A stream is considered asynchronous if it defines `__aiter__()`.

        **Yields**

        - **bytes** — Byte chunks from each stream in sequence.
        """
        for stream in streams:
            if hasattr(stream, "__aiter__"):
                async for chunk in stream:
                    yield chunk
            else:
                for chunk in stream:
                    yield chunk

    @staticmethod
    async def process_read_stream(
        file_stream: Union[AsyncBufferedReader, BufferedReader],
        processor: Processor[T],
        chunk_size: int,
        yield_processed: bool = True
    ) -> AsyncGenerator[Union[bytes, T], None]:
        """
        Read a file/stream in chunks and optionally process each chunk before
        yielding it. Supports both synchronous and asynchronous `.read()`
        methods.

        This helper is useful when streaming large files or socket data and
        applying on-the-fly transformations, such as:
        - hashing
        - compression / decompression
        - encryption / decryption
        - line parsing
        - transcoding

        **Parameters**

        - **file_stream** (`AsyncBufferedReader | BufferedReader`)
          Object with a `.read(chunk_size)` method.
          If the method is async, it will be awaited automatically.

        - **processor** (`Callable[[bytes], T] | Callable[[bytes], Any]`)
          Function applied to each chunk.
          - If `yield_processed=True`, the output of this function is yielded.
          - If `yield_processed=False`, the raw chunk is yielded instead.

        - **chunk_size** (`int`)
          Maximum number of bytes to read per iteration.

        - **yield_processed** (`bool`, default `True`)
          Controls what gets yielded:
          - `True` → yield `processor(chunk)`
          - `False` → yield the raw `bytes` chunk

        **Yields**

        - If `yield_processed=True`: values of type `T` returned by `processor()`
        - If `yield_processed=False`: raw `bytes` chunks

        **Stops When**

        - `.read()` returns empty bytes (`b""`)
        - `.read()` returns `None`

        """
        while True:
            if asyncio.iscoroutinefunction(file_stream.read):
                chunk = await file_stream.read(chunk_size)
            else:
                chunk = file_stream.read(chunk_size)

            if chunk is None or len(chunk) == 0:
                break

            processed = processor(chunk)

            if yield_processed:
                yield processed
            else:
                yield chunk
