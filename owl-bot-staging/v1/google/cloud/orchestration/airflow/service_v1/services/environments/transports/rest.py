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

from google.auth.transport.requests import AuthorizedSession  # type: ignore
import json  # type: ignore
import grpc  # type: ignore
from google.auth.transport.grpc import SslCredentials  # type: ignore
from google.auth import credentials as ga_credentials  # type: ignore
from google.api_core import exceptions as core_exceptions
from google.api_core import retry as retries
from google.api_core import rest_helpers
from google.api_core import rest_streaming
from google.api_core import path_template
from google.api_core import gapic_v1

from google.protobuf import json_format
from google.api_core import operations_v1
from requests import __version__ as requests_version
import dataclasses
import re
from typing import Callable, Dict, List, Optional, Sequence, Tuple, Union
import warnings

try:
    OptionalRetry = Union[retries.Retry, gapic_v1.method._MethodDefault]
except AttributeError:  # pragma: NO COVER
    OptionalRetry = Union[retries.Retry, object]  # type: ignore


from google.cloud.orchestration.airflow.service_v1.types import environments
from google.longrunning import operations_pb2  # type: ignore

from .base import EnvironmentsTransport, DEFAULT_CLIENT_INFO as BASE_DEFAULT_CLIENT_INFO


DEFAULT_CLIENT_INFO = gapic_v1.client_info.ClientInfo(
    gapic_version=BASE_DEFAULT_CLIENT_INFO.gapic_version,
    grpc_version=None,
    rest_version=requests_version,
)


class EnvironmentsRestInterceptor:
    """Interceptor for Environments.

    Interceptors are used to manipulate requests, request metadata, and responses
    in arbitrary ways.
    Example use cases include:
    * Logging
    * Verifying requests according to service or custom semantics
    * Stripping extraneous information from responses

    These use cases and more can be enabled by injecting an
    instance of a custom subclass when constructing the EnvironmentsRestTransport.

    .. code-block:: python
        class MyCustomEnvironmentsInterceptor(EnvironmentsRestInterceptor):
            def pre_create_environment(self, request, metadata):
                logging.log(f"Received request: {request}")
                return request, metadata

            def post_create_environment(self, response):
                logging.log(f"Received response: {response}")
                return response

            def pre_delete_environment(self, request, metadata):
                logging.log(f"Received request: {request}")
                return request, metadata

            def post_delete_environment(self, response):
                logging.log(f"Received response: {response}")
                return response

            def pre_get_environment(self, request, metadata):
                logging.log(f"Received request: {request}")
                return request, metadata

            def post_get_environment(self, response):
                logging.log(f"Received response: {response}")
                return response

            def pre_list_environments(self, request, metadata):
                logging.log(f"Received request: {request}")
                return request, metadata

            def post_list_environments(self, response):
                logging.log(f"Received response: {response}")
                return response

            def pre_load_snapshot(self, request, metadata):
                logging.log(f"Received request: {request}")
                return request, metadata

            def post_load_snapshot(self, response):
                logging.log(f"Received response: {response}")
                return response

            def pre_save_snapshot(self, request, metadata):
                logging.log(f"Received request: {request}")
                return request, metadata

            def post_save_snapshot(self, response):
                logging.log(f"Received response: {response}")
                return response

            def pre_update_environment(self, request, metadata):
                logging.log(f"Received request: {request}")
                return request, metadata

            def post_update_environment(self, response):
                logging.log(f"Received response: {response}")
                return response

        transport = EnvironmentsRestTransport(interceptor=MyCustomEnvironmentsInterceptor())
        client = EnvironmentsClient(transport=transport)


    """
    def pre_create_environment(self, request: environments.CreateEnvironmentRequest, metadata: Sequence[Tuple[str, str]]) -> Tuple[environments.CreateEnvironmentRequest, Sequence[Tuple[str, str]]]:
        """Pre-rpc interceptor for create_environment

        Override in a subclass to manipulate the request or metadata
        before they are sent to the Environments server.
        """
        return request, metadata

    def post_create_environment(self, response: operations_pb2.Operation) -> operations_pb2.Operation:
        """Post-rpc interceptor for create_environment

        Override in a subclass to manipulate the response
        after it is returned by the Environments server but before
        it is returned to user code.
        """
        return response
    def pre_delete_environment(self, request: environments.DeleteEnvironmentRequest, metadata: Sequence[Tuple[str, str]]) -> Tuple[environments.DeleteEnvironmentRequest, Sequence[Tuple[str, str]]]:
        """Pre-rpc interceptor for delete_environment

        Override in a subclass to manipulate the request or metadata
        before they are sent to the Environments server.
        """
        return request, metadata

    def post_delete_environment(self, response: operations_pb2.Operation) -> operations_pb2.Operation:
        """Post-rpc interceptor for delete_environment

        Override in a subclass to manipulate the response
        after it is returned by the Environments server but before
        it is returned to user code.
        """
        return response
    def pre_get_environment(self, request: environments.GetEnvironmentRequest, metadata: Sequence[Tuple[str, str]]) -> Tuple[environments.GetEnvironmentRequest, Sequence[Tuple[str, str]]]:
        """Pre-rpc interceptor for get_environment

        Override in a subclass to manipulate the request or metadata
        before they are sent to the Environments server.
        """
        return request, metadata

    def post_get_environment(self, response: environments.Environment) -> environments.Environment:
        """Post-rpc interceptor for get_environment

        Override in a subclass to manipulate the response
        after it is returned by the Environments server but before
        it is returned to user code.
        """
        return response
    def pre_list_environments(self, request: environments.ListEnvironmentsRequest, metadata: Sequence[Tuple[str, str]]) -> Tuple[environments.ListEnvironmentsRequest, Sequence[Tuple[str, str]]]:
        """Pre-rpc interceptor for list_environments

        Override in a subclass to manipulate the request or metadata
        before they are sent to the Environments server.
        """
        return request, metadata

    def post_list_environments(self, response: environments.ListEnvironmentsResponse) -> environments.ListEnvironmentsResponse:
        """Post-rpc interceptor for list_environments

        Override in a subclass to manipulate the response
        after it is returned by the Environments server but before
        it is returned to user code.
        """
        return response
    def pre_load_snapshot(self, request: environments.LoadSnapshotRequest, metadata: Sequence[Tuple[str, str]]) -> Tuple[environments.LoadSnapshotRequest, Sequence[Tuple[str, str]]]:
        """Pre-rpc interceptor for load_snapshot

        Override in a subclass to manipulate the request or metadata
        before they are sent to the Environments server.
        """
        return request, metadata

    def post_load_snapshot(self, response: operations_pb2.Operation) -> operations_pb2.Operation:
        """Post-rpc interceptor for load_snapshot

        Override in a subclass to manipulate the response
        after it is returned by the Environments server but before
        it is returned to user code.
        """
        return response
    def pre_save_snapshot(self, request: environments.SaveSnapshotRequest, metadata: Sequence[Tuple[str, str]]) -> Tuple[environments.SaveSnapshotRequest, Sequence[Tuple[str, str]]]:
        """Pre-rpc interceptor for save_snapshot

        Override in a subclass to manipulate the request or metadata
        before they are sent to the Environments server.
        """
        return request, metadata

    def post_save_snapshot(self, response: operations_pb2.Operation) -> operations_pb2.Operation:
        """Post-rpc interceptor for save_snapshot

        Override in a subclass to manipulate the response
        after it is returned by the Environments server but before
        it is returned to user code.
        """
        return response
    def pre_update_environment(self, request: environments.UpdateEnvironmentRequest, metadata: Sequence[Tuple[str, str]]) -> Tuple[environments.UpdateEnvironmentRequest, Sequence[Tuple[str, str]]]:
        """Pre-rpc interceptor for update_environment

        Override in a subclass to manipulate the request or metadata
        before they are sent to the Environments server.
        """
        return request, metadata

    def post_update_environment(self, response: operations_pb2.Operation) -> operations_pb2.Operation:
        """Post-rpc interceptor for update_environment

        Override in a subclass to manipulate the response
        after it is returned by the Environments server but before
        it is returned to user code.
        """
        return response


@dataclasses.dataclass
class EnvironmentsRestStub:
    _session: AuthorizedSession
    _host: str
    _interceptor: EnvironmentsRestInterceptor


class EnvironmentsRestTransport(EnvironmentsTransport):
    """REST backend transport for Environments.

    Managed Apache Airflow Environments.

    This class defines the same methods as the primary client, so the
    primary client can load the underlying transport implementation
    and call it.

    It sends JSON representations of protocol buffers over HTTP/1.1

    """

    def __init__(self, *,
            host: str = 'composer.googleapis.com',
            credentials: Optional[ga_credentials.Credentials] = None,
            credentials_file: Optional[str] = None,
            scopes: Optional[Sequence[str]] = None,
            client_cert_source_for_mtls: Optional[Callable[[
                ], Tuple[bytes, bytes]]] = None,
            quota_project_id: Optional[str] = None,
            client_info: gapic_v1.client_info.ClientInfo = DEFAULT_CLIENT_INFO,
            always_use_jwt_access: Optional[bool] = False,
            url_scheme: str = 'https',
            interceptor: Optional[EnvironmentsRestInterceptor] = None,
            api_audience: Optional[str] = None,
            ) -> None:
        """Instantiate the transport.

        Args:
            host (Optional[str]):
                 The hostname to connect to.
            credentials (Optional[google.auth.credentials.Credentials]): The
                authorization credentials to attach to requests. These
                credentials identify the application to the service; if none
                are specified, the client will attempt to ascertain the
                credentials from the environment.

            credentials_file (Optional[str]): A file with credentials that can
                be loaded with :func:`google.auth.load_credentials_from_file`.
                This argument is ignored if ``channel`` is provided.
            scopes (Optional(Sequence[str])): A list of scopes. This argument is
                ignored if ``channel`` is provided.
            client_cert_source_for_mtls (Callable[[], Tuple[bytes, bytes]]): Client
                certificate to configure mutual TLS HTTP channel. It is ignored
                if ``channel`` is provided.
            quota_project_id (Optional[str]): An optional project to use for billing
                and quota.
            client_info (google.api_core.gapic_v1.client_info.ClientInfo):
                The client info used to send a user-agent string along with
                API requests. If ``None``, then default info will be used.
                Generally, you only need to set this if you are developing
                your own client library.
            always_use_jwt_access (Optional[bool]): Whether self signed JWT should
                be used for service account credentials.
            url_scheme: the protocol scheme for the API endpoint.  Normally
                "https", but for testing or local servers,
                "http" can be specified.
        """
        # Run the base constructor
        # TODO(yon-mg): resolve other ctor params i.e. scopes, quota, etc.
        # TODO: When custom host (api_endpoint) is set, `scopes` must *also* be set on the
        # credentials object
        maybe_url_match = re.match("^(?P<scheme>http(?:s)?://)?(?P<host>.*)$", host)
        if maybe_url_match is None:
            raise ValueError(f"Unexpected hostname structure: {host}")  # pragma: NO COVER

        url_match_items = maybe_url_match.groupdict()

        host = f"{url_scheme}://{host}" if not url_match_items["scheme"] else host

        super().__init__(
            host=host,
            credentials=credentials,
            client_info=client_info,
            always_use_jwt_access=always_use_jwt_access,
            api_audience=api_audience
        )
        self._session = AuthorizedSession(
            self._credentials, default_host=self.DEFAULT_HOST)
        self._operations_client: Optional[operations_v1.AbstractOperationsClient] = None
        if client_cert_source_for_mtls:
            self._session.configure_mtls_channel(client_cert_source_for_mtls)
        self._interceptor = interceptor or EnvironmentsRestInterceptor()
        self._prep_wrapped_messages(client_info)

    @property
    def operations_client(self) -> operations_v1.AbstractOperationsClient:
        """Create the client designed to process long-running operations.

        This property caches on the instance; repeated calls return the same
        client.
        """
        # Only create a new client if we do not already have one.
        if self._operations_client is None:
            http_options: Dict[str, List[Dict[str, str]]] = {
            }

            rest_transport = operations_v1.OperationsRestTransport(
                    host=self._host,
                    # use the credentials which are saved
                    credentials=self._credentials,
                    scopes=self._scopes,
                    http_options=http_options,
                    path_prefix="v1")

            self._operations_client = operations_v1.AbstractOperationsClient(transport=rest_transport)

        # Return the client from cache.
        return self._operations_client

    class _CreateEnvironment(EnvironmentsRestStub):
        def __hash__(self):
            return hash("CreateEnvironment")

        def __call__(self,
                request: environments.CreateEnvironmentRequest, *,
                retry: OptionalRetry=gapic_v1.method.DEFAULT,
                timeout: Optional[float]=None,
                metadata: Sequence[Tuple[str, str]]=(),
                ) -> operations_pb2.Operation:
            r"""Call the create environment method over HTTP.

            Args:
                request (~.environments.CreateEnvironmentRequest):
                    The request object. Create a new environment.
                retry (google.api_core.retry.Retry): Designation of what errors, if any,
                    should be retried.
                timeout (float): The timeout for this request.
                metadata (Sequence[Tuple[str, str]]): Strings which should be
                    sent along with the request as metadata.

            Returns:
                ~.operations_pb2.Operation:
                    This resource represents a
                long-running operation that is the
                result of a network API call.

            """

            http_options: List[Dict[str, str]] = [{
                'method': 'post',
                'uri': '/v1/{parent=projects/*/locations/*}/environments',
                'body': 'environment',
            },
            ]
            request, metadata = self._interceptor.pre_create_environment(request, metadata)
            pb_request = environments.CreateEnvironmentRequest.pb(request)
            transcoded_request = path_template.transcode(http_options, pb_request)

            # Jsonify the request body

            body = json_format.MessageToJson(
                transcoded_request['body'],
                including_default_value_fields=False,
                use_integers_for_enums=True
            )
            uri = transcoded_request['uri']
            method = transcoded_request['method']

            # Jsonify the query params
            query_params = json.loads(json_format.MessageToJson(
                transcoded_request['query_params'],
                including_default_value_fields=False,
                use_integers_for_enums=True,
            ))

            query_params["$alt"] = "json;enum-encoding=int"

            # Send the request
            headers = dict(metadata)
            headers['Content-Type'] = 'application/json'
            response = getattr(self._session, method)(
                "{host}{uri}".format(host=self._host, uri=uri),
                timeout=timeout,
                headers=headers,
                params=rest_helpers.flatten_query_params(query_params, strict=True),
                data=body,
                )

            # In case of error, raise the appropriate core_exceptions.GoogleAPICallError exception
            # subclass.
            if response.status_code >= 400:
                raise core_exceptions.from_http_response(response)

            # Return the response
            resp = operations_pb2.Operation()
            json_format.Parse(response.content, resp, ignore_unknown_fields=True)
            resp = self._interceptor.post_create_environment(resp)
            return resp

    class _DeleteEnvironment(EnvironmentsRestStub):
        def __hash__(self):
            return hash("DeleteEnvironment")

        def __call__(self,
                request: environments.DeleteEnvironmentRequest, *,
                retry: OptionalRetry=gapic_v1.method.DEFAULT,
                timeout: Optional[float]=None,
                metadata: Sequence[Tuple[str, str]]=(),
                ) -> operations_pb2.Operation:
            r"""Call the delete environment method over HTTP.

            Args:
                request (~.environments.DeleteEnvironmentRequest):
                    The request object. Delete an environment.
                retry (google.api_core.retry.Retry): Designation of what errors, if any,
                    should be retried.
                timeout (float): The timeout for this request.
                metadata (Sequence[Tuple[str, str]]): Strings which should be
                    sent along with the request as metadata.

            Returns:
                ~.operations_pb2.Operation:
                    This resource represents a
                long-running operation that is the
                result of a network API call.

            """

            http_options: List[Dict[str, str]] = [{
                'method': 'delete',
                'uri': '/v1/{name=projects/*/locations/*/environments/*}',
            },
            ]
            request, metadata = self._interceptor.pre_delete_environment(request, metadata)
            pb_request = environments.DeleteEnvironmentRequest.pb(request)
            transcoded_request = path_template.transcode(http_options, pb_request)

            uri = transcoded_request['uri']
            method = transcoded_request['method']

            # Jsonify the query params
            query_params = json.loads(json_format.MessageToJson(
                transcoded_request['query_params'],
                including_default_value_fields=False,
                use_integers_for_enums=True,
            ))

            query_params["$alt"] = "json;enum-encoding=int"

            # Send the request
            headers = dict(metadata)
            headers['Content-Type'] = 'application/json'
            response = getattr(self._session, method)(
                "{host}{uri}".format(host=self._host, uri=uri),
                timeout=timeout,
                headers=headers,
                params=rest_helpers.flatten_query_params(query_params, strict=True),
                )

            # In case of error, raise the appropriate core_exceptions.GoogleAPICallError exception
            # subclass.
            if response.status_code >= 400:
                raise core_exceptions.from_http_response(response)

            # Return the response
            resp = operations_pb2.Operation()
            json_format.Parse(response.content, resp, ignore_unknown_fields=True)
            resp = self._interceptor.post_delete_environment(resp)
            return resp

    class _GetEnvironment(EnvironmentsRestStub):
        def __hash__(self):
            return hash("GetEnvironment")

        def __call__(self,
                request: environments.GetEnvironmentRequest, *,
                retry: OptionalRetry=gapic_v1.method.DEFAULT,
                timeout: Optional[float]=None,
                metadata: Sequence[Tuple[str, str]]=(),
                ) -> environments.Environment:
            r"""Call the get environment method over HTTP.

            Args:
                request (~.environments.GetEnvironmentRequest):
                    The request object. Get an environment.
                retry (google.api_core.retry.Retry): Designation of what errors, if any,
                    should be retried.
                timeout (float): The timeout for this request.
                metadata (Sequence[Tuple[str, str]]): Strings which should be
                    sent along with the request as metadata.

            Returns:
                ~.environments.Environment:
                    An environment for running
                orchestration tasks.

            """

            http_options: List[Dict[str, str]] = [{
                'method': 'get',
                'uri': '/v1/{name=projects/*/locations/*/environments/*}',
            },
            ]
            request, metadata = self._interceptor.pre_get_environment(request, metadata)
            pb_request = environments.GetEnvironmentRequest.pb(request)
            transcoded_request = path_template.transcode(http_options, pb_request)

            uri = transcoded_request['uri']
            method = transcoded_request['method']

            # Jsonify the query params
            query_params = json.loads(json_format.MessageToJson(
                transcoded_request['query_params'],
                including_default_value_fields=False,
                use_integers_for_enums=True,
            ))

            query_params["$alt"] = "json;enum-encoding=int"

            # Send the request
            headers = dict(metadata)
            headers['Content-Type'] = 'application/json'
            response = getattr(self._session, method)(
                "{host}{uri}".format(host=self._host, uri=uri),
                timeout=timeout,
                headers=headers,
                params=rest_helpers.flatten_query_params(query_params, strict=True),
                )

            # In case of error, raise the appropriate core_exceptions.GoogleAPICallError exception
            # subclass.
            if response.status_code >= 400:
                raise core_exceptions.from_http_response(response)

            # Return the response
            resp = environments.Environment()
            pb_resp = environments.Environment.pb(resp)

            json_format.Parse(response.content, pb_resp, ignore_unknown_fields=True)
            resp = self._interceptor.post_get_environment(resp)
            return resp

    class _ListEnvironments(EnvironmentsRestStub):
        def __hash__(self):
            return hash("ListEnvironments")

        def __call__(self,
                request: environments.ListEnvironmentsRequest, *,
                retry: OptionalRetry=gapic_v1.method.DEFAULT,
                timeout: Optional[float]=None,
                metadata: Sequence[Tuple[str, str]]=(),
                ) -> environments.ListEnvironmentsResponse:
            r"""Call the list environments method over HTTP.

            Args:
                request (~.environments.ListEnvironmentsRequest):
                    The request object. List environments in a project and
                location.

                retry (google.api_core.retry.Retry): Designation of what errors, if any,
                    should be retried.
                timeout (float): The timeout for this request.
                metadata (Sequence[Tuple[str, str]]): Strings which should be
                    sent along with the request as metadata.

            Returns:
                ~.environments.ListEnvironmentsResponse:
                    The environments in a project and
                location.

            """

            http_options: List[Dict[str, str]] = [{
                'method': 'get',
                'uri': '/v1/{parent=projects/*/locations/*}/environments',
            },
            ]
            request, metadata = self._interceptor.pre_list_environments(request, metadata)
            pb_request = environments.ListEnvironmentsRequest.pb(request)
            transcoded_request = path_template.transcode(http_options, pb_request)

            uri = transcoded_request['uri']
            method = transcoded_request['method']

            # Jsonify the query params
            query_params = json.loads(json_format.MessageToJson(
                transcoded_request['query_params'],
                including_default_value_fields=False,
                use_integers_for_enums=True,
            ))

            query_params["$alt"] = "json;enum-encoding=int"

            # Send the request
            headers = dict(metadata)
            headers['Content-Type'] = 'application/json'
            response = getattr(self._session, method)(
                "{host}{uri}".format(host=self._host, uri=uri),
                timeout=timeout,
                headers=headers,
                params=rest_helpers.flatten_query_params(query_params, strict=True),
                )

            # In case of error, raise the appropriate core_exceptions.GoogleAPICallError exception
            # subclass.
            if response.status_code >= 400:
                raise core_exceptions.from_http_response(response)

            # Return the response
            resp = environments.ListEnvironmentsResponse()
            pb_resp = environments.ListEnvironmentsResponse.pb(resp)

            json_format.Parse(response.content, pb_resp, ignore_unknown_fields=True)
            resp = self._interceptor.post_list_environments(resp)
            return resp

    class _LoadSnapshot(EnvironmentsRestStub):
        def __hash__(self):
            return hash("LoadSnapshot")

        def __call__(self,
                request: environments.LoadSnapshotRequest, *,
                retry: OptionalRetry=gapic_v1.method.DEFAULT,
                timeout: Optional[float]=None,
                metadata: Sequence[Tuple[str, str]]=(),
                ) -> operations_pb2.Operation:
            r"""Call the load snapshot method over HTTP.

            Args:
                request (~.environments.LoadSnapshotRequest):
                    The request object. Request to load a snapshot into a
                Cloud Composer environment.

                retry (google.api_core.retry.Retry): Designation of what errors, if any,
                    should be retried.
                timeout (float): The timeout for this request.
                metadata (Sequence[Tuple[str, str]]): Strings which should be
                    sent along with the request as metadata.

            Returns:
                ~.operations_pb2.Operation:
                    This resource represents a
                long-running operation that is the
                result of a network API call.

            """

            http_options: List[Dict[str, str]] = [{
                'method': 'post',
                'uri': '/v1/{environment=projects/*/locations/*/environments/*}:loadSnapshot',
                'body': '*',
            },
            ]
            request, metadata = self._interceptor.pre_load_snapshot(request, metadata)
            pb_request = environments.LoadSnapshotRequest.pb(request)
            transcoded_request = path_template.transcode(http_options, pb_request)

            # Jsonify the request body

            body = json_format.MessageToJson(
                transcoded_request['body'],
                including_default_value_fields=False,
                use_integers_for_enums=True
            )
            uri = transcoded_request['uri']
            method = transcoded_request['method']

            # Jsonify the query params
            query_params = json.loads(json_format.MessageToJson(
                transcoded_request['query_params'],
                including_default_value_fields=False,
                use_integers_for_enums=True,
            ))

            query_params["$alt"] = "json;enum-encoding=int"

            # Send the request
            headers = dict(metadata)
            headers['Content-Type'] = 'application/json'
            response = getattr(self._session, method)(
                "{host}{uri}".format(host=self._host, uri=uri),
                timeout=timeout,
                headers=headers,
                params=rest_helpers.flatten_query_params(query_params, strict=True),
                data=body,
                )

            # In case of error, raise the appropriate core_exceptions.GoogleAPICallError exception
            # subclass.
            if response.status_code >= 400:
                raise core_exceptions.from_http_response(response)

            # Return the response
            resp = operations_pb2.Operation()
            json_format.Parse(response.content, resp, ignore_unknown_fields=True)
            resp = self._interceptor.post_load_snapshot(resp)
            return resp

    class _SaveSnapshot(EnvironmentsRestStub):
        def __hash__(self):
            return hash("SaveSnapshot")

        def __call__(self,
                request: environments.SaveSnapshotRequest, *,
                retry: OptionalRetry=gapic_v1.method.DEFAULT,
                timeout: Optional[float]=None,
                metadata: Sequence[Tuple[str, str]]=(),
                ) -> operations_pb2.Operation:
            r"""Call the save snapshot method over HTTP.

            Args:
                request (~.environments.SaveSnapshotRequest):
                    The request object. Request to create a snapshot of a
                Cloud Composer environment.

                retry (google.api_core.retry.Retry): Designation of what errors, if any,
                    should be retried.
                timeout (float): The timeout for this request.
                metadata (Sequence[Tuple[str, str]]): Strings which should be
                    sent along with the request as metadata.

            Returns:
                ~.operations_pb2.Operation:
                    This resource represents a
                long-running operation that is the
                result of a network API call.

            """

            http_options: List[Dict[str, str]] = [{
                'method': 'post',
                'uri': '/v1/{environment=projects/*/locations/*/environments/*}:saveSnapshot',
                'body': '*',
            },
            ]
            request, metadata = self._interceptor.pre_save_snapshot(request, metadata)
            pb_request = environments.SaveSnapshotRequest.pb(request)
            transcoded_request = path_template.transcode(http_options, pb_request)

            # Jsonify the request body

            body = json_format.MessageToJson(
                transcoded_request['body'],
                including_default_value_fields=False,
                use_integers_for_enums=True
            )
            uri = transcoded_request['uri']
            method = transcoded_request['method']

            # Jsonify the query params
            query_params = json.loads(json_format.MessageToJson(
                transcoded_request['query_params'],
                including_default_value_fields=False,
                use_integers_for_enums=True,
            ))

            query_params["$alt"] = "json;enum-encoding=int"

            # Send the request
            headers = dict(metadata)
            headers['Content-Type'] = 'application/json'
            response = getattr(self._session, method)(
                "{host}{uri}".format(host=self._host, uri=uri),
                timeout=timeout,
                headers=headers,
                params=rest_helpers.flatten_query_params(query_params, strict=True),
                data=body,
                )

            # In case of error, raise the appropriate core_exceptions.GoogleAPICallError exception
            # subclass.
            if response.status_code >= 400:
                raise core_exceptions.from_http_response(response)

            # Return the response
            resp = operations_pb2.Operation()
            json_format.Parse(response.content, resp, ignore_unknown_fields=True)
            resp = self._interceptor.post_save_snapshot(resp)
            return resp

    class _UpdateEnvironment(EnvironmentsRestStub):
        def __hash__(self):
            return hash("UpdateEnvironment")

        def __call__(self,
                request: environments.UpdateEnvironmentRequest, *,
                retry: OptionalRetry=gapic_v1.method.DEFAULT,
                timeout: Optional[float]=None,
                metadata: Sequence[Tuple[str, str]]=(),
                ) -> operations_pb2.Operation:
            r"""Call the update environment method over HTTP.

            Args:
                request (~.environments.UpdateEnvironmentRequest):
                    The request object. Update an environment.
                retry (google.api_core.retry.Retry): Designation of what errors, if any,
                    should be retried.
                timeout (float): The timeout for this request.
                metadata (Sequence[Tuple[str, str]]): Strings which should be
                    sent along with the request as metadata.

            Returns:
                ~.operations_pb2.Operation:
                    This resource represents a
                long-running operation that is the
                result of a network API call.

            """

            http_options: List[Dict[str, str]] = [{
                'method': 'patch',
                'uri': '/v1/{name=projects/*/locations/*/environments/*}',
                'body': 'environment',
            },
            ]
            request, metadata = self._interceptor.pre_update_environment(request, metadata)
            pb_request = environments.UpdateEnvironmentRequest.pb(request)
            transcoded_request = path_template.transcode(http_options, pb_request)

            # Jsonify the request body

            body = json_format.MessageToJson(
                transcoded_request['body'],
                including_default_value_fields=False,
                use_integers_for_enums=True
            )
            uri = transcoded_request['uri']
            method = transcoded_request['method']

            # Jsonify the query params
            query_params = json.loads(json_format.MessageToJson(
                transcoded_request['query_params'],
                including_default_value_fields=False,
                use_integers_for_enums=True,
            ))

            query_params["$alt"] = "json;enum-encoding=int"

            # Send the request
            headers = dict(metadata)
            headers['Content-Type'] = 'application/json'
            response = getattr(self._session, method)(
                "{host}{uri}".format(host=self._host, uri=uri),
                timeout=timeout,
                headers=headers,
                params=rest_helpers.flatten_query_params(query_params, strict=True),
                data=body,
                )

            # In case of error, raise the appropriate core_exceptions.GoogleAPICallError exception
            # subclass.
            if response.status_code >= 400:
                raise core_exceptions.from_http_response(response)

            # Return the response
            resp = operations_pb2.Operation()
            json_format.Parse(response.content, resp, ignore_unknown_fields=True)
            resp = self._interceptor.post_update_environment(resp)
            return resp

    @property
    def create_environment(self) -> Callable[
            [environments.CreateEnvironmentRequest],
            operations_pb2.Operation]:
        # The return type is fine, but mypy isn't sophisticated enough to determine what's going on here.
        # In C++ this would require a dynamic_cast
        return self._CreateEnvironment(self._session, self._host, self._interceptor) # type: ignore

    @property
    def delete_environment(self) -> Callable[
            [environments.DeleteEnvironmentRequest],
            operations_pb2.Operation]:
        # The return type is fine, but mypy isn't sophisticated enough to determine what's going on here.
        # In C++ this would require a dynamic_cast
        return self._DeleteEnvironment(self._session, self._host, self._interceptor) # type: ignore

    @property
    def get_environment(self) -> Callable[
            [environments.GetEnvironmentRequest],
            environments.Environment]:
        # The return type is fine, but mypy isn't sophisticated enough to determine what's going on here.
        # In C++ this would require a dynamic_cast
        return self._GetEnvironment(self._session, self._host, self._interceptor) # type: ignore

    @property
    def list_environments(self) -> Callable[
            [environments.ListEnvironmentsRequest],
            environments.ListEnvironmentsResponse]:
        # The return type is fine, but mypy isn't sophisticated enough to determine what's going on here.
        # In C++ this would require a dynamic_cast
        return self._ListEnvironments(self._session, self._host, self._interceptor) # type: ignore

    @property
    def load_snapshot(self) -> Callable[
            [environments.LoadSnapshotRequest],
            operations_pb2.Operation]:
        # The return type is fine, but mypy isn't sophisticated enough to determine what's going on here.
        # In C++ this would require a dynamic_cast
        return self._LoadSnapshot(self._session, self._host, self._interceptor) # type: ignore

    @property
    def save_snapshot(self) -> Callable[
            [environments.SaveSnapshotRequest],
            operations_pb2.Operation]:
        # The return type is fine, but mypy isn't sophisticated enough to determine what's going on here.
        # In C++ this would require a dynamic_cast
        return self._SaveSnapshot(self._session, self._host, self._interceptor) # type: ignore

    @property
    def update_environment(self) -> Callable[
            [environments.UpdateEnvironmentRequest],
            operations_pb2.Operation]:
        # The return type is fine, but mypy isn't sophisticated enough to determine what's going on here.
        # In C++ this would require a dynamic_cast
        return self._UpdateEnvironment(self._session, self._host, self._interceptor) # type: ignore

    @property
    def kind(self) -> str:
        return "rest"

    def close(self):
        self._session.close()


__all__=(
    'EnvironmentsRestTransport',
)
