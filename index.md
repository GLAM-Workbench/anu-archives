# ANU Archives

This repository contains Jupyter notebooks that help you work with data from the ANU Archives. The notebooks currently focus on the [Sydney Stock exchange stock and share lists](http://archivescollection.anu.edu.au/index.php/or59j). As the content note indicates:

> These are large format bound volumes of the official lists that were posted up for the public to see - 3 times a day - forenoon, noon and afternoon - at the close of the trading session in the call room at the Sydney Stock Exchange. The closing prices of stocks and shares were entered in by hand on pre-printed sheets.

There are 199 volumes covering the period from 1901 to 1950, containing more than 70,000 pages. Each page is divided into columns. The number of columns varies across the collection. Each column is divided into rows labelled with printed company or stock names. The prices are written alongside the company names.

We're currently working on ways of extracting company and share names, as well as the handwritten prices, from the digitised images. For more information see [this repository](https://github.com/wragge/sydney-stock-exchange). The notebooks below provide ways of navigating, visualising, and using the digitised pages.

See the [GLAM Workbench for more details](https://glam-workbench.github.io/anu-archives/).

## Notebooks

* Summary information about volumes – collates links and metadata relating to the 199 bound volumes in the Sydney Stock Exchange collection.
* Calendar view of the complete collection – helps you see the number of stock and share sheets in the bound volumes from the Sydney Stock Exchange for each day from 1901 to 1950.
* Display information about a single day's trading – select a date and this notebook will display information about any sheets that are available from this day. It notes where pages seem to be missing, and loads images of the pages for examination.
* Display details of pages within a date range – select a date range and this notebook will display information about available sheets from all the days within the range.
* Visualise page data – explores the aggregated page metadata from all 199 volumes.

If you haven't used Jupyter notebooks before, you might want to try the Getting Started notebook. It introduces some basic concepts using data from the National Museum of Australia.

## Data files

* [CSV-formatted list of all 70,000+ pages](https://github.com/GLAM-Workbench/anu-archives/blob/master/complete_page_list.csv) in the bound volumes including their date and session (Morning, Noon, Afternoon). Duplicate images are excluded.
* [CSV-formatted list of all dates](https://github.com/GLAM-Workbench/anu-archives/blob/master/complete_date_list.csv) within the period of the volumes. Includes the number of pages available for each date, and the number of pages expected (the number of pages produced each day changes across the collection). On dates with no pages, the `reason` field is used to record details of holidays or other interruptions to trading (some with links to Trove).
* [CSV-formatted list of holidays](https://github.com/GLAM-Workbench/anu-archives/blob/master/nsw_holidays_1900_1950.csv) in NSW from 1901 to 1950.
* Full data about missing, misplaced, and duplicated pages is saved in [`page_data_master.py`](https://github.com/GLAM-Workbench/anu-archives/blob/master/page_data_master.py). This data is combined with the holiday data to generate the complete page and date lists above.



## Cite as

See the GLAM Workbench or [Zenodo](https://doi.org/10.5281/zenodo.3545044) for up-to-date citation details.

[![DOI](https://zenodo.org/badge/DOI/10.5281/zenodo.3545044.svg)](https://doi.org/10.5281/zenodo.3545044)

----

This repository is part of the [GLAM Workbench](https://glam-workbench.github.io/).  

If you think this project is worthwhile, you might like [to support me on GitHub](https://github.com/sponsors/wragge).
