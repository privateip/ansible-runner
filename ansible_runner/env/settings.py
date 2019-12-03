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


class Settings(Object):

    idle_timeout = make_attr('integer')
    job_timeout = make_attr('integer')
    pexpect_timeout = make_attr('integer')
    pexpect_use_poll = make_attr('boolean')
    suppress_ansible_output = make_attr('boolean')

    fact_cache = make_attr('string')
    fact_cache_type = make_attr('string')

    process_isolation = make_attr('boolean')
    process_isolation_executable = make_attr('string')
    process_isolation_path = make_attr('string')
    process_isolation_hide_paths = make_attr('list')
    process_isolation_show_paths = make_attr('list')
    process_isloation_ro_paths = make_attr('list')

    resource_profiling = make_attr('boolean')
    resource_profiling_base_cgroup = make_attr('string')
    resource_profiling_cpu_poll_interval = make_attr('float')
    resource_profiling_memory_poll_interval = make_attr('float')
    resource_profiling_pid_poll_interval = make_attr('float')
    resource_profiling_reesults_dir = make_attr('string')
