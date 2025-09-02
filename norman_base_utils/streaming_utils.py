from typing import Union, Iterable, AsyncIterable, TypeVar, Callable, AsyncGenerator, Protocol

T = TypeVar('T')
Processor = Union[Callable[[bytes], None], Callable[[bytes], T]]


class AsyncBufferedReader(Protocol):
    async def read(self, chunk_size: int) -> bytes: ...


class StreamingUtils:
    @staticmethod
    async def chain_streams(*streams: Union[Iterable[bytes], AsyncIterable[bytes]]):
        for stream in streams:
            if hasattr(stream, "__aiter__"):
                async for chunk in stream:
                    yield chunk
            else:
                for chunk in stream:
                    yield chunk

    @staticmethod
    async def process_read_stream(
            file_stream: AsyncBufferedReader,
            processor: Processor[T],
            chunk_size: int,
            return_processed: bool = False
    ) -> AsyncGenerator[Union[bytes, T], None]:
        while True:
            chunk = await file_stream.read(chunk_size)
            if not chunk:
                break
            processed = processor(chunk)
            yield processed if return_processed else chunk
