# -*- coding: utf-8 -*-
# Copyright 2022 Google LLC
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
from google.cloud.dataplex import gapic_version as package_version

__version__ = package_version.__version__


from google.cloud.dataplex_v1.services.content_service.async_client import (
    ContentServiceAsyncClient,
)
from google.cloud.dataplex_v1.services.content_service.client import (
    ContentServiceClient,
)
from google.cloud.dataplex_v1.services.dataplex_service.async_client import (
    DataplexServiceAsyncClient,
)
from google.cloud.dataplex_v1.services.dataplex_service.client import (
    DataplexServiceClient,
)
from google.cloud.dataplex_v1.services.metadata_service.async_client import (
    MetadataServiceAsyncClient,
)
from google.cloud.dataplex_v1.services.metadata_service.client import (
    MetadataServiceClient,
)
from google.cloud.dataplex_v1.types.analyze import Content, Environment, Session
from google.cloud.dataplex_v1.types.content import (
    CreateContentRequest,
    DeleteContentRequest,
    GetContentRequest,
    ListContentRequest,
    ListContentResponse,
    UpdateContentRequest,
)
from google.cloud.dataplex_v1.types.logs import DiscoveryEvent, JobEvent, SessionEvent
from google.cloud.dataplex_v1.types.metadata_ import (
    CreateEntityRequest,
    CreatePartitionRequest,
    DeleteEntityRequest,
    DeletePartitionRequest,
    Entity,
    GetEntityRequest,
    GetPartitionRequest,
    ListEntitiesRequest,
    ListEntitiesResponse,
    ListPartitionsRequest,
    ListPartitionsResponse,
    Partition,
    Schema,
    StorageFormat,
    StorageSystem,
    UpdateEntityRequest,
)
from google.cloud.dataplex_v1.types.resources import (
    Action,
    Asset,
    AssetStatus,
    Lake,
    State,
    Zone,
)
from google.cloud.dataplex_v1.types.service import (
    CancelJobRequest,
    CreateAssetRequest,
    CreateEnvironmentRequest,
    CreateLakeRequest,
    CreateTaskRequest,
    CreateZoneRequest,
    DeleteAssetRequest,
    DeleteEnvironmentRequest,
    DeleteLakeRequest,
    DeleteTaskRequest,
    DeleteZoneRequest,
    GetAssetRequest,
    GetEnvironmentRequest,
    GetJobRequest,
    GetLakeRequest,
    GetTaskRequest,
    GetZoneRequest,
    ListActionsResponse,
    ListAssetActionsRequest,
    ListAssetsRequest,
    ListAssetsResponse,
    ListEnvironmentsRequest,
    ListEnvironmentsResponse,
    ListJobsRequest,
    ListJobsResponse,
    ListLakeActionsRequest,
    ListLakesRequest,
    ListLakesResponse,
    ListSessionsRequest,
    ListSessionsResponse,
    ListTasksRequest,
    ListTasksResponse,
    ListZoneActionsRequest,
    ListZonesRequest,
    ListZonesResponse,
    OperationMetadata,
    UpdateAssetRequest,
    UpdateEnvironmentRequest,
    UpdateLakeRequest,
    UpdateTaskRequest,
    UpdateZoneRequest,
)
from google.cloud.dataplex_v1.types.tasks import Job, Task

__all__ = (
    "ContentServiceClient",
    "ContentServiceAsyncClient",
    "DataplexServiceClient",
    "DataplexServiceAsyncClient",
    "MetadataServiceClient",
    "MetadataServiceAsyncClient",
    "Content",
    "Environment",
    "Session",
    "CreateContentRequest",
    "DeleteContentRequest",
    "GetContentRequest",
    "ListContentRequest",
    "ListContentResponse",
    "UpdateContentRequest",
    "DiscoveryEvent",
    "JobEvent",
    "SessionEvent",
    "CreateEntityRequest",
    "CreatePartitionRequest",
    "DeleteEntityRequest",
    "DeletePartitionRequest",
    "Entity",
    "GetEntityRequest",
    "GetPartitionRequest",
    "ListEntitiesRequest",
    "ListEntitiesResponse",
    "ListPartitionsRequest",
    "ListPartitionsResponse",
    "Partition",
    "Schema",
    "StorageFormat",
    "UpdateEntityRequest",
    "StorageSystem",
    "Action",
    "Asset",
    "AssetStatus",
    "Lake",
    "Zone",
    "State",
    "CancelJobRequest",
    "CreateAssetRequest",
    "CreateEnvironmentRequest",
    "CreateLakeRequest",
    "CreateTaskRequest",
    "CreateZoneRequest",
    "DeleteAssetRequest",
    "DeleteEnvironmentRequest",
    "DeleteLakeRequest",
    "DeleteTaskRequest",
    "DeleteZoneRequest",
    "GetAssetRequest",
    "GetEnvironmentRequest",
    "GetJobRequest",
    "GetLakeRequest",
    "GetTaskRequest",
    "GetZoneRequest",
    "ListActionsResponse",
    "ListAssetActionsRequest",
    "ListAssetsRequest",
    "ListAssetsResponse",
    "ListEnvironmentsRequest",
    "ListEnvironmentsResponse",
    "ListJobsRequest",
    "ListJobsResponse",
    "ListLakeActionsRequest",
    "ListLakesRequest",
    "ListLakesResponse",
    "ListSessionsRequest",
    "ListSessionsResponse",
    "ListTasksRequest",
    "ListTasksResponse",
    "ListZoneActionsRequest",
    "ListZonesRequest",
    "ListZonesResponse",
    "OperationMetadata",
    "UpdateAssetRequest",
    "UpdateEnvironmentRequest",
    "UpdateLakeRequest",
    "UpdateTaskRequest",
    "UpdateZoneRequest",
    "Job",
    "Task",
)
