# Licensed to the Apache Software Foundation (ASF) under one
# or more contributor license agreements.  See the NOTICE file
# distributed with this work for additional information
# regarding copyright ownership.  The ASF licenses this file
# to you under the Apache License, Version 2.0 (the
# "License"); you may not use this file except in compliance
# with the License.  You may obtain a copy of the License at
#
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
#
# Unless required by applicable law or agreed to in writing,
# software distributed under the License is distributed on an
# "AS IS" BASIS, WITHOUT WARRANTIES OR CONDITIONS OF ANY
# KIND, either express or implied.  See the License for the
# specific language governing permissions and limitations
# under the License.

from aliyunsdkcore.request import RpcRequest
from aliyunsdksmartag.endpoint import endpoint_data

class ModifyQosPolicyRequest(RpcRequest):

	def __init__(self):
		RpcRequest.__init__(self, 'Smartag', '2018-03-13', 'ModifyQosPolicy','smartag')
		self.set_method('POST')
		if hasattr(self, "endpoint_map"):
			setattr(self, "endpoint_map", endpoint_data.getEndpointMap())
		if hasattr(self, "endpoint_regional"):
			setattr(self, "endpoint_regional", endpoint_data.getEndpointRegional())


	def get_ResourceOwnerId(self):
		return self.get_query_params().get('ResourceOwnerId')

	def set_ResourceOwnerId(self,ResourceOwnerId):
		self.add_query_param('ResourceOwnerId',ResourceOwnerId)

	def get_SourcePortRange(self):
		return self.get_query_params().get('SourcePortRange')

	def set_SourcePortRange(self,SourcePortRange):
		self.add_query_param('SourcePortRange',SourcePortRange)

	def get_QosPolicyId(self):
		return self.get_query_params().get('QosPolicyId')

	def set_QosPolicyId(self,QosPolicyId):
		self.add_query_param('QosPolicyId',QosPolicyId)

	def get_SourceCidr(self):
		return self.get_query_params().get('SourceCidr')

	def set_SourceCidr(self,SourceCidr):
		self.add_query_param('SourceCidr',SourceCidr)

	def get_Description(self):
		return self.get_query_params().get('Description')

	def set_Description(self,Description):
		self.add_query_param('Description',Description)

	def get_StartTime(self):
		return self.get_query_params().get('StartTime')

	def set_StartTime(self,StartTime):
		self.add_query_param('StartTime',StartTime)

	def get_DestCidr(self):
		return self.get_query_params().get('DestCidr')

	def set_DestCidr(self,DestCidr):
		self.add_query_param('DestCidr',DestCidr)

	def get_QosId(self):
		return self.get_query_params().get('QosId')

	def set_QosId(self,QosId):
		self.add_query_param('QosId',QosId)

	def get_ResourceOwnerAccount(self):
		return self.get_query_params().get('ResourceOwnerAccount')

	def set_ResourceOwnerAccount(self,ResourceOwnerAccount):
		self.add_query_param('ResourceOwnerAccount',ResourceOwnerAccount)

	def get_IpProtocol(self):
		return self.get_query_params().get('IpProtocol')

	def set_IpProtocol(self,IpProtocol):
		self.add_query_param('IpProtocol',IpProtocol)

	def get_OwnerAccount(self):
		return self.get_query_params().get('OwnerAccount')

	def set_OwnerAccount(self,OwnerAccount):
		self.add_query_param('OwnerAccount',OwnerAccount)

	def get_EndTime(self):
		return self.get_query_params().get('EndTime')

	def set_EndTime(self,EndTime):
		self.add_query_param('EndTime',EndTime)

	def get_OwnerId(self):
		return self.get_query_params().get('OwnerId')

	def set_OwnerId(self,OwnerId):
		self.add_query_param('OwnerId',OwnerId)

	def get_Priority(self):
		return self.get_query_params().get('Priority')

	def set_Priority(self,Priority):
		self.add_query_param('Priority',Priority)

	def get_DestPortRange(self):
		return self.get_query_params().get('DestPortRange')

	def set_DestPortRange(self,DestPortRange):
		self.add_query_param('DestPortRange',DestPortRange)

	def get_Name(self):
		return self.get_query_params().get('Name')

	def set_Name(self,Name):
		self.add_query_param('Name',Name)