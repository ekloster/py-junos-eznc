# for debugging ...
import pdb
from pprint import pprint as pp 
from lxml import etree

# for the example ...
from exampleutils import *
from jnpr.eznc import Netconf as Junos
from jnpr.eznc.resources.srx.nat import NatSrcPool
from jnpr.eznc.utils import ConfigUtils

login = dict(user='jeremy', host='vsrx_cyan', password='jeremy1')

jdev = Junos(**login)
jdev.open()

jdev.ez(cu=ConfigUtils)
mgr = NatSrcPool(jdev)

def make_some_pools():
  make_pools = dict(
    this_pool =  dict(addr_from="1.1.1.1", addr_to="1.1.1.10"),
    that_pool =  dict(addr_from='2.2.2.2', addr_to="2.2.2.10"),
    goober_pool =  dict(addr_from="3.3.3.3", addr_to="3.3.3.10")
  )

  for pool_name, pool_vars in make_pools.items():
    r = mgr[pool_name]
    r(**pool_vars)
    r.write()

