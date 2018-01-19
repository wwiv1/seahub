# -*- coding: utf-8 -*-

from seahub.test_utils import BaseTestCase
from seahub.thumbnail.utils import generate_thumbnail

from django.test import RequestFactory

class GenerateThumbnailTest(BaseTestCase):
    def setUp(self):
        self.factory = RequestFactory()

    def tearDown(self):
        pass

    def test_generate_thumbnail(self):
        '''
        file_path and repo_id must exist,
        otherwise assert status_code == 500
        '''
        file_path = '1DBC33F9-F621-.png'
        repo_id = '349f89d3-ea03-4bbe-bb3a-e3b3b8032fad'
        url = '/thumbnail/%s/create/' % repo_id
        request = self.factory.get(url)
        success, status_code = generate_thumbnail(request, repo_id, 48, file_path)
        assert success is True
        assert status_code == 200
