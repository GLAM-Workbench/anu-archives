# ANU Archives

This repository contains Jupyter notebooks that help you work with data from the ANU Archives. The notebooks currently focus on the [Sydney Stock exchange stock and share lists](http://archivescollection.anu.edu.au/index.php/or59j). As the content note indicates:

> These are large format bound volumes of the official lists that were posted up for the public to see - 3 times a day - forenoon, noon and afternoon - at the close of the trading session in the call room at the Sydney Stock Exchange. The closing prices of stocks and shares were entered in by hand on pre-printed sheets.

There are 199 volumes covering the period from 1901 to 1950, containing more than 70,000 pages. Each page is divided into columns. The number of columns varies across the collection. Each column is divided into rows labelled with printed company or stock names. The prices are written alongside the company names.

We're currently working on ways of extracting company and share names, as well as the handwritten prices, from the digitised images. For more information see [this repository](https://github.com/wragge/sydney-stock-exchange). The notebooks below provide ways of navigating, visualising, and using the digitised pages.

See the [GLAM Workbench for more details](https://glam-workbench.github.io/anu-archives/).

## Notebooks

* [Summary information about volumes](stock-exchange-details-by-volume.ipynb) – collates links and metadata relating to the 199 bound volumes in the Sydney Stock Exchange collection.
* [Calendar view of the complete collection](stock-exchange-pages-calendar.ipynb) – helps you see the number of stock and share sheets in the bound volumes from the Sydney Stock Exchange for each day from 1901 to 1950.
* [Display information about a single day's trading](view-pages-by-date.ipynb) – select a date and this notebook will display information about any sheets that are available from this day. It notes where pages seem to be missing, and loads images of the pages for examination.
* [Display details of pages within a date range](view-pages-by-date-range.ipynb) – select a date range and this notebook will display information about available sheets from all the days within the range.
* [Visualise page data](pages_viz.ipynb) – explores the aggregated page metadata from all 199 volumes.

If you haven't used Jupyter notebooks before, you might want to try the Getting Started notebook. It introduces some basic concepts using data from the National Museum of Australia.

## Data files

* [CSV-formatted list of all 70,000+ pages](https://github.com/GLAM-Workbench/anu-archives/blob/master/complete_page_list.csv) in the bound volumes including their date and session (Morning, Noon, Afternoon). Duplicate images are excluded.
* [CSV-formatted list of all dates](https://github.com/GLAM-Workbench/anu-archives/blob/master/complete_date_list.csv) within the period of the volumes. Includes the number of pages available for each date, and the number of pages expected (the number of pages produced each day changes across the collection). On dates with no pages, the `reason` field is used to record details of holidays or other interruptions to trading (some with links to Trove).
* [CSV-formatted list of holidays](https://github.com/GLAM-Workbench/anu-archives/blob/master/nsw_holidays_1900_1950.csv) in NSW from 1901 to 1950.
* Full data about missing, misplaced, and duplicated pages is saved in [`page_data_master.py`](https://github.com/GLAM-Workbench/anu-archives/blob/master/page_data_master.py). This data is combined with the holiday data to generate the complete page and date lists above.


<!-- START RUN INFO -->

## Run these notebooks

There are a number of different ways to use these notebooks. Binder is quickest and easiest, but it doesn't save your data. I've listed the options below from easiest to most complicated (requiring more technical knowledge).

### Using Binder

[![Launch on Binder](https://mybinder.org/badge_logo.svg)](https://mybinder.org/v2/gh/GLAM-Workbench/anu-archives/master?urlpath=lab%2Ftree%2Findex.md)

Click on the button above to launch the notebooks in this repository using the [Binder](https://mybinder.org/) service (it might take a little while to load). This is a free service, but note that sessions will close if you stop using the notebooks, and no data will be saved. Make sure you download any changed notebooks or harvested data that you want to save.

### Using Reclaim Cloud

[![Launch on Reclaim Cloud](https://glam-workbench.github.io/images/launch-on-reclaim-cloud.svg)](https://app.my.reclaim.cloud/?manifest=https://raw.githubusercontent.com/GLAM-Workbench/anu-archives/master/reclaim-manifest.jps)

[Reclaim Cloud](https://reclaim.cloud/) is a paid hosting service, aimed particularly at supported digital scholarship in hte humanities. Unlike Binder, the environments you create on Reclaim Cloud will save your data – even if you switch them off! To run this repository on Reclaim Cloud for the first time:

* Create a [Reclaim Cloud](https://reclaim.cloud/) account and log in.
* Click on the button above to start the installation process.
* A dialogue box will ask you to set a password, this is used to limit access to your Jupyter installation.
* Sit back and wait for the installation to complete!
* Once the installation is finished click on the 'Open in Browser' button of your newly created environment (note that you might need to wait a few minutes before everything is ready).

See the GLAM Workbench for more details.

### Using Docker

You can use Docker to run a pre-built computing environment on your own computer. It will set up everything you need to run the notebooks in this repository. This is free, but requires more technical knowledge – you'll have to install Docker on your computer, and be able to use the command line.

* Install [Docker Desktop](https://docs.docker.com/get-docker/).
* Create a new directory for this repository and open it from the command line.
* From the command line, run the following command:  
  ```
  docker run -p 8888:8888 --name anu-archives -v "$PWD":/home/jovyan/work glamworkbench/anu-archives repo2docker-entrypoint jupyter lab --ip 0.0.0.0 --NotebookApp.token='' --LabApp.default_url='/lab/tree/index.md'
  ```
* It will take a while to download and configure the Docker image. Once it's ready you'll see a message saying that Jupyter Notebook is running.
* Point your web browser to `http://127.0.0.1:8888`

See the GLAM Workbench for more details.

### Setting up on your own computer

If you know your way around the command line and are comfortable installing software, you might want to set up your own computer to run these notebooks.

Assuming you have recent versions of Python and Git installed, the steps might be something like:

* Create a virtual environment, eg: `python -m venv anu-archives`
* Open the new directory" `cd trove-harvester`
* Activate the environment `source bin/activate`
* Clone the repository: `git clone https://github.com/GLAM-Workbench/anu-archives.git notebooks`
* Open the new `notebooks` directory: `cd notebooks`
* Install the necessary Python packages: `pip install -r requirements.txt`
* Run Jupyter: `jupyter lab`

See the GLAM Workbench for more details.

<!-- END RUN INFO -->

## Cite as

See the GLAM Workbench or [Zenodo](https://doi.org/10.5281/zenodo.3545044) for up-to-date citation details.

[![DOI](https://zenodo.org/badge/DOI/10.5281/zenodo.3545044.svg)](https://doi.org/10.5281/zenodo.3545044)

----

This repository is part of the [GLAM Workbench](https://glam-workbench.github.io/).  

If you think this project is worthwhile, you might like [to support me on GitHub](https://github.com/sponsors/wragge).
