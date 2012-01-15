#!/usr/bin/env python
#
# Copyright 2011 Fullboar Creative, Corp. All Rights Reserved.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#      http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.


from dictshield.fields import IntField, StringField

from pyvotal.manager import ResourceManager
from pyvotal.fields import PyDateTimeField, PyBooleanField
from pyvotal.document import PyvotalDocument


class TaskManager(ResourceManager):
    """
    Class for tasks retrieval. Availeable as Story.tasks
    """

    def __init__(self, client, project_id, story_id):
        self.client = client
        endpoint = 'projects/%s/stories/%s/tasks' % (project_id, story_id)
        super(TaskManager, self).__init__(client, Task, endpoint)


class Task(PyvotalDocument):
    """
    Parsed response from api with task info
    """
    description = StringField()
    position = IntField()
    complete = PyBooleanField()
    created_at = PyDateTimeField()

    _tagname = 'task'

    def save(self):
        # FIXME do we need this
        data = self._to_xml(excludes=['id', 'created_at'])
        self.client.put('%s/%s' % (self.endpoint, self.id), data)
