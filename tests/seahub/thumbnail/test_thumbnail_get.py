# -*- coding: utf-8 -*-

from seahub.test_utils import BaseTestCase
from django.core.urlresolvers import reverse

class ThumbnailGetTest(BaseTestCase):
    def test_thumbnail_get(self):
        self.login_as(self.user)
        file_path = self.create_file(repo_id=self.repo.id,
                                     parent_dir='',
                                     filename='test.png',
                                     username=self.user.username)
        url = reverse('thumbnail_get', kwargs={
            'repo_id': self.repo.id,
            'size': 48,
            'path': file_path
        })
        resp = self.client.get(url)
        self.assertEqual(200, resp.status_code)
