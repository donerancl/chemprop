from dataclasses import dataclass, field

from chemprop.featurizers.atom import MultiHotAtomFeaturizer, AtomFeaturizer
from chemprop.featurizers.bond import MultiHotBondFeaturizer, BondFeaturizer


@dataclass
class _MolGraphFeaturizerMixin:
    atom_featurizer: AtomFeaturizer = field(default_factory=MultiHotAtomFeaturizer.default)
    bond_featurizer: BondFeaturizer = field(default_factory=MultiHotBondFeaturizer)

    def __post_init__(self):
        self.atom_fdim = len(self.atom_featurizer)
        self.bond_fdim = len(self.bond_featurizer)

    @property
    def shape(self) -> tuple[int, int]:
        """the feature dimension of the atoms and bonds, respectively, of `MolGraph`s generated by
        this featurizer"""
        return self.atom_fdim, self.bond_fdim
