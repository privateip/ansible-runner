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
from ansible_runner.types.objects import Object
from ansible_runner.helpers import make_attr


class Cmdline(Object):

    flush_cache = make_attr('boolean')
    force_handlers = make_attr('boolean')
    skip_tags = make_attr('list')
    start_at_task = make_attr('string')
    check = make_attr('boolean')
    diff = make_attr('boolean')
    forks = make_attr('integer')
    tags = make_attr('list')
    verbose = make_attr('integer')
    raw = make_attr('string')



