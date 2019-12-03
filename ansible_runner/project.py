#
# Licensed to the Apache Software Foundation (ASF) under one
# or more contributor license agreements.  See the NOTICE file
# distributed with this work for additional information
# regarding copyright ownership.  The ASF licenses this file
# to you under the Apache License, Version 2.0 (the
# "License"); you may not use this file except in compliance
# with the License.  You may obtain a copy of the License at
#
#   http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing,
# software distributed under the License is distributed on an
# "AS IS" BASIS, WITHOUT WARRANTIES OR CONDITIONS OF ANY
# KIND, either express or implied.  See the License for the
# specific language governing permissions and limitations
# under the License.
#
import os

from ansible_runner.types.objects import Object
from ansible_runner.helpers import make_attr
from ansible_runner.utils import dump_artifacts


class Project(Object):

    private_data_dir = make_attr('string', required=True)

    playbook = make_attr('any', cls='ansible_runner.playbook:Playbook')
    inventory = make_attr('any', cls='ansible_runner.inventory:Inventory')

    envvars = make_attr('dict')
    extravars = make_attr('any', cls='ansible_runner.env.extravars:Extravars')
    #passwords = make_attr('any', cls='ansible_runner.passwords:Passwords')
    passwords = make_attr('dict')
    cmdline = make_attr('any', cls='ansible_runner.env.cmdline:Cmdline')
    settings = make_attr('any', cls='ansible_runner.env.settings:Settings')
    ssh_key = make_attr('string')


    def write(self):
        if not os.path.exists(self.private_data_dir):
            os.makedirs(self.private_data_dir)
        dump_artifacts(self.serialize())

