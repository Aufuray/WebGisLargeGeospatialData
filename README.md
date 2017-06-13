# WebGisLargeGeospatialData

A Geographic Information System (GIS) is a computer system for capturing, storing,
checking, and displaying data related to positions on Earth’s surface. GIS can show
many different kinds of data on one map, such as streets, buildings, and vegetation.
This enables people to more easily see, analyze, and understand patterns and
relationships.

With the birth of the Web, we have seen immense value and broad applicability of GIS
and the endless possibilities that can be achieved when integrating GIS systems into
flexible Web architectures for use with modern IT infrastructure.

Traditional WebGIS systems has limited capability in handling large-scale geospatial
data. This project integrates a GPU-accelerated spatial database backend with Google
Maps API to support visualizing and querying large-scale geospatial data in a web
environment.

The large data set used in this project is the global biodiversity data on species
distributions. This data contains more than 1.6 million species, collected over three
centuries of natural history exploration and including current observations from citizen
scientists, researchers and automated monitoring programmes.

The size and nature of this data makes this project a good case-study to take
advantage of the massive capabilities of the GPU, we hope to achieve significant
performance speedup compared to traditional Web GIS applications run on CPU.
