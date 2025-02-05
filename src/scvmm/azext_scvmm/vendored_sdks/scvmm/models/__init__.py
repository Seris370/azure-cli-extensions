# coding=utf-8
# --------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
# Code generated by Microsoft (R) AutoRest Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is regenerated.
# --------------------------------------------------------------------------

try:
    from ._models_py3 import AvailabilitySet
    from ._models_py3 import AvailabilitySetListItem
    from ._models_py3 import AvailabilitySetListResult
    from ._models_py3 import Checkpoint
    from ._models_py3 import Cloud
    from ._models_py3 import CloudCapacity
    from ._models_py3 import CloudInventoryItem
    from ._models_py3 import CloudListResult
    from ._models_py3 import ErrorAdditionalInfo
    from ._models_py3 import ErrorDefinition
    from ._models_py3 import ErrorDetail
    from ._models_py3 import ErrorResponse
    from ._models_py3 import ExtendedLocation
    from ._models_py3 import GuestAgent
    from ._models_py3 import GuestAgentList
    from ._models_py3 import GuestAgentProfile
    from ._models_py3 import GuestCredential
    from ._models_py3 import HardwareProfile
    from ._models_py3 import HardwareProfileUpdate
    from ._models_py3 import HttpProxyConfiguration
    from ._models_py3 import HybridIdentityMetadata
    from ._models_py3 import HybridIdentityMetadataList
    from ._models_py3 import Identity
    from ._models_py3 import InfrastructureProfile
    from ._models_py3 import InfrastructureProfileUpdate
    from ._models_py3 import InventoryItem
    from ._models_py3 import InventoryItemDetails
    from ._models_py3 import InventoryItemProperties
    from ._models_py3 import InventoryItemsList
    from ._models_py3 import MachineExtension
    from ._models_py3 import MachineExtensionInstanceView
    from ._models_py3 import MachineExtensionInstanceViewStatus
    from ._models_py3 import MachineExtensionPropertiesInstanceView
    from ._models_py3 import MachineExtensionUpdate
    from ._models_py3 import MachineExtensionsListResult
    from ._models_py3 import NetworkInterfaces
    from ._models_py3 import NetworkInterfacesUpdate
    from ._models_py3 import NetworkProfile
    from ._models_py3 import NetworkProfileUpdate
    from ._models_py3 import OsProfile
    from ._models_py3 import OsProfileForVMInstance
    from ._models_py3 import ProxyResource
    from ._models_py3 import Resource
    from ._models_py3 import ResourcePatch
    from ._models_py3 import ResourceProviderOperation
    from ._models_py3 import ResourceProviderOperationDisplay
    from ._models_py3 import ResourceProviderOperationList
    from ._models_py3 import StopVirtualMachineOptions
    from ._models_py3 import StorageProfile
    from ._models_py3 import StorageProfileUpdate
    from ._models_py3 import StorageQoSPolicy
    from ._models_py3 import StorageQoSPolicyDetails
    from ._models_py3 import SystemData
    from ._models_py3 import TrackedResource
    from ._models_py3 import VMMServer
    from ._models_py3 import VMMServerListResult
    from ._models_py3 import VMMServerPropertiesCredentials
    from ._models_py3 import VirtualDisk
    from ._models_py3 import VirtualDiskUpdate
    from ._models_py3 import VirtualMachine
    from ._models_py3 import VirtualMachineCreateCheckpoint
    from ._models_py3 import VirtualMachineDeleteCheckpoint
    from ._models_py3 import VirtualMachineInstance
    from ._models_py3 import VirtualMachineInstanceListResult
    from ._models_py3 import VirtualMachineInstanceUpdate
    from ._models_py3 import VirtualMachineInventoryItem
    from ._models_py3 import VirtualMachineListResult
    from ._models_py3 import VirtualMachineRestoreCheckpoint
    from ._models_py3 import VirtualMachineTemplate
    from ._models_py3 import VirtualMachineTemplateInventoryItem
    from ._models_py3 import VirtualMachineTemplateListResult
    from ._models_py3 import VirtualMachineUpdate
    from ._models_py3 import VirtualMachineUpdateProperties
    from ._models_py3 import VirtualNetwork
    from ._models_py3 import VirtualNetworkInventoryItem
    from ._models_py3 import VirtualNetworkListResult
    from ._models_py3 import VmInstanceHybridIdentityMetadata
    from ._models_py3 import VmInstanceHybridIdentityMetadataList
except (SyntaxError, ImportError):
    from ._models import AvailabilitySet  # type: ignore
    from ._models import AvailabilitySetListItem  # type: ignore
    from ._models import AvailabilitySetListResult  # type: ignore
    from ._models import Checkpoint  # type: ignore
    from ._models import Cloud  # type: ignore
    from ._models import CloudCapacity  # type: ignore
    from ._models import CloudInventoryItem  # type: ignore
    from ._models import CloudListResult  # type: ignore
    from ._models import ErrorAdditionalInfo  # type: ignore
    from ._models import ErrorDefinition  # type: ignore
    from ._models import ErrorDetail  # type: ignore
    from ._models import ErrorResponse  # type: ignore
    from ._models import ExtendedLocation  # type: ignore
    from ._models import GuestAgent  # type: ignore
    from ._models import GuestAgentList  # type: ignore
    from ._models import GuestAgentProfile  # type: ignore
    from ._models import GuestCredential  # type: ignore
    from ._models import HardwareProfile  # type: ignore
    from ._models import HardwareProfileUpdate  # type: ignore
    from ._models import HttpProxyConfiguration  # type: ignore
    from ._models import HybridIdentityMetadata  # type: ignore
    from ._models import HybridIdentityMetadataList  # type: ignore
    from ._models import Identity  # type: ignore
    from ._models import InfrastructureProfile  # type: ignore
    from ._models import InfrastructureProfileUpdate  # type: ignore
    from ._models import InventoryItem  # type: ignore
    from ._models import InventoryItemDetails  # type: ignore
    from ._models import InventoryItemProperties  # type: ignore
    from ._models import InventoryItemsList  # type: ignore
    from ._models import MachineExtension  # type: ignore
    from ._models import MachineExtensionInstanceView  # type: ignore
    from ._models import MachineExtensionInstanceViewStatus  # type: ignore
    from ._models import MachineExtensionPropertiesInstanceView  # type: ignore
    from ._models import MachineExtensionUpdate  # type: ignore
    from ._models import MachineExtensionsListResult  # type: ignore
    from ._models import NetworkInterfaces  # type: ignore
    from ._models import NetworkInterfacesUpdate  # type: ignore
    from ._models import NetworkProfile  # type: ignore
    from ._models import NetworkProfileUpdate  # type: ignore
    from ._models import OsProfile  # type: ignore
    from ._models import OsProfileForVMInstance  # type: ignore
    from ._models import ProxyResource  # type: ignore
    from ._models import Resource  # type: ignore
    from ._models import ResourcePatch  # type: ignore
    from ._models import ResourceProviderOperation  # type: ignore
    from ._models import ResourceProviderOperationDisplay  # type: ignore
    from ._models import ResourceProviderOperationList  # type: ignore
    from ._models import StopVirtualMachineOptions  # type: ignore
    from ._models import StorageProfile  # type: ignore
    from ._models import StorageProfileUpdate  # type: ignore
    from ._models import StorageQoSPolicy  # type: ignore
    from ._models import StorageQoSPolicyDetails  # type: ignore
    from ._models import SystemData  # type: ignore
    from ._models import TrackedResource  # type: ignore
    from ._models import VMMServer  # type: ignore
    from ._models import VMMServerListResult  # type: ignore
    from ._models import VMMServerPropertiesCredentials  # type: ignore
    from ._models import VirtualDisk  # type: ignore
    from ._models import VirtualDiskUpdate  # type: ignore
    from ._models import VirtualMachine  # type: ignore
    from ._models import VirtualMachineCreateCheckpoint  # type: ignore
    from ._models import VirtualMachineDeleteCheckpoint  # type: ignore
    from ._models import VirtualMachineInstance  # type: ignore
    from ._models import VirtualMachineInstanceListResult  # type: ignore
    from ._models import VirtualMachineInstanceUpdate  # type: ignore
    from ._models import VirtualMachineInventoryItem  # type: ignore
    from ._models import VirtualMachineListResult  # type: ignore
    from ._models import VirtualMachineRestoreCheckpoint  # type: ignore
    from ._models import VirtualMachineTemplate  # type: ignore
    from ._models import VirtualMachineTemplateInventoryItem  # type: ignore
    from ._models import VirtualMachineTemplateListResult  # type: ignore
    from ._models import VirtualMachineUpdate  # type: ignore
    from ._models import VirtualMachineUpdateProperties  # type: ignore
    from ._models import VirtualNetwork  # type: ignore
    from ._models import VirtualNetworkInventoryItem  # type: ignore
    from ._models import VirtualNetworkListResult  # type: ignore
    from ._models import VmInstanceHybridIdentityMetadata  # type: ignore
    from ._models import VmInstanceHybridIdentityMetadataList  # type: ignore

from ._scvmm_enums import (
    AllocationMethod,
    CreateDiffDisk,
    CreatedByType,
    DynamicMemoryEnabled,
    IdentityType,
    InventoryType,
    IsCustomizable,
    LimitCpuForMigration,
    OsType,
    ProvisioningAction,
    StatusLevelTypes,
    StatusTypes,
)

__all__ = [
    'AvailabilitySet',
    'AvailabilitySetListItem',
    'AvailabilitySetListResult',
    'Checkpoint',
    'Cloud',
    'CloudCapacity',
    'CloudInventoryItem',
    'CloudListResult',
    'ErrorAdditionalInfo',
    'ErrorDefinition',
    'ErrorDetail',
    'ErrorResponse',
    'ExtendedLocation',
    'GuestAgent',
    'GuestAgentList',
    'GuestAgentProfile',
    'GuestCredential',
    'HardwareProfile',
    'HardwareProfileUpdate',
    'HttpProxyConfiguration',
    'HybridIdentityMetadata',
    'HybridIdentityMetadataList',
    'Identity',
    'InfrastructureProfile',
    'InfrastructureProfileUpdate',
    'InventoryItem',
    'InventoryItemDetails',
    'InventoryItemProperties',
    'InventoryItemsList',
    'MachineExtension',
    'MachineExtensionInstanceView',
    'MachineExtensionInstanceViewStatus',
    'MachineExtensionPropertiesInstanceView',
    'MachineExtensionUpdate',
    'MachineExtensionsListResult',
    'NetworkInterfaces',
    'NetworkInterfacesUpdate',
    'NetworkProfile',
    'NetworkProfileUpdate',
    'OsProfile',
    'OsProfileForVMInstance',
    'ProxyResource',
    'Resource',
    'ResourcePatch',
    'ResourceProviderOperation',
    'ResourceProviderOperationDisplay',
    'ResourceProviderOperationList',
    'StopVirtualMachineOptions',
    'StorageProfile',
    'StorageProfileUpdate',
    'StorageQoSPolicy',
    'StorageQoSPolicyDetails',
    'SystemData',
    'TrackedResource',
    'VMMServer',
    'VMMServerListResult',
    'VMMServerPropertiesCredentials',
    'VirtualDisk',
    'VirtualDiskUpdate',
    'VirtualMachine',
    'VirtualMachineCreateCheckpoint',
    'VirtualMachineDeleteCheckpoint',
    'VirtualMachineInstance',
    'VirtualMachineInstanceListResult',
    'VirtualMachineInstanceUpdate',
    'VirtualMachineInventoryItem',
    'VirtualMachineListResult',
    'VirtualMachineRestoreCheckpoint',
    'VirtualMachineTemplate',
    'VirtualMachineTemplateInventoryItem',
    'VirtualMachineTemplateListResult',
    'VirtualMachineUpdate',
    'VirtualMachineUpdateProperties',
    'VirtualNetwork',
    'VirtualNetworkInventoryItem',
    'VirtualNetworkListResult',
    'VmInstanceHybridIdentityMetadata',
    'VmInstanceHybridIdentityMetadataList',
    'AllocationMethod',
    'CreateDiffDisk',
    'CreatedByType',
    'DynamicMemoryEnabled',
    'IdentityType',
    'InventoryType',
    'IsCustomizable',
    'LimitCpuForMigration',
    'OsType',
    'ProvisioningAction',
    'StatusLevelTypes',
    'StatusTypes',
]
