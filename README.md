# Datasets @ APEX Lab

## ANNOUNCEMENT
This dataset is a standard version of indexed iPinyou/criteo dataset (threshold chosen) **ONLY IN APEX LAB**.

## Usage
At the very beginning, run command
`echo NASPATH > .naspath`
where `NASPATH` here is the mounted path of NAS.

## Python package `apexdsets`

Use
```python
import sys
sys.path.append("REPOSITORY")
import apexdsets
```
to import package `apexdsets`, where `"REPOSITORY"` here represents the path of **this** repository.
<br/>

### Method: `datapath(dataname)`
Return the absolute file path given the name of the dataset (`dataname`).
<br/>

### Class: `apexdsets.CTRLoader`

#### Method: `__init__(datapath)`
Constructor. Example:
```python
loader = CTRLoader(datapath("ipinyou"))
```

#### Method: `meta(key)`

Args:

* `key`: the key of the meta information.
	* `"names"` for the names of fields.
	* `"sizes"` for the sizes of fields.
	* `"dtypes"` for the data types of fields, including
		* `"num"` for numerical field,
		* `"cate"` for categorical field.
	* `"index2cate"` for the maps of fields from their indices to the original categories.
	* `"cate2index"` for the maps of fields from their original categories to the indices. (This option is invalid for `criteo` dataset)
	
Returns:
A python object (usually a list) for the meta information of key `key`.
<br/>

#### Method: `data_generator(dsetname, batch_size, unified_index=True)`
To get a generator, yielding data in pair `(inputs, labels)`.

Args:

* `dsetname`: the name of the dataset, usually
	* `"train"`,
	* `"test"`.
* `batch_size`: the size of a batch.
* `unified_index`: which represents whether to unify all index. If false, all fields will have its own index, starting from `0`.

Returns:
A generator for data packed in batches.
<br/>

#### Property: unified_size
A value representing the total number of categories across all categorical fields

## iPinyou
Threshold chosen: `5`

Fields:

* The first one represents click-or-not
* Other `28` fields are categorical

Original dataset includes:

* `15395258` samples in the training set
* `4100716` samples in the test set

Positive samples over total samples: `0.075%`.

## criteo
Threshold chosen: `20`

Use `day_6.gz` to `day_12.gz` as training set, `day_13.gz` as test set.

Negative-down sampling used, positive samples over total samples: `50%`.

