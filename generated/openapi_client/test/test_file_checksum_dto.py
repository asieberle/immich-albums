# coding: utf-8

"""
    Immich

    Immich API

    The version of the OpenAPI document: 1.88.2
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest
import datetime

from openapi_client.models.file_checksum_dto import FileChecksumDto  # noqa: E501

class TestFileChecksumDto(unittest.TestCase):
    """FileChecksumDto unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> FileChecksumDto:
        """Test FileChecksumDto
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `FileChecksumDto`
        """
        model = FileChecksumDto()  # noqa: E501
        if include_optional:
            return FileChecksumDto(
                filenames = [
                    ''
                    ]
            )
        else:
            return FileChecksumDto(
                filenames = [
                    ''
                    ],
        )
        """

    def testFileChecksumDto(self):
        """Test FileChecksumDto"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()