from viam.components.sensor import Sensor
from viam.resource.registry import Registry, ResourceCreatorRegistration

from .lv_maxsonar_ez import LVMAXSONAREZ

Registry.register_resource_creator(
    Sensor.SUBTYPE,
    LVMAXSONAREZ.MODEL,
    ResourceCreatorRegistration(LVMAXSONAREZ.new, LVMAXSONAREZ.validate),
)
