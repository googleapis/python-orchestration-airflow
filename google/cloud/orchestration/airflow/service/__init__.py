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
from google.cloud.orchestration.airflow.service import gapic_version as package_version

__version__ = package_version.__version__


from google.cloud.orchestration.airflow.service_v1.services.environments.async_client import (
    EnvironmentsAsyncClient,
)
from google.cloud.orchestration.airflow.service_v1.services.environments.client import (
    EnvironmentsClient,
)
from google.cloud.orchestration.airflow.service_v1.services.image_versions.async_client import (
    ImageVersionsAsyncClient,
)
from google.cloud.orchestration.airflow.service_v1.services.image_versions.client import (
    ImageVersionsClient,
)
from google.cloud.orchestration.airflow.service_v1.types.environments import (
    CheckUpgradeResponse,
    CreateEnvironmentRequest,
    DatabaseConfig,
    DeleteEnvironmentRequest,
    EncryptionConfig,
    Environment,
    EnvironmentConfig,
    GetEnvironmentRequest,
    IPAllocationPolicy,
    ListEnvironmentsRequest,
    ListEnvironmentsResponse,
    LoadSnapshotRequest,
    LoadSnapshotResponse,
    MaintenanceWindow,
    MasterAuthorizedNetworksConfig,
    NetworkingConfig,
    NodeConfig,
    PrivateClusterConfig,
    PrivateEnvironmentConfig,
    RecoveryConfig,
    SaveSnapshotRequest,
    SaveSnapshotResponse,
    ScheduledSnapshotsConfig,
    SoftwareConfig,
    UpdateEnvironmentRequest,
    WebServerConfig,
    WebServerNetworkAccessControl,
    WorkloadsConfig,
)
from google.cloud.orchestration.airflow.service_v1.types.image_versions import (
    ImageVersion,
    ListImageVersionsRequest,
    ListImageVersionsResponse,
)
from google.cloud.orchestration.airflow.service_v1.types.operations import (
    OperationMetadata,
)

__all__ = (
    "EnvironmentsClient",
    "EnvironmentsAsyncClient",
    "ImageVersionsClient",
    "ImageVersionsAsyncClient",
    "CheckUpgradeResponse",
    "CreateEnvironmentRequest",
    "DatabaseConfig",
    "DeleteEnvironmentRequest",
    "EncryptionConfig",
    "Environment",
    "EnvironmentConfig",
    "GetEnvironmentRequest",
    "IPAllocationPolicy",
    "ListEnvironmentsRequest",
    "ListEnvironmentsResponse",
    "LoadSnapshotRequest",
    "LoadSnapshotResponse",
    "MaintenanceWindow",
    "MasterAuthorizedNetworksConfig",
    "NetworkingConfig",
    "NodeConfig",
    "PrivateClusterConfig",
    "PrivateEnvironmentConfig",
    "RecoveryConfig",
    "SaveSnapshotRequest",
    "SaveSnapshotResponse",
    "ScheduledSnapshotsConfig",
    "SoftwareConfig",
    "UpdateEnvironmentRequest",
    "WebServerConfig",
    "WebServerNetworkAccessControl",
    "WorkloadsConfig",
    "ImageVersion",
    "ListImageVersionsRequest",
    "ListImageVersionsResponse",
    "OperationMetadata",
)
