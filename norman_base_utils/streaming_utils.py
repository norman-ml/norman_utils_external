import asyncio
from typing import Union, Iterable, AsyncIterable, TypeVar, Callable, AsyncGenerator, Protocol, Any, Literal, overload

T = TypeVar('T')
Processor = Union[Callable[[bytes], Any], Callable[[bytes], T]]

class AsyncBufferedReader(Protocol):
    async def read(self, chunk_size: int) -> bytes: ...

class BufferedReader(Protocol):
    def read(self, chunk_size: int) -> bytes: ...


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
            file_stream: Union[AsyncBufferedReader, BufferedReader] ,
            processor: Processor[T],
            chunk_size: int,
            yield_processed: bool = True
    ) -> AsyncGenerator[Union[bytes, T], None]:
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
