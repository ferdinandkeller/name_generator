# Name Generator for Python.

You can use this package to generate funny names in the same say the [Moby Project](https://github.com/moby/moby/blob/4f0d95fa6ee7f865597c03b9e63702cdcb0f7067/pkg/namesgenerator/names-generator.go) does.

Here is an example:

```python
from name_generator import random_name

for _ in range(10):
    print(random_name())

# Output:
# gracious_archimedes
# jovial_benz
# elated_neumann
# elastic_chandrasekhar
# flamboyant_franklin
# vigorous_jang
# distracted_boyd
# sharp_hawking
# friendly_northcutt
# stupefied_easley
```

You can also use a custom separator:

```python
from name_generator import random_name

print(random_name(separator="."))
# Output: "happy.fermat"
```

Or import the list of adjectives and last names:

```python
from name_generator import adjectives, lastnames
```