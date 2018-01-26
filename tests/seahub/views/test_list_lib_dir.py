import json
import os

from django.core.urlresolvers import reverse

from seahub.test_utils import BaseTestCase
from seahub.tags.models import FileTag
from seaserv import seafile_api

class ListLibDirTest(BaseTestCase):
    def setUp(self):
        self.login_as(self.user)
        self.endpoint = reverse('list_lib_dir', args=[self.repo.id])
        self.folder_name = os.path.basename(self.folder)
        seafile_api.post_empty_file(self.repo.id,
                                    '/',
                                    filename='test_tags.txt',
                                    username=self.user.username)
        FileTag.objects.get_or_create_file_tag(self.repo.id,
                                               '/', 'test_tags.txt',
                                               False, 'file_tags_test',
                                               self.user.username)
        FileTag.objects.get_or_create_file_tag(self.repo.id,
                                               '/', 'test_tags.txt',
                                               False, 'file_tags',
                                               self.user.username)



    def tearDown(self):
        self.remove_repo()

    def test_can_list(self):
        resp = self.client.get(self.endpoint, HTTP_X_REQUESTED_WITH='XMLHttpRequest')
        self.assertEqual(200, resp.status_code)

        json_resp = json.loads(resp.content)
        assert self.folder_name == json_resp['dirent_list'][0]['obj_name']
        assert self.repo.name == json_resp['repo_name']

    def test_can_list_file_tags(self):
        resp = self.client.get(self.endpoint, HTTP_X_REQUESTED_WITH='XMLHttpRequest')

        json_resp = json.loads(resp.content)
        self.assertIn(u'tags', json_resp['dirent_list'][1])
        assert json_resp['dirent_list'][1]['tags'] is not None
        self.assertEqual([u'file_tags_test',u'file_tags'], json_resp['dirent_list'][1]['tags'])
