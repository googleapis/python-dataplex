# -*- coding: utf-8 -*-
# Copyright 2020 Google LLC
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
#
# Generated code. DO NOT EDIT!
#
# Snippet for UpdateTask
# NOTE: This snippet has been automatically generated for illustrative purposes only.
# It may require modifications to work in your environment.

# To install the latest published package dependency, execute the following:
#   python3 -m pip install google-cloud-dataplex


# [START dataplex_v1_generated_DataplexService_UpdateTask_sync]
from google.cloud import dataplex_v1


def sample_update_task():
    # Create a client
    client = dataplex_v1.DataplexServiceClient()

    # Initialize request argument(s)
    task = dataplex_v1.Task()
    task.spark.main_jar_file_uri = "main_jar_file_uri_value"
    task.trigger_spec.schedule = "schedule_value"
    task.trigger_spec.type_ = "RECURRING"
    task.execution_spec.service_account = "service_account_value"

    request = dataplex_v1.UpdateTaskRequest(
        task=task,
    )

    # Make the request
    operation = client.update_task(request=request)

    print("Waiting for operation to complete...")

    response = operation.result()

    # Handle the response
    print(response)

# [END dataplex_v1_generated_DataplexService_UpdateTask_sync]
