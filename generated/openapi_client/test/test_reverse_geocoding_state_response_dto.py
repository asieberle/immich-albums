# coding: utf-8

"""
    Immich

    Immich API

    The version of the OpenAPI document: 1.105.1
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from openapi_client.models.reverse_geocoding_state_response_dto import ReverseGeocodingStateResponseDto

class TestReverseGeocodingStateResponseDto(unittest.TestCase):
    """ReverseGeocodingStateResponseDto unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> ReverseGeocodingStateResponseDto:
        """Test ReverseGeocodingStateResponseDto
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `ReverseGeocodingStateResponseDto`
        """
        model = ReverseGeocodingStateResponseDto()
        if include_optional:
            return ReverseGeocodingStateResponseDto(
                last_import_file_name = '',
                last_update = ''
            )
        else:
            return ReverseGeocodingStateResponseDto(
                last_import_file_name = '',
                last_update = '',
        )
        """

    def testReverseGeocodingStateResponseDto(self):
        """Test ReverseGeocodingStateResponseDto"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
