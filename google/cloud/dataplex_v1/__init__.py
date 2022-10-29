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


from .services.content_service import ContentServiceAsyncClient, ContentServiceClient
from .services.dataplex_service import DataplexServiceAsyncClient, DataplexServiceClient
from .services.metadata_service import MetadataServiceAsyncClient, MetadataServiceClient
from .types.analyze import Content, Environment, Session
from .types.content import (
    CreateContentRequest,
    DeleteContentRequest,
    GetContentRequest,
    ListContentRequest,
    ListContentResponse,
    UpdateContentRequest,
)
from .types.logs import DiscoveryEvent, JobEvent, SessionEvent
from .types.metadata_ import (
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
from .types.resources import Action, Asset, AssetStatus, Lake, State, Zone
from .types.service import (
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
from .types.tasks import Job, Task

__all__ = (
    "ContentServiceAsyncClient",
    "DataplexServiceAsyncClient",
    "MetadataServiceAsyncClient",
    "Action",
    "Asset",
    "AssetStatus",
    "CancelJobRequest",
    "Content",
    "ContentServiceClient",
    "CreateAssetRequest",
    "CreateContentRequest",
    "CreateEntityRequest",
    "CreateEnvironmentRequest",
    "CreateLakeRequest",
    "CreatePartitionRequest",
    "CreateTaskRequest",
    "CreateZoneRequest",
    "DataplexServiceClient",
    "DeleteAssetRequest",
    "DeleteContentRequest",
    "DeleteEntityRequest",
    "DeleteEnvironmentRequest",
    "DeleteLakeRequest",
    "DeletePartitionRequest",
    "DeleteTaskRequest",
    "DeleteZoneRequest",
    "DiscoveryEvent",
    "Entity",
    "Environment",
    "GetAssetRequest",
    "GetContentRequest",
    "GetEntityRequest",
    "GetEnvironmentRequest",
    "GetJobRequest",
    "GetLakeRequest",
    "GetPartitionRequest",
    "GetTaskRequest",
    "GetZoneRequest",
    "Job",
    "JobEvent",
    "Lake",
    "ListActionsResponse",
    "ListAssetActionsRequest",
    "ListAssetsRequest",
    "ListAssetsResponse",
    "ListContentRequest",
    "ListContentResponse",
    "ListEntitiesRequest",
    "ListEntitiesResponse",
    "ListEnvironmentsRequest",
    "ListEnvironmentsResponse",
    "ListJobsRequest",
    "ListJobsResponse",
    "ListLakeActionsRequest",
    "ListLakesRequest",
    "ListLakesResponse",
    "ListPartitionsRequest",
    "ListPartitionsResponse",
    "ListSessionsRequest",
    "ListSessionsResponse",
    "ListTasksRequest",
    "ListTasksResponse",
    "ListZoneActionsRequest",
    "ListZonesRequest",
    "ListZonesResponse",
    "MetadataServiceClient",
    "OperationMetadata",
    "Partition",
    "Schema",
    "Session",
    "SessionEvent",
    "State",
    "StorageFormat",
    "StorageSystem",
    "Task",
    "UpdateAssetRequest",
    "UpdateContentRequest",
    "UpdateEntityRequest",
    "UpdateEnvironmentRequest",
    "UpdateLakeRequest",
    "UpdateTaskRequest",
    "UpdateZoneRequest",
    "Zone",
)
