# ChemSpyder research data model

This reasearch data model following the software-driven-rdm specifications serves to capture chemical species from ChemSpider.

## Objects

### Collection

The Collection serves as the root object of the data model and can hold multiple Species.

- name
  - Type: string
  - Description: An optional name for the Collection.
- created
  - Type: datetime
  - Description: The timestamp of this Collection's creation.
