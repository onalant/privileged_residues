.. _tutorial:

Tutorial
========

.. _tutorial_begin:

First steps with Privileged Residues
------------------------------------

A PrivilegedResidues instance is created like so:

    >>> from privileged_residues.core import PrivilegedResidues
    >>> pr = PrivilegedResidues("$DATA_TABLES_PATH")

Additionally, you will need a `pyrosetta.Pose` to search and a
`pyrosetta.rosetta.core.select.residue_selector.ResidueSelector` to select
target sites in the structure.

    >>> pose = pyrosetta.pose_from_sequence("AAAAA")
    >>> select = pyrosetta.rosetta.core.select.residue_selector.TrueResidueSelector()

With the pose and residue selector in hand, you can search the data-tables
for potential privileged interaction sites::

    >>> matches = pr.search(pose, selector)

.. _tutorial_limit:

Limiting match groups
---------------------

Currently, the following search groups are available::

    + bidentate
    |
    +--> sc_sc
    |
    +--> sc_scbb
    |
    +--> sc_bb

    + network
    |
    +--> acceptor_acceptor
    |
    +--> acceptor_donor
    |
    +--> donor_acceptor
    |
    +--> donor_donor

    + cation-pi

The default behavior of :func:`PrivilegedResidues.search` is to search in all
of the groups. This can be undesirable if matching speed is a priority. It
is possible to restrict the search space by passing a subset of the above
groups to :func:`PrivilegedResidues.search`::

    >>> matches = pr.search(pose, selector, groups=["sc_sc", "donor_donor"])

PrivilegedResidues will also resolve group hierarchies, so

    >>> matches = pr.search(pose, selector, groups=["bidentate"])

is equivalent to

    >>> matches = pr.search(pose, selector, groups=["sc_sc", "sc_scbb", "sc_bb"])
