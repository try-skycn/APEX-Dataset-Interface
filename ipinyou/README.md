# iPinyou Dataset @ APEX Lab

## ANNOUNCEMENT
This dataset is a standard version of indexed iPinyou dataset (threshold chosen) **ONLY IN APEX LAB**.

## Configuration
Threshold chosen: `5`

Fields:

* The first one represents click-or-not
* Other `28` fields are categorical

Original dataset includes:

* `15395258` samples in the training set
* `4100716` samples in the test set

Positive samples over total samples: `0.075%`

## Usage

Default dataset file is `ipinyou/data`.

### CTRLoader

How to use:

```python
from ipinyou import CTRLoader
```

#### `meta(key)`

Args:

* `key`: the key of the meta information.
	* `"names"` for the names of fields.
	* `"sizes"` for the sizes of fields.
	* `"dtypes"` for the data types of fields, including
		* `"num"` for numerical field,
		* `"cate"` for categorical field.
	* `"index2cate"` for the maps of fields from their indices to the original categories.
	* `"cate2index"` for the maps of fields from their original categories to the indices.
	
Returns:

A python object (usually a list) for the meta information of key `key`.

#### `data_generator(dsetname, batch_size, unified_index=True)`

To get a generator, yielding data in pair `(inputs, labels)`.

Args:

* `dsetname`: the name of the dataset, usually
	* `"train"`,
	* `"test"`.
* `batch_size`: the size of a batch.
* `unified_index`: which represents whether to unify all index. If false, all fields will have its own index, starting from `0`.

Returns:

A generator for data packed in batches.


