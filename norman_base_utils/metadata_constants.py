import os

from norman_base_utils.singleton import Singleton


class MetadataConstants(metaclass=Singleton):
    def __init__(self):
        # aws metadata server static ip address
        self.metadata_server_ip = "169.254.169.254"

        # config profiles
        project_folder_name = os.getcwd().split(os.sep)[-1]  # expecting "norman_service_name"
        service_name = project_folder_name.replace("_", "-") # expecting "norman-service-name"
        self.config_profile_names = [
            "norman-base-config",
            f"{service_name}-config"  # expecting "norman-service-name-config"
        ]

        # metadata parameters
        self.metadata_parameter_paths = {
            "instance_id": "latest/meta-data/instance-id",
            "public_ipv4": "latest/meta-data/public-ipv4",
            "local_ipv4": "latest/meta-data/local-ipv4"
        }

        # identity document path
        self.identity_document_path = "latest/dynamic/instance-identity/document"
