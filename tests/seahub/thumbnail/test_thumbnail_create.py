# -*- coding: utf-8 -*-

from seahub.test_utils import BaseTestCase

from django.core.urlresolvers import reverse

class ThumbnailCreateTest(BaseTestCase):
    def setUp(self):
        self.login_as(self.user)

    def tearDown(self):
        self.remove_repo(self.repo.id)

    def test_repo_not_exist(self):
        url = reverse('thumbnail_create', kwargs={
            'repo_id': '349f89d3-ea03-4bbe-bb3a-e3b3b8032fad'
        })
        resp = self.client.get(url, HTTP_X_REQUESTED_WITH='XMLHttpRequest')
        self.assertEqual(400, resp.status_code)

    def test_path_not_exit(self):
        url = reverse('thumbnail_create', kwargs={
            'repo_id': self.repo.id
        })
        resp = self.client.get(url, HTTP_X_REQUESTED_WITH='XMLHttpRequest')
        self.assertEqual(400, resp.status_code)
