# intro
this is generally a pandas.Dataframe usage for querying, for more info please refer to official documentation. 
-------
# series-data-structure
- index
    bisa pake custom index, walau tidak di dalam seriesnya (di dalam dictionary) 
- name 
- values
- sum()
- append(), hati hati buat indexing ke dict yang beda, mirip sama query di sql 

# data frame data structures
- transpose
- mirip sama sql buat ngequery tabel 
- you can chain operations from series, **avoid at all cost**
- drop function (deleting columns)
    - returns a new variable, doesn't replace the old one. 
    - bisa pake inplace=true di dalam argumennya biar gak perlu bikin copy variable lagi   
    - axis, row yang akan di drop, kalo mau drop column berarti set ke 1
- del function
    - immediate effect, gak return apa2 
- adding column tinggal tambah arraynya aja, dendgan set value sesuai keinginan

# Boolean masking
- if you add rows with Series, pandas will automatically input Nan values kalo gak ada yang di set ke dalam index nya, very nice. 
*Venn Diagram*
- outer join == union
- inner join == intersection
- left join _y
- right join y_
## Group By 
- splitting dataframe to chunks, return tuple sesuai kondisi grup nya 
## Apply 
## Scales
### ratio scale
- units equally space
- height, weight
### interval scale
- no true zero, units equally space
- arah mata angin, suhu 
### ordinal scale
- order of units is important, not equally space
- nilai test
### nominal scale (Categorical data) 
- categorical units, but between categories there are no order to one another 
- team of sports
## Pivot table
- aggregation function, by making a new table for reference purposes
- marginal values, so we can see the relation between variables at a glance 

## nan
not a number, pake isnan(nan) buat ngecek value, gak bisa langsung pake itenerary if condition  
## indexing
bisa pake `iloc` buat refer ke nomor indexnya atau `loc` buat name dari dictionary 
# advanced python objects
## map()
returns object of an output of a function, which uses multiple arguments to be inserted
## lambda()
anonymous function, lazy function making, no complex logic because single expression.
useful for simple data cleaning task

# numpy 
working with arrays and matrices in python 
## arrays
### arrange
### linespace
### resize
### reshape
## operations
### T
### setype
### min, max
### mean
### std (standar deviation)
### argmax, argmin (index of a max/min value)
