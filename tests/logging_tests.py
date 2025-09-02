import io
from concurrent.futures import ThreadPoolExecutor

from fastapi import UploadFile
from pydantic import BaseModel

import norman_utils
from norman_utils.cloud.efs_utils import EFSUtils

metadata_utils = norman_utils.cloud.metadata_utils.MetadataUtils()
norman_logger = norman_utils.logging.norman_logger.NormanLogger()


class ExampleModel(BaseModel):
    fur: str
    tail: str
    age: int

def stress_func():
    for i in range(100):
        norman_logger.debug(f"stress test log {i}")
        norman_sandbox = metadata_utils.get_parameter("norman.sandbox")
        # if norman_sandbox is not None:
        #     print(f"Sandbox: {norman_sandbox}")
        # else:
        #     print(f"No sandbox!")

if __name__ == "__main__":
    print("Starting")

    # tpe = ThreadPoolExecutor(max_workers=10)
    # norman_logger.debug("Testing fast serialization")
    #
    # for i in range(10):
    #     tpe.submit(stress_func)
    #
    # tpe.shutdown()

    # efs_utils = EFSUtils()
    # text = efs_utils.read_primitive_value(file_path=r"D:\Downloads\yona_the_ip_tables_king(v2).txt")
    # file = efs_utils.read_file_sync(file_path=r"D:\Downloads\yona_the_ip_tables_king(v2).txt")
    #
    # primitive_byte_count = efs_utils.write_primitive_value(
    #     primitive_value=5,
    #     working_path=r"D:\Downloads\efs_write_test_work_file1",
    #     complete_path=r"D:\Downloads\efs_write_test_complete_file1"
    # )
    #
    # fastapi_file=UploadFile(file)
    # file_byte_count = efs_utils.write_file_sync(
    #     file=fastapi_file,
    #     working_path=r"D:\Downloads\efs_write_test_work_file2",
    #     complete_path=r"D:\Downloads\efs_write_test_complete_file2"
    # )
    #
    # print(text)
    # print(primitive_byte_count)
    # print(file_byte_count)

    # example_model = ExampleModel.parse_obj({
    #     "fur": "floof",
    #     "tail": "ringed",
    #     "age": 3
    # })
    #
    # norman_logger.debug("Testing BaseModel serialization")
    # norman_logger.info("test object as dict", provided_context={"example_model": example_model.dict()})
    # norman_logger.info("test object as json", provided_context={"example_model": example_model.json()})
    # norman_logger.info("test object raw", ["example_model"])
    #
    # unloggable_file = io.BytesIO(b"")
    # norman_logger.info("test unloggable object", ["unloggable_file"])
    # norman_logger.debug("Testing a normal log after unloggable object was attempted")

    # nest = {
    #     "family_a": {
    #         "raccoon_1": "Bandit",
    #         "raccoon_2": "Cooper",
    #     },
    #     "family_b": {
    #         "raccoon_3": "Rascal"
    #     }
    # }
    # fur = "floof"
    # tail = "ringed"
    # age = 3
    #
    # try:
    #     will_raise_exception = nest["family_c"]
    # except Exception as e:
    #     norman_logger.error("Failed to find raccoon family")
    #
    # norman_logger.add_context_aliases({"leader": "nest.family_b.raccoon_3"})
    # norman_logger.debug("Debug coon", ["fur", "tail", "age", "nest.family_a.raccoon_1", "leader"])
    # norman_logger.error("Error coon", provided_context={"cause": "Not enough raccoons"})
    #
    # print("Examining raccoon")
    # print(norman_utils.raccoons.examine())
