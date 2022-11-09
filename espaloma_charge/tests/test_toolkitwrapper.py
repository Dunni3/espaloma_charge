from espaloma_charge.espaloma_wrapper import EspalomaChargeToolkitWrapper
from openff.toolkit import ToolkitRegistry, ForceField, RDKitToolkitWrapper
from openff.units import unit
import pytest
from openff.toolkit.utils.exceptions import ChargeMethodUnavailableError
from openff.toolkit.tests.create_molecules import create_ethanol

def test_ethanol_molecule_api_w_wrapper():
    ectkw = EspalomaChargeToolkitWrapper()
    offmol = create_ethanol()
    offmol.assign_partial_charges('espaloma-am1bcc',
                                  toolkit_registry=ectkw)
    # Ensure its not all 0s
    assert (abs(offmol.partial_charges.value_in_unit(unit.elementary_charge)) > 0.01).any(), offmol.partial_charges

def test_ethanol_molecule_api_w_explicit_registry():
    ectkr = ToolkitRegistry([EspalomaChargeToolkitWrapper])
    offmol = create_ethanol()
    offmol.assign_partial_charges('espaloma-am1bcc',
                                  toolkit_registry=ectkr)
    # Ensure its not all 0s
    assert (abs(offmol.partial_charges.value_in_unit(unit.elementary_charge)) > 0.01).any(), offmol.partial_charges

def test_ethanol_molecule_api_wo_registry():
    offmol = create_ethanol()
    # This should raise a ChargeMethodUnavailableError since the global toolkit registry won't
    # automatically add the espalomawrapper
    with pytest.raises(ChargeMethodUnavailableError):
        offmol.assign_partial_charges('espaloma-am1bcc')


def test_ethanol_direct():
    ectkw = EspalomaChargeToolkitWrapper()
    offmol = create_ethanol()
    ectkw.assign_partial_charges(offmol, 'espaloma-am1bcc')
    # Ensure its not all 0s
    assert (abs(offmol.partial_charges.value_in_unit(unit.elementary_charge)) > 0.01).any(), offmol.partial_charges

def test_create_system():
    offmol = create_ethanol()
    ff = ForceField('openff-2.0.0.offxml')
    ff.deregister_parameter_handler('ToolkitAM1BCC')
    ff.get_parameter_handler('ChargeIncrementModel', {'version': '0.3',
                                                      'partial_charge_method': 'espaloma-am1bcc'})
    sys = ff.create_openmm_system(offmol.to_topology(),
                                  toolkit_registry=ToolkitRegistry([EspalomaChargeToolkitWrapper, RDKitToolkitWrapper]))

def test_create_interchange():
    offmol = create_ethanol()
    ff = ForceField('openff-2.0.0.offxml')
    ff.deregister_parameter_handler('ToolkitAM1BCC')
    ff.get_parameter_handler('ChargeIncrementModel', {'version': '0.3',
                                                      'partial_charge_method': 'espaloma-am1bcc'})
    interchange = ff.create_interchange(offmol.to_topology(),
                                        toolkit_registry=ToolkitRegistry([EspalomaChargeToolkitWrapper, RDKitToolkitWrapper]))


# TODO: Tests for user-provided use_conformers, strict_n_conformers, normalize_partial_charges