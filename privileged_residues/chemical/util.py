from collections import namedtuple

# the order of the keys of this dictionary
FunctionalGroup = namedtuple("FunctionalGroup", ["resName", "donor", "acceptor", "atoms"])
FunctionalGroup.__doc__ = """Store hydrogen bonding information about a
functional group as well as information that can be used to position it
in three-space.

Attributes
----------
resName : str
    Name of the functional group.
donor : bool
    True if the functional group can be a donor in a hydrogen bond.
acceptor : bool
    True if the functional group can be an acceptor in a hydrogen bond.
atoms : list of str
    List of three atom names that are used to construct a coordinate
    frame to describe the position of the functional group in three-space.
"""

functional_groups = {
    "OH_": FunctionalGroup("hydroxide", True, True, ["CV", "OH", "HH"]),
    "G__": FunctionalGroup("guanidinium", True, False, ["CZ", "NH1", "NH2"]),
    "I__": FunctionalGroup("imidazole", True, True, ["ND1", "CD2", "NE2"]),
    # imidazole tautomer
    "ID_": FunctionalGroup("imidazole_D", True, True, ["ND1", "CD2", "NE2"]),
    "A__": FunctionalGroup("amine", True, False, ["NZ", "1HZ", "2HZ"]),
    "C__": FunctionalGroup("carboxylate", False, True, ["CD", "OE1", "OE2"]),
    "CA_": FunctionalGroup("carboxamide", True, True, ["CG", "OD1", "ND2"])
}

ResInfo = namedtuple("ResInfo", ["grp", "atoms"])
ResInfo.__doc__ = """Store functional group information about an amino
acid as well as information that can be used to position it in
three-space.

Attributes
----------
grp : str
    Name of a functional group.
atoms : list of str
    List of three atom names that are used to construct a coordinate
    frame to describe the position of the functional group of the amino
    acid in three-space.
"""

def resolve_rays(groups):
    """Expand list of interaction groups into the appropriate ray
    selection methods.

    Parameters
    ----------
    groups : list of str
        Interaction groups to search in.

    Returns
    -------
    list of tuple of str, function
        Names of groups and the corresponding ray selectors for the
        groups.
    """

    from . import (
        bidentate, network, catpi
    )
    ray_bins = {
        "bidentate": [
            ("sc_sc", bidentate.sc_sc_rays),
            ("sc_scbb", bidentate.sc_scbb_rays),
            ("sc_bb", bidentate.sc_bb_rays)
        ],
        "network": [
            ("acceptor_acceptor", network.acceptor_acceptor_rays),
            ("acceptor_donor", network.donor_acceptor_rays),
            ("donor_acceptor", network.donor_acceptor_rays),
            ("donor_donor", network.donor_donor_rays)
        ],
        "cation-pi": [("cation-pi", catpi.rays)]
    }

    ray_selectors = [ ]

    for group in groups:
        for k in ray_bins:
            for v in ray_bins[k]:
                if group in [k, v[0]]:
                    ray_selectors.append(v)

    return ray_selectors
