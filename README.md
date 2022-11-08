# Espaloma Charge
Standalone charge assignment from Espaloma framework. https://doi.org/10.1039/D2SC02739A

## Installation

```bash
pip install espaloma_charge
```

## Example

```python
>>> from rdkit import Chem; from espaloma_charge import charge
>>> molecule = Chem.MolFromSmiles("N#N")
>>> charge(molecule)
array([0., 0.], dtype=float32)

```

Use it in Google Colab to assign partial charges to your favorite molecule:

[![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/drive/1e14EkNyidPI0wXBGcewh9m9LC1imSRWZ?usp=sharing)]

## Reference
If you are using this little tool in your pipeline, please consider citing:

```
@Article{D2SC02739A,
author ="Wang, Yuanqing and Fass, Josh and Kaminow, Benjamin and Herr, John E. and Rufa, Dominic and Zhang, Ivy and Pulido, Iván and Henry, Mike and Bruce Macdonald, Hannah E. and Takaba, Kenichiro and Chodera, John D.",
title  ="End-to-end differentiable construction of molecular mechanics force fields",
journal  ="Chem. Sci.",
year  ="2022",
volume  ="13",
issue  ="41",
pages  ="12016-12033",
publisher  ="The Royal Society of Chemistry",
doi  ="10.1039/D2SC02739A",
url  ="http://dx.doi.org/10.1039/D2SC02739A"}

```
