# coding: utf-8

"""
    Immich

    Immich API

    The version of the OpenAPI document: 1.105.1
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from openapi_client.models.delete_user_dto import DeleteUserDto

class TestDeleteUserDto(unittest.TestCase):
    """DeleteUserDto unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> DeleteUserDto:
        """Test DeleteUserDto
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `DeleteUserDto`
        """
        model = DeleteUserDto()
        if include_optional:
            return DeleteUserDto(
                force = True
            )
        else:
            return DeleteUserDto(
        )
        """

    def testDeleteUserDto(self):
        """Test DeleteUserDto"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
