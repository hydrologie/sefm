```python
import xarray as xr
import fsspec
from distributed import Client
import hvplot.xarray
import numpy as np
```








# Intrants


```python
latlngbox = [-82, -74, 44.5, 49]
```

# Client Dask (pour paralléliser l'ensemble du code)


```python
client = Client()
client
```




<table style="border: 2px solid white;">
<tr>
<td style="vertical-align: top; border: 0px solid white">
<h3 style="text-align: left;">Client</h3>
<ul style="text-align: left; list-style: none; margin: 0; padding: 0;">
  <li><b>Scheduler: </b>tcp://127.0.0.1:41411</li>
  <li><b>Dashboard: </b><a href='http://127.0.0.1:8787/status' target='_blank'>http://127.0.0.1:8787/status</a>
</ul>
</td>
<td style="vertical-align: top; border: 0px solid white">
<h3 style="text-align: left;">Cluster</h3>
<ul style="text-align: left; list-style:none; margin: 0; padding: 0;">
  <li><b>Workers: </b>8</li>
  <li><b>Cores: </b>32</li>
  <li><b>Memory: </b>135.00 GB</li>
</ul>
</td>
</tr>
</table>



# Importation de ERA5-Land vers un dataset (ds)


```python
ds = xr.open_zarr(fsspec.get_mapper('s3://era5-atlantic-northeast/zarr/land/reanalysis',
                                   client_kwargs={'endpoint_url': 'https://s3.us-east-2.wasabisys.com'}),
                  consolidated=True)
```

# Calculs des grilles 


```python
# Accès à un sous ensemble des données via le lazy loading

ds = ds.sel(time=slice('1981-01-01', '2010-12-31'),
            longitude=slice(latlngbox[0], latlngbox[1]),
            latitude=slice(latlngbox[3], latlngbox[2]))
```


```python
ds
```




<div><svg style="position: absolute; width: 0; height: 0; overflow: hidden">
<defs>
<symbol id="icon-database" viewBox="0 0 32 32">
<title>Show/Hide data repr</title>
<path d="M16 0c-8.837 0-16 2.239-16 5v4c0 2.761 7.163 5 16 5s16-2.239 16-5v-4c0-2.761-7.163-5-16-5z"></path>
<path d="M16 17c-8.837 0-16-2.239-16-5v6c0 2.761 7.163 5 16 5s16-2.239 16-5v-6c0 2.761-7.163 5-16 5z"></path>
<path d="M16 26c-8.837 0-16-2.239-16-5v6c0 2.761 7.163 5 16 5s16-2.239 16-5v-6c0 2.761-7.163 5-16 5z"></path>
</symbol>
<symbol id="icon-file-text2" viewBox="0 0 32 32">
<title>Show/Hide attributes</title>
<path d="M28.681 7.159c-0.694-0.947-1.662-2.053-2.724-3.116s-2.169-2.030-3.116-2.724c-1.612-1.182-2.393-1.319-2.841-1.319h-15.5c-1.378 0-2.5 1.121-2.5 2.5v27c0 1.378 1.122 2.5 2.5 2.5h23c1.378 0 2.5-1.122 2.5-2.5v-19.5c0-0.448-0.137-1.23-1.319-2.841zM24.543 5.457c0.959 0.959 1.712 1.825 2.268 2.543h-4.811v-4.811c0.718 0.556 1.584 1.309 2.543 2.268zM28 29.5c0 0.271-0.229 0.5-0.5 0.5h-23c-0.271 0-0.5-0.229-0.5-0.5v-27c0-0.271 0.229-0.5 0.5-0.5 0 0 15.499-0 15.5 0v7c0 0.552 0.448 1 1 1h7v19.5z"></path>
<path d="M23 26h-14c-0.552 0-1-0.448-1-1s0.448-1 1-1h14c0.552 0 1 0.448 1 1s-0.448 1-1 1z"></path>
<path d="M23 22h-14c-0.552 0-1-0.448-1-1s0.448-1 1-1h14c0.552 0 1 0.448 1 1s-0.448 1-1 1z"></path>
<path d="M23 18h-14c-0.552 0-1-0.448-1-1s0.448-1 1-1h14c0.552 0 1 0.448 1 1s-0.448 1-1 1z"></path>
</symbol>
</defs>
</svg>
<style>/* CSS stylesheet for displaying xarray objects in jupyterlab.
 *
 */

:root {
  --xr-font-color0: var(--jp-content-font-color0, rgba(0, 0, 0, 1));
  --xr-font-color2: var(--jp-content-font-color2, rgba(0, 0, 0, 0.54));
  --xr-font-color3: var(--jp-content-font-color3, rgba(0, 0, 0, 0.38));
  --xr-border-color: var(--jp-border-color2, #e0e0e0);
  --xr-disabled-color: var(--jp-layout-color3, #bdbdbd);
  --xr-background-color: var(--jp-layout-color0, white);
  --xr-background-color-row-even: var(--jp-layout-color1, white);
  --xr-background-color-row-odd: var(--jp-layout-color2, #eeeeee);
}

.xr-wrap {
  min-width: 300px;
  max-width: 700px;
}

.xr-header {
  padding-top: 6px;
  padding-bottom: 6px;
  margin-bottom: 4px;
  border-bottom: solid 1px var(--xr-border-color);
}

.xr-header > div,
.xr-header > ul {
  display: inline;
  margin-top: 0;
  margin-bottom: 0;
}

.xr-obj-type,
.xr-array-name {
  margin-left: 2px;
  margin-right: 10px;
}

.xr-obj-type {
  color: var(--xr-font-color2);
}

.xr-sections {
  padding-left: 0 !important;
  display: grid;
  grid-template-columns: 150px auto auto 1fr 20px 20px;
}

.xr-section-item {
  display: contents;
}

.xr-section-item input {
  display: none;
}

.xr-section-item input + label {
  color: var(--xr-disabled-color);
}

.xr-section-item input:enabled + label {
  cursor: pointer;
  color: var(--xr-font-color2);
}

.xr-section-item input:enabled + label:hover {
  color: var(--xr-font-color0);
}

.xr-section-summary {
  grid-column: 1;
  color: var(--xr-font-color2);
  font-weight: 500;
}

.xr-section-summary > span {
  display: inline-block;
  padding-left: 0.5em;
}

.xr-section-summary-in:disabled + label {
  color: var(--xr-font-color2);
}

.xr-section-summary-in + label:before {
  display: inline-block;
  content: '►';
  font-size: 11px;
  width: 15px;
  text-align: center;
}

.xr-section-summary-in:disabled + label:before {
  color: var(--xr-disabled-color);
}

.xr-section-summary-in:checked + label:before {
  content: '▼';
}

.xr-section-summary-in:checked + label > span {
  display: none;
}

.xr-section-summary,
.xr-section-inline-details {
  padding-top: 4px;
  padding-bottom: 4px;
}

.xr-section-inline-details {
  grid-column: 2 / -1;
}

.xr-section-details {
  display: none;
  grid-column: 1 / -1;
  margin-bottom: 5px;
}

.xr-section-summary-in:checked ~ .xr-section-details {
  display: contents;
}

.xr-array-wrap {
  grid-column: 1 / -1;
  display: grid;
  grid-template-columns: 20px auto;
}

.xr-array-wrap > label {
  grid-column: 1;
  vertical-align: top;
}

.xr-preview {
  color: var(--xr-font-color3);
}

.xr-array-preview,
.xr-array-data {
  padding: 0 5px !important;
  grid-column: 2;
}

.xr-array-data,
.xr-array-in:checked ~ .xr-array-preview {
  display: none;
}

.xr-array-in:checked ~ .xr-array-data,
.xr-array-preview {
  display: inline-block;
}

.xr-dim-list {
  display: inline-block !important;
  list-style: none;
  padding: 0 !important;
  margin: 0;
}

.xr-dim-list li {
  display: inline-block;
  padding: 0;
  margin: 0;
}

.xr-dim-list:before {
  content: '(';
}

.xr-dim-list:after {
  content: ')';
}

.xr-dim-list li:not(:last-child):after {
  content: ',';
  padding-right: 5px;
}

.xr-has-index {
  font-weight: bold;
}

.xr-var-list,
.xr-var-item {
  display: contents;
}

.xr-var-item > div,
.xr-var-item label,
.xr-var-item > .xr-var-name span {
  background-color: var(--xr-background-color-row-even);
  margin-bottom: 0;
}

.xr-var-item > .xr-var-name:hover span {
  padding-right: 5px;
}

.xr-var-list > li:nth-child(odd) > div,
.xr-var-list > li:nth-child(odd) > label,
.xr-var-list > li:nth-child(odd) > .xr-var-name span {
  background-color: var(--xr-background-color-row-odd);
}

.xr-var-name {
  grid-column: 1;
}

.xr-var-dims {
  grid-column: 2;
}

.xr-var-dtype {
  grid-column: 3;
  text-align: right;
  color: var(--xr-font-color2);
}

.xr-var-preview {
  grid-column: 4;
}

.xr-var-name,
.xr-var-dims,
.xr-var-dtype,
.xr-preview,
.xr-attrs dt {
  white-space: nowrap;
  overflow: hidden;
  text-overflow: ellipsis;
  padding-right: 10px;
}

.xr-var-name:hover,
.xr-var-dims:hover,
.xr-var-dtype:hover,
.xr-attrs dt:hover {
  overflow: visible;
  width: auto;
  z-index: 1;
}

.xr-var-attrs,
.xr-var-data {
  display: none;
  background-color: var(--xr-background-color) !important;
  padding-bottom: 5px !important;
}

.xr-var-attrs-in:checked ~ .xr-var-attrs,
.xr-var-data-in:checked ~ .xr-var-data {
  display: block;
}

.xr-var-data > table {
  float: right;
}

.xr-var-name span,
.xr-var-data,
.xr-attrs {
  padding-left: 25px !important;
}

.xr-attrs,
.xr-var-attrs,
.xr-var-data {
  grid-column: 1 / -1;
}

dl.xr-attrs {
  padding: 0;
  margin: 0;
  display: grid;
  grid-template-columns: 125px auto;
}

.xr-attrs dt, dd {
  padding: 0;
  margin: 0;
  float: left;
  padding-right: 10px;
  width: auto;
}

.xr-attrs dt {
  font-weight: normal;
  grid-column: 1;
}

.xr-attrs dt:hover span {
  display: inline-block;
  background: var(--xr-background-color);
  padding-right: 10px;
}

.xr-attrs dd {
  grid-column: 2;
  white-space: pre-wrap;
  word-break: break-all;
}

.xr-icon-database,
.xr-icon-file-text2 {
  display: inline-block;
  vertical-align: middle;
  width: 1em;
  height: 1.5em !important;
  stroke-width: 0;
  stroke: currentColor;
  fill: currentColor;
}
</style><div class='xr-wrap'><div class='xr-header'><div class='xr-obj-type'>xarray.Dataset</div></div><ul class='xr-sections'><li class='xr-section-item'><input id='section-edc82774-3d56-4393-b49d-d95cb4d1c8d1' class='xr-section-summary-in' type='checkbox' disabled ><label for='section-edc82774-3d56-4393-b49d-d95cb4d1c8d1' class='xr-section-summary'  title='Expand/collapse section'>Dimensions:</label><div class='xr-section-inline-details'><ul class='xr-dim-list'><li><span class='xr-has-index'>latitude</span>: 46</li><li><span class='xr-has-index'>longitude</span>: 81</li><li><span class='xr-has-index'>time</span>: 262968</li></ul></div><div class='xr-section-details'></div></li><li class='xr-section-item'><input id='section-c60be910-400f-40d0-a9b3-014ae4ceeb79' class='xr-section-summary-in' type='checkbox'  checked><label for='section-c60be910-400f-40d0-a9b3-014ae4ceeb79' class='xr-section-summary' >Coordinates: <span>(3)</span></label><div class='xr-section-inline-details'></div><div class='xr-section-details'><ul class='xr-var-list'><li class='xr-var-item'><div class='xr-var-name'><span class='xr-has-index'>latitude</span></div><div class='xr-var-dims'>(latitude)</div><div class='xr-var-dtype'>float32</div><div class='xr-var-preview xr-preview'>49.0 48.9 48.8 ... 44.7 44.6 44.5</div><input id='attrs-d6fbb2c8-7d75-4fe3-8b1a-af1cf66c186c' class='xr-var-attrs-in' type='checkbox' ><label for='attrs-d6fbb2c8-7d75-4fe3-8b1a-af1cf66c186c' title='Show/Hide attributes'><svg class='icon xr-icon-file-text2'><use xlink:href='#icon-file-text2'></use></svg></label><input id='data-c601ef39-6144-4445-9e22-6d29cd61006b' class='xr-var-data-in' type='checkbox'><label for='data-c601ef39-6144-4445-9e22-6d29cd61006b' title='Show/Hide data repr'><svg class='icon xr-icon-database'><use xlink:href='#icon-database'></use></svg></label><div class='xr-var-attrs'><dl class='xr-attrs'><dt><span>long_name :</span></dt><dd>latitude</dd><dt><span>units :</span></dt><dd>degrees_north</dd></dl></div><pre class='xr-var-data'>array([49. , 48.9, 48.8, 48.7, 48.6, 48.5, 48.4, 48.3, 48.2, 48.1, 48. , 47.9,
       47.8, 47.7, 47.6, 47.5, 47.4, 47.3, 47.2, 47.1, 47. , 46.9, 46.8, 46.7,
       46.6, 46.5, 46.4, 46.3, 46.2, 46.1, 46. , 45.9, 45.8, 45.7, 45.6, 45.5,
       45.4, 45.3, 45.2, 45.1, 45. , 44.9, 44.8, 44.7, 44.6, 44.5],
      dtype=float32)</pre></li><li class='xr-var-item'><div class='xr-var-name'><span class='xr-has-index'>longitude</span></div><div class='xr-var-dims'>(longitude)</div><div class='xr-var-dtype'>float32</div><div class='xr-var-preview xr-preview'>-82.0 -81.9 -81.8 ... -74.1 -74.0</div><input id='attrs-6d216ab9-724e-4a05-a1d2-87d038bb0d69' class='xr-var-attrs-in' type='checkbox' ><label for='attrs-6d216ab9-724e-4a05-a1d2-87d038bb0d69' title='Show/Hide attributes'><svg class='icon xr-icon-file-text2'><use xlink:href='#icon-file-text2'></use></svg></label><input id='data-ddf53039-6b36-4483-bc8f-7696b05598fe' class='xr-var-data-in' type='checkbox'><label for='data-ddf53039-6b36-4483-bc8f-7696b05598fe' title='Show/Hide data repr'><svg class='icon xr-icon-database'><use xlink:href='#icon-database'></use></svg></label><div class='xr-var-attrs'><dl class='xr-attrs'><dt><span>long_name :</span></dt><dd>longitude</dd><dt><span>units :</span></dt><dd>degrees_east</dd></dl></div><pre class='xr-var-data'>array([-82. , -81.9, -81.8, -81.7, -81.6, -81.5, -81.4, -81.3, -81.2, -81.1,
       -81. , -80.9, -80.8, -80.7, -80.6, -80.5, -80.4, -80.3, -80.2, -80.1,
       -80. , -79.9, -79.8, -79.7, -79.6, -79.5, -79.4, -79.3, -79.2, -79.1,
       -79. , -78.9, -78.8, -78.7, -78.6, -78.5, -78.4, -78.3, -78.2, -78.1,
       -78. , -77.9, -77.8, -77.7, -77.6, -77.5, -77.4, -77.3, -77.2, -77.1,
       -77. , -76.9, -76.8, -76.7, -76.6, -76.5, -76.4, -76.3, -76.2, -76.1,
       -76. , -75.9, -75.8, -75.7, -75.6, -75.5, -75.4, -75.3, -75.2, -75.1,
       -75. , -74.9, -74.8, -74.7, -74.6, -74.5, -74.4, -74.3, -74.2, -74.1,
       -74. ], dtype=float32)</pre></li><li class='xr-var-item'><div class='xr-var-name'><span class='xr-has-index'>time</span></div><div class='xr-var-dims'>(time)</div><div class='xr-var-dtype'>datetime64[ns]</div><div class='xr-var-preview xr-preview'>1981-01-01 ... 2010-12-31T23:00:00</div><input id='attrs-e7271668-e73c-497f-b4ea-83bae99d1ac1' class='xr-var-attrs-in' type='checkbox' ><label for='attrs-e7271668-e73c-497f-b4ea-83bae99d1ac1' title='Show/Hide attributes'><svg class='icon xr-icon-file-text2'><use xlink:href='#icon-file-text2'></use></svg></label><input id='data-080d3ead-a1b2-4bd6-a586-d5676b1719f2' class='xr-var-data-in' type='checkbox'><label for='data-080d3ead-a1b2-4bd6-a586-d5676b1719f2' title='Show/Hide data repr'><svg class='icon xr-icon-database'><use xlink:href='#icon-database'></use></svg></label><div class='xr-var-attrs'><dl class='xr-attrs'><dt><span>long_name :</span></dt><dd>time</dd></dl></div><pre class='xr-var-data'>array([&#x27;1981-01-01T00:00:00.000000000&#x27;, &#x27;1981-01-01T01:00:00.000000000&#x27;,
       &#x27;1981-01-01T02:00:00.000000000&#x27;, ..., &#x27;2010-12-31T21:00:00.000000000&#x27;,
       &#x27;2010-12-31T22:00:00.000000000&#x27;, &#x27;2010-12-31T23:00:00.000000000&#x27;],
      dtype=&#x27;datetime64[ns]&#x27;)</pre></li></ul></div></li><li class='xr-section-item'><input id='section-aa33d2a6-2008-41f1-bfb9-a6b1bfbcd334' class='xr-section-summary-in' type='checkbox'  ><label for='section-aa33d2a6-2008-41f1-bfb9-a6b1bfbcd334' class='xr-section-summary' >Data variables: <span>(19)</span></label><div class='xr-section-inline-details'></div><div class='xr-section-details'><ul class='xr-var-list'><li class='xr-var-item'><div class='xr-var-name'><span>d2m</span></div><div class='xr-var-dims'>(time, latitude, longitude)</div><div class='xr-var-dtype'>float64</div><div class='xr-var-preview xr-preview'>dask.array&lt;chunksize=(8760, 10, 10), meta=np.ndarray&gt;</div><input id='attrs-868f8612-2888-4917-a686-6b1cebbec980' class='xr-var-attrs-in' type='checkbox' disabled><label for='attrs-868f8612-2888-4917-a686-6b1cebbec980' title='Show/Hide attributes'><svg class='icon xr-icon-file-text2'><use xlink:href='#icon-file-text2'></use></svg></label><input id='data-94e5ff38-1281-4cb6-bc9e-50c1fe9fedee' class='xr-var-data-in' type='checkbox'><label for='data-94e5ff38-1281-4cb6-bc9e-50c1fe9fedee' title='Show/Hide data repr'><svg class='icon xr-icon-database'><use xlink:href='#icon-database'></use></svg></label><div class='xr-var-attrs'><dl class='xr-attrs'></dl></div><pre class='xr-var-data'><table>
<tr>
<td>
<table>
  <thead>
    <tr><td> </td><th> Array </th><th> Chunk </th></tr>
  </thead>
  <tbody>
    <tr><th> Bytes </th><td> 7.84 GB </td> <td> 43.80 MB </td></tr>
    <tr><th> Shape </th><td> (262968, 46, 81) </td> <td> (8760, 25, 25) </td></tr>
    <tr><th> Count </th><td> 7573 Tasks </td><td> 372 Chunks </td></tr>
    <tr><th> Type </th><td> float64 </td><td> numpy.ndarray </td></tr>
  </tbody>
</table>
</td>
<td>
<svg width="156" height="146" style="stroke:rgb(0,0,0);stroke-width:1" >

  <!-- Horizontal lines -->
  <line x1="10" y1="0" x2="80" y2="70" style="stroke-width:2" />
  <line x1="10" y1="5" x2="80" y2="76" />
  <line x1="10" y1="19" x2="80" y2="89" />
  <line x1="10" y1="25" x2="80" y2="96" style="stroke-width:2" />

  <!-- Vertical lines -->
  <line x1="10" y1="0" x2="10" y2="25" style="stroke-width:2" />
  <line x1="12" y1="2" x2="12" y2="27" />
  <line x1="14" y1="4" x2="14" y2="30" />
  <line x1="17" y1="7" x2="17" y2="32" />
  <line x1="19" y1="9" x2="19" y2="34" />
  <line x1="21" y1="11" x2="21" y2="37" />
  <line x1="24" y1="14" x2="24" y2="39" />
  <line x1="26" y1="16" x2="26" y2="41" />
  <line x1="28" y1="18" x2="28" y2="44" />
  <line x1="31" y1="21" x2="31" y2="46" />
  <line x1="33" y1="23" x2="33" y2="48" />
  <line x1="35" y1="25" x2="35" y2="51" />
  <line x1="38" y1="28" x2="38" y2="53" />
  <line x1="40" y1="30" x2="40" y2="55" />
  <line x1="42" y1="32" x2="42" y2="58" />
  <line x1="45" y1="35" x2="45" y2="60" />
  <line x1="47" y1="37" x2="47" y2="63" />
  <line x1="49" y1="39" x2="49" y2="65" />
  <line x1="52" y1="42" x2="52" y2="67" />
  <line x1="54" y1="44" x2="54" y2="70" />
  <line x1="57" y1="47" x2="57" y2="72" />
  <line x1="59" y1="49" x2="59" y2="74" />
  <line x1="61" y1="51" x2="61" y2="77" />
  <line x1="64" y1="54" x2="64" y2="79" />
  <line x1="66" y1="56" x2="66" y2="81" />
  <line x1="68" y1="58" x2="68" y2="84" />
  <line x1="71" y1="61" x2="71" y2="86" />
  <line x1="73" y1="63" x2="73" y2="88" />
  <line x1="75" y1="65" x2="75" y2="91" />
  <line x1="78" y1="68" x2="78" y2="93" />
  <line x1="80" y1="70" x2="80" y2="95" />
  <line x1="80" y1="70" x2="80" y2="96" style="stroke-width:2" />

  <!-- Colored Rectangle -->
  <polygon points="10.000000,0.000000 80.588235,70.588235 80.588235,96.000852 10.000000,25.412617" style="fill:#ECB172A0;stroke-width:0"/>

  <!-- Horizontal lines -->
  <line x1="10" y1="0" x2="35" y2="0" style="stroke-width:2" />
  <line x1="12" y1="2" x2="37" y2="2" />
  <line x1="14" y1="4" x2="40" y2="4" />
  <line x1="17" y1="7" x2="42" y2="7" />
  <line x1="19" y1="9" x2="44" y2="9" />
  <line x1="21" y1="11" x2="47" y2="11" />
  <line x1="24" y1="14" x2="49" y2="14" />
  <line x1="26" y1="16" x2="51" y2="16" />
  <line x1="28" y1="18" x2="54" y2="18" />
  <line x1="31" y1="21" x2="56" y2="21" />
  <line x1="33" y1="23" x2="58" y2="23" />
  <line x1="35" y1="25" x2="61" y2="25" />
  <line x1="38" y1="28" x2="63" y2="28" />
  <line x1="40" y1="30" x2="65" y2="30" />
  <line x1="42" y1="32" x2="68" y2="32" />
  <line x1="45" y1="35" x2="70" y2="35" />
  <line x1="47" y1="37" x2="73" y2="37" />
  <line x1="49" y1="39" x2="75" y2="39" />
  <line x1="52" y1="42" x2="77" y2="42" />
  <line x1="54" y1="44" x2="80" y2="44" />
  <line x1="57" y1="47" x2="82" y2="47" />
  <line x1="59" y1="49" x2="84" y2="49" />
  <line x1="61" y1="51" x2="87" y2="51" />
  <line x1="64" y1="54" x2="89" y2="54" />
  <line x1="66" y1="56" x2="91" y2="56" />
  <line x1="68" y1="58" x2="94" y2="58" />
  <line x1="71" y1="61" x2="96" y2="61" />
  <line x1="73" y1="63" x2="98" y2="63" />
  <line x1="75" y1="65" x2="101" y2="65" />
  <line x1="78" y1="68" x2="103" y2="68" />
  <line x1="80" y1="70" x2="105" y2="70" />
  <line x1="80" y1="70" x2="106" y2="70" style="stroke-width:2" />

  <!-- Vertical lines -->
  <line x1="10" y1="0" x2="80" y2="70" style="stroke-width:2" />
  <line x1="13" y1="0" x2="83" y2="70" />
  <line x1="20" y1="0" x2="91" y2="70" />
  <line x1="28" y1="0" x2="99" y2="70" />
  <line x1="35" y1="0" x2="106" y2="70" style="stroke-width:2" />

  <!-- Colored Rectangle -->
  <polygon points="10.000000,0.000000 35.412617,0.000000 106.000852,70.588235 80.588235,70.588235" style="fill:#ECB172A0;stroke-width:0"/>

  <!-- Horizontal lines -->
  <line x1="80" y1="70" x2="106" y2="70" style="stroke-width:2" />
  <line x1="80" y1="76" x2="106" y2="76" />
  <line x1="80" y1="89" x2="106" y2="89" />
  <line x1="80" y1="96" x2="106" y2="96" style="stroke-width:2" />

  <!-- Vertical lines -->
  <line x1="80" y1="70" x2="80" y2="96" style="stroke-width:2" />
  <line x1="83" y1="70" x2="83" y2="96" />
  <line x1="91" y1="70" x2="91" y2="96" />
  <line x1="99" y1="70" x2="99" y2="96" />
  <line x1="106" y1="70" x2="106" y2="96" style="stroke-width:2" />

  <!-- Colored Rectangle -->
  <polygon points="80.588235,70.588235 106.000852,70.588235 106.000852,96.000852 80.588235,96.000852" style="fill:#ECB172A0;stroke-width:0"/>

  <!-- Text -->
  <text x="93.294544" y="116.000852" font-size="1.0rem" font-weight="100" text-anchor="middle" >81</text>
  <text x="126.000852" y="83.294544" font-size="1.0rem" font-weight="100" text-anchor="middle" transform="rotate(0,126.000852,83.294544)">46</text>
  <text x="35.294118" y="80.706734" font-size="1.0rem" font-weight="100" text-anchor="middle" transform="rotate(45,35.294118,80.706734)">262968</text>
</svg>
</td>
</tr>
</table></pre></li><li class='xr-var-item'><div class='xr-var-name'><span>e</span></div><div class='xr-var-dims'>(time, latitude, longitude)</div><div class='xr-var-dtype'>float64</div><div class='xr-var-preview xr-preview'>dask.array&lt;chunksize=(8760, 10, 10), meta=np.ndarray&gt;</div><input id='attrs-449afd42-cb18-4ed7-a3bc-6df29fd940e0' class='xr-var-attrs-in' type='checkbox' disabled><label for='attrs-449afd42-cb18-4ed7-a3bc-6df29fd940e0' title='Show/Hide attributes'><svg class='icon xr-icon-file-text2'><use xlink:href='#icon-file-text2'></use></svg></label><input id='data-3aab91bc-a7f2-4534-aba9-deadce87472a' class='xr-var-data-in' type='checkbox'><label for='data-3aab91bc-a7f2-4534-aba9-deadce87472a' title='Show/Hide data repr'><svg class='icon xr-icon-database'><use xlink:href='#icon-database'></use></svg></label><div class='xr-var-attrs'><dl class='xr-attrs'></dl></div><pre class='xr-var-data'><table>
<tr>
<td>
<table>
  <thead>
    <tr><td> </td><th> Array </th><th> Chunk </th></tr>
  </thead>
  <tbody>
    <tr><th> Bytes </th><td> 7.84 GB </td> <td> 43.80 MB </td></tr>
    <tr><th> Shape </th><td> (262968, 46, 81) </td> <td> (8760, 25, 25) </td></tr>
    <tr><th> Count </th><td> 7573 Tasks </td><td> 372 Chunks </td></tr>
    <tr><th> Type </th><td> float64 </td><td> numpy.ndarray </td></tr>
  </tbody>
</table>
</td>
<td>
<svg width="156" height="146" style="stroke:rgb(0,0,0);stroke-width:1" >

  <!-- Horizontal lines -->
  <line x1="10" y1="0" x2="80" y2="70" style="stroke-width:2" />
  <line x1="10" y1="5" x2="80" y2="76" />
  <line x1="10" y1="19" x2="80" y2="89" />
  <line x1="10" y1="25" x2="80" y2="96" style="stroke-width:2" />

  <!-- Vertical lines -->
  <line x1="10" y1="0" x2="10" y2="25" style="stroke-width:2" />
  <line x1="12" y1="2" x2="12" y2="27" />
  <line x1="14" y1="4" x2="14" y2="30" />
  <line x1="17" y1="7" x2="17" y2="32" />
  <line x1="19" y1="9" x2="19" y2="34" />
  <line x1="21" y1="11" x2="21" y2="37" />
  <line x1="24" y1="14" x2="24" y2="39" />
  <line x1="26" y1="16" x2="26" y2="41" />
  <line x1="28" y1="18" x2="28" y2="44" />
  <line x1="31" y1="21" x2="31" y2="46" />
  <line x1="33" y1="23" x2="33" y2="48" />
  <line x1="35" y1="25" x2="35" y2="51" />
  <line x1="38" y1="28" x2="38" y2="53" />
  <line x1="40" y1="30" x2="40" y2="55" />
  <line x1="42" y1="32" x2="42" y2="58" />
  <line x1="45" y1="35" x2="45" y2="60" />
  <line x1="47" y1="37" x2="47" y2="63" />
  <line x1="49" y1="39" x2="49" y2="65" />
  <line x1="52" y1="42" x2="52" y2="67" />
  <line x1="54" y1="44" x2="54" y2="70" />
  <line x1="57" y1="47" x2="57" y2="72" />
  <line x1="59" y1="49" x2="59" y2="74" />
  <line x1="61" y1="51" x2="61" y2="77" />
  <line x1="64" y1="54" x2="64" y2="79" />
  <line x1="66" y1="56" x2="66" y2="81" />
  <line x1="68" y1="58" x2="68" y2="84" />
  <line x1="71" y1="61" x2="71" y2="86" />
  <line x1="73" y1="63" x2="73" y2="88" />
  <line x1="75" y1="65" x2="75" y2="91" />
  <line x1="78" y1="68" x2="78" y2="93" />
  <line x1="80" y1="70" x2="80" y2="95" />
  <line x1="80" y1="70" x2="80" y2="96" style="stroke-width:2" />

  <!-- Colored Rectangle -->
  <polygon points="10.000000,0.000000 80.588235,70.588235 80.588235,96.000852 10.000000,25.412617" style="fill:#ECB172A0;stroke-width:0"/>

  <!-- Horizontal lines -->
  <line x1="10" y1="0" x2="35" y2="0" style="stroke-width:2" />
  <line x1="12" y1="2" x2="37" y2="2" />
  <line x1="14" y1="4" x2="40" y2="4" />
  <line x1="17" y1="7" x2="42" y2="7" />
  <line x1="19" y1="9" x2="44" y2="9" />
  <line x1="21" y1="11" x2="47" y2="11" />
  <line x1="24" y1="14" x2="49" y2="14" />
  <line x1="26" y1="16" x2="51" y2="16" />
  <line x1="28" y1="18" x2="54" y2="18" />
  <line x1="31" y1="21" x2="56" y2="21" />
  <line x1="33" y1="23" x2="58" y2="23" />
  <line x1="35" y1="25" x2="61" y2="25" />
  <line x1="38" y1="28" x2="63" y2="28" />
  <line x1="40" y1="30" x2="65" y2="30" />
  <line x1="42" y1="32" x2="68" y2="32" />
  <line x1="45" y1="35" x2="70" y2="35" />
  <line x1="47" y1="37" x2="73" y2="37" />
  <line x1="49" y1="39" x2="75" y2="39" />
  <line x1="52" y1="42" x2="77" y2="42" />
  <line x1="54" y1="44" x2="80" y2="44" />
  <line x1="57" y1="47" x2="82" y2="47" />
  <line x1="59" y1="49" x2="84" y2="49" />
  <line x1="61" y1="51" x2="87" y2="51" />
  <line x1="64" y1="54" x2="89" y2="54" />
  <line x1="66" y1="56" x2="91" y2="56" />
  <line x1="68" y1="58" x2="94" y2="58" />
  <line x1="71" y1="61" x2="96" y2="61" />
  <line x1="73" y1="63" x2="98" y2="63" />
  <line x1="75" y1="65" x2="101" y2="65" />
  <line x1="78" y1="68" x2="103" y2="68" />
  <line x1="80" y1="70" x2="105" y2="70" />
  <line x1="80" y1="70" x2="106" y2="70" style="stroke-width:2" />

  <!-- Vertical lines -->
  <line x1="10" y1="0" x2="80" y2="70" style="stroke-width:2" />
  <line x1="13" y1="0" x2="83" y2="70" />
  <line x1="20" y1="0" x2="91" y2="70" />
  <line x1="28" y1="0" x2="99" y2="70" />
  <line x1="35" y1="0" x2="106" y2="70" style="stroke-width:2" />

  <!-- Colored Rectangle -->
  <polygon points="10.000000,0.000000 35.412617,0.000000 106.000852,70.588235 80.588235,70.588235" style="fill:#ECB172A0;stroke-width:0"/>

  <!-- Horizontal lines -->
  <line x1="80" y1="70" x2="106" y2="70" style="stroke-width:2" />
  <line x1="80" y1="76" x2="106" y2="76" />
  <line x1="80" y1="89" x2="106" y2="89" />
  <line x1="80" y1="96" x2="106" y2="96" style="stroke-width:2" />

  <!-- Vertical lines -->
  <line x1="80" y1="70" x2="80" y2="96" style="stroke-width:2" />
  <line x1="83" y1="70" x2="83" y2="96" />
  <line x1="91" y1="70" x2="91" y2="96" />
  <line x1="99" y1="70" x2="99" y2="96" />
  <line x1="106" y1="70" x2="106" y2="96" style="stroke-width:2" />

  <!-- Colored Rectangle -->
  <polygon points="80.588235,70.588235 106.000852,70.588235 106.000852,96.000852 80.588235,96.000852" style="fill:#ECB172A0;stroke-width:0"/>

  <!-- Text -->
  <text x="93.294544" y="116.000852" font-size="1.0rem" font-weight="100" text-anchor="middle" >81</text>
  <text x="126.000852" y="83.294544" font-size="1.0rem" font-weight="100" text-anchor="middle" transform="rotate(0,126.000852,83.294544)">46</text>
  <text x="35.294118" y="80.706734" font-size="1.0rem" font-weight="100" text-anchor="middle" transform="rotate(45,35.294118,80.706734)">262968</text>
</svg>
</td>
</tr>
</table></pre></li><li class='xr-var-item'><div class='xr-var-name'><span>licd</span></div><div class='xr-var-dims'>(time, latitude, longitude)</div><div class='xr-var-dtype'>float64</div><div class='xr-var-preview xr-preview'>dask.array&lt;chunksize=(8760, 10, 10), meta=np.ndarray&gt;</div><input id='attrs-826765dd-c30e-41eb-a178-e38a6f4793da' class='xr-var-attrs-in' type='checkbox' disabled><label for='attrs-826765dd-c30e-41eb-a178-e38a6f4793da' title='Show/Hide attributes'><svg class='icon xr-icon-file-text2'><use xlink:href='#icon-file-text2'></use></svg></label><input id='data-659063ed-bb35-4c70-b89c-30c08e962d6a' class='xr-var-data-in' type='checkbox'><label for='data-659063ed-bb35-4c70-b89c-30c08e962d6a' title='Show/Hide data repr'><svg class='icon xr-icon-database'><use xlink:href='#icon-database'></use></svg></label><div class='xr-var-attrs'><dl class='xr-attrs'></dl></div><pre class='xr-var-data'><table>
<tr>
<td>
<table>
  <thead>
    <tr><td> </td><th> Array </th><th> Chunk </th></tr>
  </thead>
  <tbody>
    <tr><th> Bytes </th><td> 7.84 GB </td> <td> 43.80 MB </td></tr>
    <tr><th> Shape </th><td> (262968, 46, 81) </td> <td> (8760, 25, 25) </td></tr>
    <tr><th> Count </th><td> 7573 Tasks </td><td> 372 Chunks </td></tr>
    <tr><th> Type </th><td> float64 </td><td> numpy.ndarray </td></tr>
  </tbody>
</table>
</td>
<td>
<svg width="156" height="146" style="stroke:rgb(0,0,0);stroke-width:1" >

  <!-- Horizontal lines -->
  <line x1="10" y1="0" x2="80" y2="70" style="stroke-width:2" />
  <line x1="10" y1="5" x2="80" y2="76" />
  <line x1="10" y1="19" x2="80" y2="89" />
  <line x1="10" y1="25" x2="80" y2="96" style="stroke-width:2" />

  <!-- Vertical lines -->
  <line x1="10" y1="0" x2="10" y2="25" style="stroke-width:2" />
  <line x1="12" y1="2" x2="12" y2="27" />
  <line x1="14" y1="4" x2="14" y2="30" />
  <line x1="17" y1="7" x2="17" y2="32" />
  <line x1="19" y1="9" x2="19" y2="34" />
  <line x1="21" y1="11" x2="21" y2="37" />
  <line x1="24" y1="14" x2="24" y2="39" />
  <line x1="26" y1="16" x2="26" y2="41" />
  <line x1="28" y1="18" x2="28" y2="44" />
  <line x1="31" y1="21" x2="31" y2="46" />
  <line x1="33" y1="23" x2="33" y2="48" />
  <line x1="35" y1="25" x2="35" y2="51" />
  <line x1="38" y1="28" x2="38" y2="53" />
  <line x1="40" y1="30" x2="40" y2="55" />
  <line x1="42" y1="32" x2="42" y2="58" />
  <line x1="45" y1="35" x2="45" y2="60" />
  <line x1="47" y1="37" x2="47" y2="63" />
  <line x1="49" y1="39" x2="49" y2="65" />
  <line x1="52" y1="42" x2="52" y2="67" />
  <line x1="54" y1="44" x2="54" y2="70" />
  <line x1="57" y1="47" x2="57" y2="72" />
  <line x1="59" y1="49" x2="59" y2="74" />
  <line x1="61" y1="51" x2="61" y2="77" />
  <line x1="64" y1="54" x2="64" y2="79" />
  <line x1="66" y1="56" x2="66" y2="81" />
  <line x1="68" y1="58" x2="68" y2="84" />
  <line x1="71" y1="61" x2="71" y2="86" />
  <line x1="73" y1="63" x2="73" y2="88" />
  <line x1="75" y1="65" x2="75" y2="91" />
  <line x1="78" y1="68" x2="78" y2="93" />
  <line x1="80" y1="70" x2="80" y2="95" />
  <line x1="80" y1="70" x2="80" y2="96" style="stroke-width:2" />

  <!-- Colored Rectangle -->
  <polygon points="10.000000,0.000000 80.588235,70.588235 80.588235,96.000852 10.000000,25.412617" style="fill:#ECB172A0;stroke-width:0"/>

  <!-- Horizontal lines -->
  <line x1="10" y1="0" x2="35" y2="0" style="stroke-width:2" />
  <line x1="12" y1="2" x2="37" y2="2" />
  <line x1="14" y1="4" x2="40" y2="4" />
  <line x1="17" y1="7" x2="42" y2="7" />
  <line x1="19" y1="9" x2="44" y2="9" />
  <line x1="21" y1="11" x2="47" y2="11" />
  <line x1="24" y1="14" x2="49" y2="14" />
  <line x1="26" y1="16" x2="51" y2="16" />
  <line x1="28" y1="18" x2="54" y2="18" />
  <line x1="31" y1="21" x2="56" y2="21" />
  <line x1="33" y1="23" x2="58" y2="23" />
  <line x1="35" y1="25" x2="61" y2="25" />
  <line x1="38" y1="28" x2="63" y2="28" />
  <line x1="40" y1="30" x2="65" y2="30" />
  <line x1="42" y1="32" x2="68" y2="32" />
  <line x1="45" y1="35" x2="70" y2="35" />
  <line x1="47" y1="37" x2="73" y2="37" />
  <line x1="49" y1="39" x2="75" y2="39" />
  <line x1="52" y1="42" x2="77" y2="42" />
  <line x1="54" y1="44" x2="80" y2="44" />
  <line x1="57" y1="47" x2="82" y2="47" />
  <line x1="59" y1="49" x2="84" y2="49" />
  <line x1="61" y1="51" x2="87" y2="51" />
  <line x1="64" y1="54" x2="89" y2="54" />
  <line x1="66" y1="56" x2="91" y2="56" />
  <line x1="68" y1="58" x2="94" y2="58" />
  <line x1="71" y1="61" x2="96" y2="61" />
  <line x1="73" y1="63" x2="98" y2="63" />
  <line x1="75" y1="65" x2="101" y2="65" />
  <line x1="78" y1="68" x2="103" y2="68" />
  <line x1="80" y1="70" x2="105" y2="70" />
  <line x1="80" y1="70" x2="106" y2="70" style="stroke-width:2" />

  <!-- Vertical lines -->
  <line x1="10" y1="0" x2="80" y2="70" style="stroke-width:2" />
  <line x1="13" y1="0" x2="83" y2="70" />
  <line x1="20" y1="0" x2="91" y2="70" />
  <line x1="28" y1="0" x2="99" y2="70" />
  <line x1="35" y1="0" x2="106" y2="70" style="stroke-width:2" />

  <!-- Colored Rectangle -->
  <polygon points="10.000000,0.000000 35.412617,0.000000 106.000852,70.588235 80.588235,70.588235" style="fill:#ECB172A0;stroke-width:0"/>

  <!-- Horizontal lines -->
  <line x1="80" y1="70" x2="106" y2="70" style="stroke-width:2" />
  <line x1="80" y1="76" x2="106" y2="76" />
  <line x1="80" y1="89" x2="106" y2="89" />
  <line x1="80" y1="96" x2="106" y2="96" style="stroke-width:2" />

  <!-- Vertical lines -->
  <line x1="80" y1="70" x2="80" y2="96" style="stroke-width:2" />
  <line x1="83" y1="70" x2="83" y2="96" />
  <line x1="91" y1="70" x2="91" y2="96" />
  <line x1="99" y1="70" x2="99" y2="96" />
  <line x1="106" y1="70" x2="106" y2="96" style="stroke-width:2" />

  <!-- Colored Rectangle -->
  <polygon points="80.588235,70.588235 106.000852,70.588235 106.000852,96.000852 80.588235,96.000852" style="fill:#ECB172A0;stroke-width:0"/>

  <!-- Text -->
  <text x="93.294544" y="116.000852" font-size="1.0rem" font-weight="100" text-anchor="middle" >81</text>
  <text x="126.000852" y="83.294544" font-size="1.0rem" font-weight="100" text-anchor="middle" transform="rotate(0,126.000852,83.294544)">46</text>
  <text x="35.294118" y="80.706734" font-size="1.0rem" font-weight="100" text-anchor="middle" transform="rotate(45,35.294118,80.706734)">262968</text>
</svg>
</td>
</tr>
</table></pre></li><li class='xr-var-item'><div class='xr-var-name'><span>sd</span></div><div class='xr-var-dims'>(time, latitude, longitude)</div><div class='xr-var-dtype'>float64</div><div class='xr-var-preview xr-preview'>dask.array&lt;chunksize=(8760, 10, 10), meta=np.ndarray&gt;</div><input id='attrs-8d6f066c-3f47-408d-be49-c562cb8ce91b' class='xr-var-attrs-in' type='checkbox' disabled><label for='attrs-8d6f066c-3f47-408d-be49-c562cb8ce91b' title='Show/Hide attributes'><svg class='icon xr-icon-file-text2'><use xlink:href='#icon-file-text2'></use></svg></label><input id='data-e53781fc-0d81-4588-aa22-2014bcfc90b5' class='xr-var-data-in' type='checkbox'><label for='data-e53781fc-0d81-4588-aa22-2014bcfc90b5' title='Show/Hide data repr'><svg class='icon xr-icon-database'><use xlink:href='#icon-database'></use></svg></label><div class='xr-var-attrs'><dl class='xr-attrs'></dl></div><pre class='xr-var-data'><table>
<tr>
<td>
<table>
  <thead>
    <tr><td> </td><th> Array </th><th> Chunk </th></tr>
  </thead>
  <tbody>
    <tr><th> Bytes </th><td> 7.84 GB </td> <td> 43.80 MB </td></tr>
    <tr><th> Shape </th><td> (262968, 46, 81) </td> <td> (8760, 25, 25) </td></tr>
    <tr><th> Count </th><td> 7573 Tasks </td><td> 372 Chunks </td></tr>
    <tr><th> Type </th><td> float64 </td><td> numpy.ndarray </td></tr>
  </tbody>
</table>
</td>
<td>
<svg width="156" height="146" style="stroke:rgb(0,0,0);stroke-width:1" >

  <!-- Horizontal lines -->
  <line x1="10" y1="0" x2="80" y2="70" style="stroke-width:2" />
  <line x1="10" y1="5" x2="80" y2="76" />
  <line x1="10" y1="19" x2="80" y2="89" />
  <line x1="10" y1="25" x2="80" y2="96" style="stroke-width:2" />

  <!-- Vertical lines -->
  <line x1="10" y1="0" x2="10" y2="25" style="stroke-width:2" />
  <line x1="12" y1="2" x2="12" y2="27" />
  <line x1="14" y1="4" x2="14" y2="30" />
  <line x1="17" y1="7" x2="17" y2="32" />
  <line x1="19" y1="9" x2="19" y2="34" />
  <line x1="21" y1="11" x2="21" y2="37" />
  <line x1="24" y1="14" x2="24" y2="39" />
  <line x1="26" y1="16" x2="26" y2="41" />
  <line x1="28" y1="18" x2="28" y2="44" />
  <line x1="31" y1="21" x2="31" y2="46" />
  <line x1="33" y1="23" x2="33" y2="48" />
  <line x1="35" y1="25" x2="35" y2="51" />
  <line x1="38" y1="28" x2="38" y2="53" />
  <line x1="40" y1="30" x2="40" y2="55" />
  <line x1="42" y1="32" x2="42" y2="58" />
  <line x1="45" y1="35" x2="45" y2="60" />
  <line x1="47" y1="37" x2="47" y2="63" />
  <line x1="49" y1="39" x2="49" y2="65" />
  <line x1="52" y1="42" x2="52" y2="67" />
  <line x1="54" y1="44" x2="54" y2="70" />
  <line x1="57" y1="47" x2="57" y2="72" />
  <line x1="59" y1="49" x2="59" y2="74" />
  <line x1="61" y1="51" x2="61" y2="77" />
  <line x1="64" y1="54" x2="64" y2="79" />
  <line x1="66" y1="56" x2="66" y2="81" />
  <line x1="68" y1="58" x2="68" y2="84" />
  <line x1="71" y1="61" x2="71" y2="86" />
  <line x1="73" y1="63" x2="73" y2="88" />
  <line x1="75" y1="65" x2="75" y2="91" />
  <line x1="78" y1="68" x2="78" y2="93" />
  <line x1="80" y1="70" x2="80" y2="95" />
  <line x1="80" y1="70" x2="80" y2="96" style="stroke-width:2" />

  <!-- Colored Rectangle -->
  <polygon points="10.000000,0.000000 80.588235,70.588235 80.588235,96.000852 10.000000,25.412617" style="fill:#ECB172A0;stroke-width:0"/>

  <!-- Horizontal lines -->
  <line x1="10" y1="0" x2="35" y2="0" style="stroke-width:2" />
  <line x1="12" y1="2" x2="37" y2="2" />
  <line x1="14" y1="4" x2="40" y2="4" />
  <line x1="17" y1="7" x2="42" y2="7" />
  <line x1="19" y1="9" x2="44" y2="9" />
  <line x1="21" y1="11" x2="47" y2="11" />
  <line x1="24" y1="14" x2="49" y2="14" />
  <line x1="26" y1="16" x2="51" y2="16" />
  <line x1="28" y1="18" x2="54" y2="18" />
  <line x1="31" y1="21" x2="56" y2="21" />
  <line x1="33" y1="23" x2="58" y2="23" />
  <line x1="35" y1="25" x2="61" y2="25" />
  <line x1="38" y1="28" x2="63" y2="28" />
  <line x1="40" y1="30" x2="65" y2="30" />
  <line x1="42" y1="32" x2="68" y2="32" />
  <line x1="45" y1="35" x2="70" y2="35" />
  <line x1="47" y1="37" x2="73" y2="37" />
  <line x1="49" y1="39" x2="75" y2="39" />
  <line x1="52" y1="42" x2="77" y2="42" />
  <line x1="54" y1="44" x2="80" y2="44" />
  <line x1="57" y1="47" x2="82" y2="47" />
  <line x1="59" y1="49" x2="84" y2="49" />
  <line x1="61" y1="51" x2="87" y2="51" />
  <line x1="64" y1="54" x2="89" y2="54" />
  <line x1="66" y1="56" x2="91" y2="56" />
  <line x1="68" y1="58" x2="94" y2="58" />
  <line x1="71" y1="61" x2="96" y2="61" />
  <line x1="73" y1="63" x2="98" y2="63" />
  <line x1="75" y1="65" x2="101" y2="65" />
  <line x1="78" y1="68" x2="103" y2="68" />
  <line x1="80" y1="70" x2="105" y2="70" />
  <line x1="80" y1="70" x2="106" y2="70" style="stroke-width:2" />

  <!-- Vertical lines -->
  <line x1="10" y1="0" x2="80" y2="70" style="stroke-width:2" />
  <line x1="13" y1="0" x2="83" y2="70" />
  <line x1="20" y1="0" x2="91" y2="70" />
  <line x1="28" y1="0" x2="99" y2="70" />
  <line x1="35" y1="0" x2="106" y2="70" style="stroke-width:2" />

  <!-- Colored Rectangle -->
  <polygon points="10.000000,0.000000 35.412617,0.000000 106.000852,70.588235 80.588235,70.588235" style="fill:#ECB172A0;stroke-width:0"/>

  <!-- Horizontal lines -->
  <line x1="80" y1="70" x2="106" y2="70" style="stroke-width:2" />
  <line x1="80" y1="76" x2="106" y2="76" />
  <line x1="80" y1="89" x2="106" y2="89" />
  <line x1="80" y1="96" x2="106" y2="96" style="stroke-width:2" />

  <!-- Vertical lines -->
  <line x1="80" y1="70" x2="80" y2="96" style="stroke-width:2" />
  <line x1="83" y1="70" x2="83" y2="96" />
  <line x1="91" y1="70" x2="91" y2="96" />
  <line x1="99" y1="70" x2="99" y2="96" />
  <line x1="106" y1="70" x2="106" y2="96" style="stroke-width:2" />

  <!-- Colored Rectangle -->
  <polygon points="80.588235,70.588235 106.000852,70.588235 106.000852,96.000852 80.588235,96.000852" style="fill:#ECB172A0;stroke-width:0"/>

  <!-- Text -->
  <text x="93.294544" y="116.000852" font-size="1.0rem" font-weight="100" text-anchor="middle" >81</text>
  <text x="126.000852" y="83.294544" font-size="1.0rem" font-weight="100" text-anchor="middle" transform="rotate(0,126.000852,83.294544)">46</text>
  <text x="35.294118" y="80.706734" font-size="1.0rem" font-weight="100" text-anchor="middle" transform="rotate(45,35.294118,80.706734)">262968</text>
</svg>
</td>
</tr>
</table></pre></li><li class='xr-var-item'><div class='xr-var-name'><span>sde</span></div><div class='xr-var-dims'>(time, latitude, longitude)</div><div class='xr-var-dtype'>float64</div><div class='xr-var-preview xr-preview'>dask.array&lt;chunksize=(8760, 10, 10), meta=np.ndarray&gt;</div><input id='attrs-f97443d3-e268-44ce-b531-35e4ef946490' class='xr-var-attrs-in' type='checkbox' disabled><label for='attrs-f97443d3-e268-44ce-b531-35e4ef946490' title='Show/Hide attributes'><svg class='icon xr-icon-file-text2'><use xlink:href='#icon-file-text2'></use></svg></label><input id='data-781da256-3104-4f6c-94e9-502539c1fc0e' class='xr-var-data-in' type='checkbox'><label for='data-781da256-3104-4f6c-94e9-502539c1fc0e' title='Show/Hide data repr'><svg class='icon xr-icon-database'><use xlink:href='#icon-database'></use></svg></label><div class='xr-var-attrs'><dl class='xr-attrs'></dl></div><pre class='xr-var-data'><table>
<tr>
<td>
<table>
  <thead>
    <tr><td> </td><th> Array </th><th> Chunk </th></tr>
  </thead>
  <tbody>
    <tr><th> Bytes </th><td> 7.84 GB </td> <td> 43.80 MB </td></tr>
    <tr><th> Shape </th><td> (262968, 46, 81) </td> <td> (8760, 25, 25) </td></tr>
    <tr><th> Count </th><td> 7573 Tasks </td><td> 372 Chunks </td></tr>
    <tr><th> Type </th><td> float64 </td><td> numpy.ndarray </td></tr>
  </tbody>
</table>
</td>
<td>
<svg width="156" height="146" style="stroke:rgb(0,0,0);stroke-width:1" >

  <!-- Horizontal lines -->
  <line x1="10" y1="0" x2="80" y2="70" style="stroke-width:2" />
  <line x1="10" y1="5" x2="80" y2="76" />
  <line x1="10" y1="19" x2="80" y2="89" />
  <line x1="10" y1="25" x2="80" y2="96" style="stroke-width:2" />

  <!-- Vertical lines -->
  <line x1="10" y1="0" x2="10" y2="25" style="stroke-width:2" />
  <line x1="12" y1="2" x2="12" y2="27" />
  <line x1="14" y1="4" x2="14" y2="30" />
  <line x1="17" y1="7" x2="17" y2="32" />
  <line x1="19" y1="9" x2="19" y2="34" />
  <line x1="21" y1="11" x2="21" y2="37" />
  <line x1="24" y1="14" x2="24" y2="39" />
  <line x1="26" y1="16" x2="26" y2="41" />
  <line x1="28" y1="18" x2="28" y2="44" />
  <line x1="31" y1="21" x2="31" y2="46" />
  <line x1="33" y1="23" x2="33" y2="48" />
  <line x1="35" y1="25" x2="35" y2="51" />
  <line x1="38" y1="28" x2="38" y2="53" />
  <line x1="40" y1="30" x2="40" y2="55" />
  <line x1="42" y1="32" x2="42" y2="58" />
  <line x1="45" y1="35" x2="45" y2="60" />
  <line x1="47" y1="37" x2="47" y2="63" />
  <line x1="49" y1="39" x2="49" y2="65" />
  <line x1="52" y1="42" x2="52" y2="67" />
  <line x1="54" y1="44" x2="54" y2="70" />
  <line x1="57" y1="47" x2="57" y2="72" />
  <line x1="59" y1="49" x2="59" y2="74" />
  <line x1="61" y1="51" x2="61" y2="77" />
  <line x1="64" y1="54" x2="64" y2="79" />
  <line x1="66" y1="56" x2="66" y2="81" />
  <line x1="68" y1="58" x2="68" y2="84" />
  <line x1="71" y1="61" x2="71" y2="86" />
  <line x1="73" y1="63" x2="73" y2="88" />
  <line x1="75" y1="65" x2="75" y2="91" />
  <line x1="78" y1="68" x2="78" y2="93" />
  <line x1="80" y1="70" x2="80" y2="95" />
  <line x1="80" y1="70" x2="80" y2="96" style="stroke-width:2" />

  <!-- Colored Rectangle -->
  <polygon points="10.000000,0.000000 80.588235,70.588235 80.588235,96.000852 10.000000,25.412617" style="fill:#ECB172A0;stroke-width:0"/>

  <!-- Horizontal lines -->
  <line x1="10" y1="0" x2="35" y2="0" style="stroke-width:2" />
  <line x1="12" y1="2" x2="37" y2="2" />
  <line x1="14" y1="4" x2="40" y2="4" />
  <line x1="17" y1="7" x2="42" y2="7" />
  <line x1="19" y1="9" x2="44" y2="9" />
  <line x1="21" y1="11" x2="47" y2="11" />
  <line x1="24" y1="14" x2="49" y2="14" />
  <line x1="26" y1="16" x2="51" y2="16" />
  <line x1="28" y1="18" x2="54" y2="18" />
  <line x1="31" y1="21" x2="56" y2="21" />
  <line x1="33" y1="23" x2="58" y2="23" />
  <line x1="35" y1="25" x2="61" y2="25" />
  <line x1="38" y1="28" x2="63" y2="28" />
  <line x1="40" y1="30" x2="65" y2="30" />
  <line x1="42" y1="32" x2="68" y2="32" />
  <line x1="45" y1="35" x2="70" y2="35" />
  <line x1="47" y1="37" x2="73" y2="37" />
  <line x1="49" y1="39" x2="75" y2="39" />
  <line x1="52" y1="42" x2="77" y2="42" />
  <line x1="54" y1="44" x2="80" y2="44" />
  <line x1="57" y1="47" x2="82" y2="47" />
  <line x1="59" y1="49" x2="84" y2="49" />
  <line x1="61" y1="51" x2="87" y2="51" />
  <line x1="64" y1="54" x2="89" y2="54" />
  <line x1="66" y1="56" x2="91" y2="56" />
  <line x1="68" y1="58" x2="94" y2="58" />
  <line x1="71" y1="61" x2="96" y2="61" />
  <line x1="73" y1="63" x2="98" y2="63" />
  <line x1="75" y1="65" x2="101" y2="65" />
  <line x1="78" y1="68" x2="103" y2="68" />
  <line x1="80" y1="70" x2="105" y2="70" />
  <line x1="80" y1="70" x2="106" y2="70" style="stroke-width:2" />

  <!-- Vertical lines -->
  <line x1="10" y1="0" x2="80" y2="70" style="stroke-width:2" />
  <line x1="13" y1="0" x2="83" y2="70" />
  <line x1="20" y1="0" x2="91" y2="70" />
  <line x1="28" y1="0" x2="99" y2="70" />
  <line x1="35" y1="0" x2="106" y2="70" style="stroke-width:2" />

  <!-- Colored Rectangle -->
  <polygon points="10.000000,0.000000 35.412617,0.000000 106.000852,70.588235 80.588235,70.588235" style="fill:#ECB172A0;stroke-width:0"/>

  <!-- Horizontal lines -->
  <line x1="80" y1="70" x2="106" y2="70" style="stroke-width:2" />
  <line x1="80" y1="76" x2="106" y2="76" />
  <line x1="80" y1="89" x2="106" y2="89" />
  <line x1="80" y1="96" x2="106" y2="96" style="stroke-width:2" />

  <!-- Vertical lines -->
  <line x1="80" y1="70" x2="80" y2="96" style="stroke-width:2" />
  <line x1="83" y1="70" x2="83" y2="96" />
  <line x1="91" y1="70" x2="91" y2="96" />
  <line x1="99" y1="70" x2="99" y2="96" />
  <line x1="106" y1="70" x2="106" y2="96" style="stroke-width:2" />

  <!-- Colored Rectangle -->
  <polygon points="80.588235,70.588235 106.000852,70.588235 106.000852,96.000852 80.588235,96.000852" style="fill:#ECB172A0;stroke-width:0"/>

  <!-- Text -->
  <text x="93.294544" y="116.000852" font-size="1.0rem" font-weight="100" text-anchor="middle" >81</text>
  <text x="126.000852" y="83.294544" font-size="1.0rem" font-weight="100" text-anchor="middle" transform="rotate(0,126.000852,83.294544)">46</text>
  <text x="35.294118" y="80.706734" font-size="1.0rem" font-weight="100" text-anchor="middle" transform="rotate(45,35.294118,80.706734)">262968</text>
</svg>
</td>
</tr>
</table></pre></li><li class='xr-var-item'><div class='xr-var-name'><span>sf</span></div><div class='xr-var-dims'>(time, latitude, longitude)</div><div class='xr-var-dtype'>float64</div><div class='xr-var-preview xr-preview'>dask.array&lt;chunksize=(8760, 10, 10), meta=np.ndarray&gt;</div><input id='attrs-3eabf523-bf29-40c1-be35-91b456527bc5' class='xr-var-attrs-in' type='checkbox' disabled><label for='attrs-3eabf523-bf29-40c1-be35-91b456527bc5' title='Show/Hide attributes'><svg class='icon xr-icon-file-text2'><use xlink:href='#icon-file-text2'></use></svg></label><input id='data-194fb471-f742-4eb0-9112-47d2cc764bbd' class='xr-var-data-in' type='checkbox'><label for='data-194fb471-f742-4eb0-9112-47d2cc764bbd' title='Show/Hide data repr'><svg class='icon xr-icon-database'><use xlink:href='#icon-database'></use></svg></label><div class='xr-var-attrs'><dl class='xr-attrs'></dl></div><pre class='xr-var-data'><table>
<tr>
<td>
<table>
  <thead>
    <tr><td> </td><th> Array </th><th> Chunk </th></tr>
  </thead>
  <tbody>
    <tr><th> Bytes </th><td> 7.84 GB </td> <td> 43.80 MB </td></tr>
    <tr><th> Shape </th><td> (262968, 46, 81) </td> <td> (8760, 25, 25) </td></tr>
    <tr><th> Count </th><td> 7573 Tasks </td><td> 372 Chunks </td></tr>
    <tr><th> Type </th><td> float64 </td><td> numpy.ndarray </td></tr>
  </tbody>
</table>
</td>
<td>
<svg width="156" height="146" style="stroke:rgb(0,0,0);stroke-width:1" >

  <!-- Horizontal lines -->
  <line x1="10" y1="0" x2="80" y2="70" style="stroke-width:2" />
  <line x1="10" y1="5" x2="80" y2="76" />
  <line x1="10" y1="19" x2="80" y2="89" />
  <line x1="10" y1="25" x2="80" y2="96" style="stroke-width:2" />

  <!-- Vertical lines -->
  <line x1="10" y1="0" x2="10" y2="25" style="stroke-width:2" />
  <line x1="12" y1="2" x2="12" y2="27" />
  <line x1="14" y1="4" x2="14" y2="30" />
  <line x1="17" y1="7" x2="17" y2="32" />
  <line x1="19" y1="9" x2="19" y2="34" />
  <line x1="21" y1="11" x2="21" y2="37" />
  <line x1="24" y1="14" x2="24" y2="39" />
  <line x1="26" y1="16" x2="26" y2="41" />
  <line x1="28" y1="18" x2="28" y2="44" />
  <line x1="31" y1="21" x2="31" y2="46" />
  <line x1="33" y1="23" x2="33" y2="48" />
  <line x1="35" y1="25" x2="35" y2="51" />
  <line x1="38" y1="28" x2="38" y2="53" />
  <line x1="40" y1="30" x2="40" y2="55" />
  <line x1="42" y1="32" x2="42" y2="58" />
  <line x1="45" y1="35" x2="45" y2="60" />
  <line x1="47" y1="37" x2="47" y2="63" />
  <line x1="49" y1="39" x2="49" y2="65" />
  <line x1="52" y1="42" x2="52" y2="67" />
  <line x1="54" y1="44" x2="54" y2="70" />
  <line x1="57" y1="47" x2="57" y2="72" />
  <line x1="59" y1="49" x2="59" y2="74" />
  <line x1="61" y1="51" x2="61" y2="77" />
  <line x1="64" y1="54" x2="64" y2="79" />
  <line x1="66" y1="56" x2="66" y2="81" />
  <line x1="68" y1="58" x2="68" y2="84" />
  <line x1="71" y1="61" x2="71" y2="86" />
  <line x1="73" y1="63" x2="73" y2="88" />
  <line x1="75" y1="65" x2="75" y2="91" />
  <line x1="78" y1="68" x2="78" y2="93" />
  <line x1="80" y1="70" x2="80" y2="95" />
  <line x1="80" y1="70" x2="80" y2="96" style="stroke-width:2" />

  <!-- Colored Rectangle -->
  <polygon points="10.000000,0.000000 80.588235,70.588235 80.588235,96.000852 10.000000,25.412617" style="fill:#ECB172A0;stroke-width:0"/>

  <!-- Horizontal lines -->
  <line x1="10" y1="0" x2="35" y2="0" style="stroke-width:2" />
  <line x1="12" y1="2" x2="37" y2="2" />
  <line x1="14" y1="4" x2="40" y2="4" />
  <line x1="17" y1="7" x2="42" y2="7" />
  <line x1="19" y1="9" x2="44" y2="9" />
  <line x1="21" y1="11" x2="47" y2="11" />
  <line x1="24" y1="14" x2="49" y2="14" />
  <line x1="26" y1="16" x2="51" y2="16" />
  <line x1="28" y1="18" x2="54" y2="18" />
  <line x1="31" y1="21" x2="56" y2="21" />
  <line x1="33" y1="23" x2="58" y2="23" />
  <line x1="35" y1="25" x2="61" y2="25" />
  <line x1="38" y1="28" x2="63" y2="28" />
  <line x1="40" y1="30" x2="65" y2="30" />
  <line x1="42" y1="32" x2="68" y2="32" />
  <line x1="45" y1="35" x2="70" y2="35" />
  <line x1="47" y1="37" x2="73" y2="37" />
  <line x1="49" y1="39" x2="75" y2="39" />
  <line x1="52" y1="42" x2="77" y2="42" />
  <line x1="54" y1="44" x2="80" y2="44" />
  <line x1="57" y1="47" x2="82" y2="47" />
  <line x1="59" y1="49" x2="84" y2="49" />
  <line x1="61" y1="51" x2="87" y2="51" />
  <line x1="64" y1="54" x2="89" y2="54" />
  <line x1="66" y1="56" x2="91" y2="56" />
  <line x1="68" y1="58" x2="94" y2="58" />
  <line x1="71" y1="61" x2="96" y2="61" />
  <line x1="73" y1="63" x2="98" y2="63" />
  <line x1="75" y1="65" x2="101" y2="65" />
  <line x1="78" y1="68" x2="103" y2="68" />
  <line x1="80" y1="70" x2="105" y2="70" />
  <line x1="80" y1="70" x2="106" y2="70" style="stroke-width:2" />

  <!-- Vertical lines -->
  <line x1="10" y1="0" x2="80" y2="70" style="stroke-width:2" />
  <line x1="13" y1="0" x2="83" y2="70" />
  <line x1="20" y1="0" x2="91" y2="70" />
  <line x1="28" y1="0" x2="99" y2="70" />
  <line x1="35" y1="0" x2="106" y2="70" style="stroke-width:2" />

  <!-- Colored Rectangle -->
  <polygon points="10.000000,0.000000 35.412617,0.000000 106.000852,70.588235 80.588235,70.588235" style="fill:#ECB172A0;stroke-width:0"/>

  <!-- Horizontal lines -->
  <line x1="80" y1="70" x2="106" y2="70" style="stroke-width:2" />
  <line x1="80" y1="76" x2="106" y2="76" />
  <line x1="80" y1="89" x2="106" y2="89" />
  <line x1="80" y1="96" x2="106" y2="96" style="stroke-width:2" />

  <!-- Vertical lines -->
  <line x1="80" y1="70" x2="80" y2="96" style="stroke-width:2" />
  <line x1="83" y1="70" x2="83" y2="96" />
  <line x1="91" y1="70" x2="91" y2="96" />
  <line x1="99" y1="70" x2="99" y2="96" />
  <line x1="106" y1="70" x2="106" y2="96" style="stroke-width:2" />

  <!-- Colored Rectangle -->
  <polygon points="80.588235,70.588235 106.000852,70.588235 106.000852,96.000852 80.588235,96.000852" style="fill:#ECB172A0;stroke-width:0"/>

  <!-- Text -->
  <text x="93.294544" y="116.000852" font-size="1.0rem" font-weight="100" text-anchor="middle" >81</text>
  <text x="126.000852" y="83.294544" font-size="1.0rem" font-weight="100" text-anchor="middle" transform="rotate(0,126.000852,83.294544)">46</text>
  <text x="35.294118" y="80.706734" font-size="1.0rem" font-weight="100" text-anchor="middle" transform="rotate(45,35.294118,80.706734)">262968</text>
</svg>
</td>
</tr>
</table></pre></li><li class='xr-var-item'><div class='xr-var-name'><span>skt</span></div><div class='xr-var-dims'>(time, latitude, longitude)</div><div class='xr-var-dtype'>float64</div><div class='xr-var-preview xr-preview'>dask.array&lt;chunksize=(8760, 10, 10), meta=np.ndarray&gt;</div><input id='attrs-e2ee5b03-3a53-4bc7-932e-69ddb265f8fa' class='xr-var-attrs-in' type='checkbox' disabled><label for='attrs-e2ee5b03-3a53-4bc7-932e-69ddb265f8fa' title='Show/Hide attributes'><svg class='icon xr-icon-file-text2'><use xlink:href='#icon-file-text2'></use></svg></label><input id='data-07acdc99-5f23-4c16-bd55-f3518128c128' class='xr-var-data-in' type='checkbox'><label for='data-07acdc99-5f23-4c16-bd55-f3518128c128' title='Show/Hide data repr'><svg class='icon xr-icon-database'><use xlink:href='#icon-database'></use></svg></label><div class='xr-var-attrs'><dl class='xr-attrs'></dl></div><pre class='xr-var-data'><table>
<tr>
<td>
<table>
  <thead>
    <tr><td> </td><th> Array </th><th> Chunk </th></tr>
  </thead>
  <tbody>
    <tr><th> Bytes </th><td> 7.84 GB </td> <td> 43.80 MB </td></tr>
    <tr><th> Shape </th><td> (262968, 46, 81) </td> <td> (8760, 25, 25) </td></tr>
    <tr><th> Count </th><td> 7573 Tasks </td><td> 372 Chunks </td></tr>
    <tr><th> Type </th><td> float64 </td><td> numpy.ndarray </td></tr>
  </tbody>
</table>
</td>
<td>
<svg width="156" height="146" style="stroke:rgb(0,0,0);stroke-width:1" >

  <!-- Horizontal lines -->
  <line x1="10" y1="0" x2="80" y2="70" style="stroke-width:2" />
  <line x1="10" y1="5" x2="80" y2="76" />
  <line x1="10" y1="19" x2="80" y2="89" />
  <line x1="10" y1="25" x2="80" y2="96" style="stroke-width:2" />

  <!-- Vertical lines -->
  <line x1="10" y1="0" x2="10" y2="25" style="stroke-width:2" />
  <line x1="12" y1="2" x2="12" y2="27" />
  <line x1="14" y1="4" x2="14" y2="30" />
  <line x1="17" y1="7" x2="17" y2="32" />
  <line x1="19" y1="9" x2="19" y2="34" />
  <line x1="21" y1="11" x2="21" y2="37" />
  <line x1="24" y1="14" x2="24" y2="39" />
  <line x1="26" y1="16" x2="26" y2="41" />
  <line x1="28" y1="18" x2="28" y2="44" />
  <line x1="31" y1="21" x2="31" y2="46" />
  <line x1="33" y1="23" x2="33" y2="48" />
  <line x1="35" y1="25" x2="35" y2="51" />
  <line x1="38" y1="28" x2="38" y2="53" />
  <line x1="40" y1="30" x2="40" y2="55" />
  <line x1="42" y1="32" x2="42" y2="58" />
  <line x1="45" y1="35" x2="45" y2="60" />
  <line x1="47" y1="37" x2="47" y2="63" />
  <line x1="49" y1="39" x2="49" y2="65" />
  <line x1="52" y1="42" x2="52" y2="67" />
  <line x1="54" y1="44" x2="54" y2="70" />
  <line x1="57" y1="47" x2="57" y2="72" />
  <line x1="59" y1="49" x2="59" y2="74" />
  <line x1="61" y1="51" x2="61" y2="77" />
  <line x1="64" y1="54" x2="64" y2="79" />
  <line x1="66" y1="56" x2="66" y2="81" />
  <line x1="68" y1="58" x2="68" y2="84" />
  <line x1="71" y1="61" x2="71" y2="86" />
  <line x1="73" y1="63" x2="73" y2="88" />
  <line x1="75" y1="65" x2="75" y2="91" />
  <line x1="78" y1="68" x2="78" y2="93" />
  <line x1="80" y1="70" x2="80" y2="95" />
  <line x1="80" y1="70" x2="80" y2="96" style="stroke-width:2" />

  <!-- Colored Rectangle -->
  <polygon points="10.000000,0.000000 80.588235,70.588235 80.588235,96.000852 10.000000,25.412617" style="fill:#ECB172A0;stroke-width:0"/>

  <!-- Horizontal lines -->
  <line x1="10" y1="0" x2="35" y2="0" style="stroke-width:2" />
  <line x1="12" y1="2" x2="37" y2="2" />
  <line x1="14" y1="4" x2="40" y2="4" />
  <line x1="17" y1="7" x2="42" y2="7" />
  <line x1="19" y1="9" x2="44" y2="9" />
  <line x1="21" y1="11" x2="47" y2="11" />
  <line x1="24" y1="14" x2="49" y2="14" />
  <line x1="26" y1="16" x2="51" y2="16" />
  <line x1="28" y1="18" x2="54" y2="18" />
  <line x1="31" y1="21" x2="56" y2="21" />
  <line x1="33" y1="23" x2="58" y2="23" />
  <line x1="35" y1="25" x2="61" y2="25" />
  <line x1="38" y1="28" x2="63" y2="28" />
  <line x1="40" y1="30" x2="65" y2="30" />
  <line x1="42" y1="32" x2="68" y2="32" />
  <line x1="45" y1="35" x2="70" y2="35" />
  <line x1="47" y1="37" x2="73" y2="37" />
  <line x1="49" y1="39" x2="75" y2="39" />
  <line x1="52" y1="42" x2="77" y2="42" />
  <line x1="54" y1="44" x2="80" y2="44" />
  <line x1="57" y1="47" x2="82" y2="47" />
  <line x1="59" y1="49" x2="84" y2="49" />
  <line x1="61" y1="51" x2="87" y2="51" />
  <line x1="64" y1="54" x2="89" y2="54" />
  <line x1="66" y1="56" x2="91" y2="56" />
  <line x1="68" y1="58" x2="94" y2="58" />
  <line x1="71" y1="61" x2="96" y2="61" />
  <line x1="73" y1="63" x2="98" y2="63" />
  <line x1="75" y1="65" x2="101" y2="65" />
  <line x1="78" y1="68" x2="103" y2="68" />
  <line x1="80" y1="70" x2="105" y2="70" />
  <line x1="80" y1="70" x2="106" y2="70" style="stroke-width:2" />

  <!-- Vertical lines -->
  <line x1="10" y1="0" x2="80" y2="70" style="stroke-width:2" />
  <line x1="13" y1="0" x2="83" y2="70" />
  <line x1="20" y1="0" x2="91" y2="70" />
  <line x1="28" y1="0" x2="99" y2="70" />
  <line x1="35" y1="0" x2="106" y2="70" style="stroke-width:2" />

  <!-- Colored Rectangle -->
  <polygon points="10.000000,0.000000 35.412617,0.000000 106.000852,70.588235 80.588235,70.588235" style="fill:#ECB172A0;stroke-width:0"/>

  <!-- Horizontal lines -->
  <line x1="80" y1="70" x2="106" y2="70" style="stroke-width:2" />
  <line x1="80" y1="76" x2="106" y2="76" />
  <line x1="80" y1="89" x2="106" y2="89" />
  <line x1="80" y1="96" x2="106" y2="96" style="stroke-width:2" />

  <!-- Vertical lines -->
  <line x1="80" y1="70" x2="80" y2="96" style="stroke-width:2" />
  <line x1="83" y1="70" x2="83" y2="96" />
  <line x1="91" y1="70" x2="91" y2="96" />
  <line x1="99" y1="70" x2="99" y2="96" />
  <line x1="106" y1="70" x2="106" y2="96" style="stroke-width:2" />

  <!-- Colored Rectangle -->
  <polygon points="80.588235,70.588235 106.000852,70.588235 106.000852,96.000852 80.588235,96.000852" style="fill:#ECB172A0;stroke-width:0"/>

  <!-- Text -->
  <text x="93.294544" y="116.000852" font-size="1.0rem" font-weight="100" text-anchor="middle" >81</text>
  <text x="126.000852" y="83.294544" font-size="1.0rem" font-weight="100" text-anchor="middle" transform="rotate(0,126.000852,83.294544)">46</text>
  <text x="35.294118" y="80.706734" font-size="1.0rem" font-weight="100" text-anchor="middle" transform="rotate(45,35.294118,80.706734)">262968</text>
</svg>
</td>
</tr>
</table></pre></li><li class='xr-var-item'><div class='xr-var-name'><span>smlt</span></div><div class='xr-var-dims'>(time, latitude, longitude)</div><div class='xr-var-dtype'>float64</div><div class='xr-var-preview xr-preview'>dask.array&lt;chunksize=(8760, 10, 10), meta=np.ndarray&gt;</div><input id='attrs-7647b0e2-ad39-46c2-9278-1bfff5779874' class='xr-var-attrs-in' type='checkbox' disabled><label for='attrs-7647b0e2-ad39-46c2-9278-1bfff5779874' title='Show/Hide attributes'><svg class='icon xr-icon-file-text2'><use xlink:href='#icon-file-text2'></use></svg></label><input id='data-c738fb75-876a-475c-b6c9-a402f9d2be33' class='xr-var-data-in' type='checkbox'><label for='data-c738fb75-876a-475c-b6c9-a402f9d2be33' title='Show/Hide data repr'><svg class='icon xr-icon-database'><use xlink:href='#icon-database'></use></svg></label><div class='xr-var-attrs'><dl class='xr-attrs'></dl></div><pre class='xr-var-data'><table>
<tr>
<td>
<table>
  <thead>
    <tr><td> </td><th> Array </th><th> Chunk </th></tr>
  </thead>
  <tbody>
    <tr><th> Bytes </th><td> 7.84 GB </td> <td> 43.80 MB </td></tr>
    <tr><th> Shape </th><td> (262968, 46, 81) </td> <td> (8760, 25, 25) </td></tr>
    <tr><th> Count </th><td> 7573 Tasks </td><td> 372 Chunks </td></tr>
    <tr><th> Type </th><td> float64 </td><td> numpy.ndarray </td></tr>
  </tbody>
</table>
</td>
<td>
<svg width="156" height="146" style="stroke:rgb(0,0,0);stroke-width:1" >

  <!-- Horizontal lines -->
  <line x1="10" y1="0" x2="80" y2="70" style="stroke-width:2" />
  <line x1="10" y1="5" x2="80" y2="76" />
  <line x1="10" y1="19" x2="80" y2="89" />
  <line x1="10" y1="25" x2="80" y2="96" style="stroke-width:2" />

  <!-- Vertical lines -->
  <line x1="10" y1="0" x2="10" y2="25" style="stroke-width:2" />
  <line x1="12" y1="2" x2="12" y2="27" />
  <line x1="14" y1="4" x2="14" y2="30" />
  <line x1="17" y1="7" x2="17" y2="32" />
  <line x1="19" y1="9" x2="19" y2="34" />
  <line x1="21" y1="11" x2="21" y2="37" />
  <line x1="24" y1="14" x2="24" y2="39" />
  <line x1="26" y1="16" x2="26" y2="41" />
  <line x1="28" y1="18" x2="28" y2="44" />
  <line x1="31" y1="21" x2="31" y2="46" />
  <line x1="33" y1="23" x2="33" y2="48" />
  <line x1="35" y1="25" x2="35" y2="51" />
  <line x1="38" y1="28" x2="38" y2="53" />
  <line x1="40" y1="30" x2="40" y2="55" />
  <line x1="42" y1="32" x2="42" y2="58" />
  <line x1="45" y1="35" x2="45" y2="60" />
  <line x1="47" y1="37" x2="47" y2="63" />
  <line x1="49" y1="39" x2="49" y2="65" />
  <line x1="52" y1="42" x2="52" y2="67" />
  <line x1="54" y1="44" x2="54" y2="70" />
  <line x1="57" y1="47" x2="57" y2="72" />
  <line x1="59" y1="49" x2="59" y2="74" />
  <line x1="61" y1="51" x2="61" y2="77" />
  <line x1="64" y1="54" x2="64" y2="79" />
  <line x1="66" y1="56" x2="66" y2="81" />
  <line x1="68" y1="58" x2="68" y2="84" />
  <line x1="71" y1="61" x2="71" y2="86" />
  <line x1="73" y1="63" x2="73" y2="88" />
  <line x1="75" y1="65" x2="75" y2="91" />
  <line x1="78" y1="68" x2="78" y2="93" />
  <line x1="80" y1="70" x2="80" y2="95" />
  <line x1="80" y1="70" x2="80" y2="96" style="stroke-width:2" />

  <!-- Colored Rectangle -->
  <polygon points="10.000000,0.000000 80.588235,70.588235 80.588235,96.000852 10.000000,25.412617" style="fill:#ECB172A0;stroke-width:0"/>

  <!-- Horizontal lines -->
  <line x1="10" y1="0" x2="35" y2="0" style="stroke-width:2" />
  <line x1="12" y1="2" x2="37" y2="2" />
  <line x1="14" y1="4" x2="40" y2="4" />
  <line x1="17" y1="7" x2="42" y2="7" />
  <line x1="19" y1="9" x2="44" y2="9" />
  <line x1="21" y1="11" x2="47" y2="11" />
  <line x1="24" y1="14" x2="49" y2="14" />
  <line x1="26" y1="16" x2="51" y2="16" />
  <line x1="28" y1="18" x2="54" y2="18" />
  <line x1="31" y1="21" x2="56" y2="21" />
  <line x1="33" y1="23" x2="58" y2="23" />
  <line x1="35" y1="25" x2="61" y2="25" />
  <line x1="38" y1="28" x2="63" y2="28" />
  <line x1="40" y1="30" x2="65" y2="30" />
  <line x1="42" y1="32" x2="68" y2="32" />
  <line x1="45" y1="35" x2="70" y2="35" />
  <line x1="47" y1="37" x2="73" y2="37" />
  <line x1="49" y1="39" x2="75" y2="39" />
  <line x1="52" y1="42" x2="77" y2="42" />
  <line x1="54" y1="44" x2="80" y2="44" />
  <line x1="57" y1="47" x2="82" y2="47" />
  <line x1="59" y1="49" x2="84" y2="49" />
  <line x1="61" y1="51" x2="87" y2="51" />
  <line x1="64" y1="54" x2="89" y2="54" />
  <line x1="66" y1="56" x2="91" y2="56" />
  <line x1="68" y1="58" x2="94" y2="58" />
  <line x1="71" y1="61" x2="96" y2="61" />
  <line x1="73" y1="63" x2="98" y2="63" />
  <line x1="75" y1="65" x2="101" y2="65" />
  <line x1="78" y1="68" x2="103" y2="68" />
  <line x1="80" y1="70" x2="105" y2="70" />
  <line x1="80" y1="70" x2="106" y2="70" style="stroke-width:2" />

  <!-- Vertical lines -->
  <line x1="10" y1="0" x2="80" y2="70" style="stroke-width:2" />
  <line x1="13" y1="0" x2="83" y2="70" />
  <line x1="20" y1="0" x2="91" y2="70" />
  <line x1="28" y1="0" x2="99" y2="70" />
  <line x1="35" y1="0" x2="106" y2="70" style="stroke-width:2" />

  <!-- Colored Rectangle -->
  <polygon points="10.000000,0.000000 35.412617,0.000000 106.000852,70.588235 80.588235,70.588235" style="fill:#ECB172A0;stroke-width:0"/>

  <!-- Horizontal lines -->
  <line x1="80" y1="70" x2="106" y2="70" style="stroke-width:2" />
  <line x1="80" y1="76" x2="106" y2="76" />
  <line x1="80" y1="89" x2="106" y2="89" />
  <line x1="80" y1="96" x2="106" y2="96" style="stroke-width:2" />

  <!-- Vertical lines -->
  <line x1="80" y1="70" x2="80" y2="96" style="stroke-width:2" />
  <line x1="83" y1="70" x2="83" y2="96" />
  <line x1="91" y1="70" x2="91" y2="96" />
  <line x1="99" y1="70" x2="99" y2="96" />
  <line x1="106" y1="70" x2="106" y2="96" style="stroke-width:2" />

  <!-- Colored Rectangle -->
  <polygon points="80.588235,70.588235 106.000852,70.588235 106.000852,96.000852 80.588235,96.000852" style="fill:#ECB172A0;stroke-width:0"/>

  <!-- Text -->
  <text x="93.294544" y="116.000852" font-size="1.0rem" font-weight="100" text-anchor="middle" >81</text>
  <text x="126.000852" y="83.294544" font-size="1.0rem" font-weight="100" text-anchor="middle" transform="rotate(0,126.000852,83.294544)">46</text>
  <text x="35.294118" y="80.706734" font-size="1.0rem" font-weight="100" text-anchor="middle" transform="rotate(45,35.294118,80.706734)">262968</text>
</svg>
</td>
</tr>
</table></pre></li><li class='xr-var-item'><div class='xr-var-name'><span>snowc</span></div><div class='xr-var-dims'>(time, latitude, longitude)</div><div class='xr-var-dtype'>float64</div><div class='xr-var-preview xr-preview'>dask.array&lt;chunksize=(8760, 10, 10), meta=np.ndarray&gt;</div><input id='attrs-3dcf9785-a4c4-4891-9b71-90c12e9869ea' class='xr-var-attrs-in' type='checkbox' disabled><label for='attrs-3dcf9785-a4c4-4891-9b71-90c12e9869ea' title='Show/Hide attributes'><svg class='icon xr-icon-file-text2'><use xlink:href='#icon-file-text2'></use></svg></label><input id='data-cb40de63-9b1a-4aea-bb4f-563fa569844e' class='xr-var-data-in' type='checkbox'><label for='data-cb40de63-9b1a-4aea-bb4f-563fa569844e' title='Show/Hide data repr'><svg class='icon xr-icon-database'><use xlink:href='#icon-database'></use></svg></label><div class='xr-var-attrs'><dl class='xr-attrs'></dl></div><pre class='xr-var-data'><table>
<tr>
<td>
<table>
  <thead>
    <tr><td> </td><th> Array </th><th> Chunk </th></tr>
  </thead>
  <tbody>
    <tr><th> Bytes </th><td> 7.84 GB </td> <td> 43.80 MB </td></tr>
    <tr><th> Shape </th><td> (262968, 46, 81) </td> <td> (8760, 25, 25) </td></tr>
    <tr><th> Count </th><td> 7573 Tasks </td><td> 372 Chunks </td></tr>
    <tr><th> Type </th><td> float64 </td><td> numpy.ndarray </td></tr>
  </tbody>
</table>
</td>
<td>
<svg width="156" height="146" style="stroke:rgb(0,0,0);stroke-width:1" >

  <!-- Horizontal lines -->
  <line x1="10" y1="0" x2="80" y2="70" style="stroke-width:2" />
  <line x1="10" y1="5" x2="80" y2="76" />
  <line x1="10" y1="19" x2="80" y2="89" />
  <line x1="10" y1="25" x2="80" y2="96" style="stroke-width:2" />

  <!-- Vertical lines -->
  <line x1="10" y1="0" x2="10" y2="25" style="stroke-width:2" />
  <line x1="12" y1="2" x2="12" y2="27" />
  <line x1="14" y1="4" x2="14" y2="30" />
  <line x1="17" y1="7" x2="17" y2="32" />
  <line x1="19" y1="9" x2="19" y2="34" />
  <line x1="21" y1="11" x2="21" y2="37" />
  <line x1="24" y1="14" x2="24" y2="39" />
  <line x1="26" y1="16" x2="26" y2="41" />
  <line x1="28" y1="18" x2="28" y2="44" />
  <line x1="31" y1="21" x2="31" y2="46" />
  <line x1="33" y1="23" x2="33" y2="48" />
  <line x1="35" y1="25" x2="35" y2="51" />
  <line x1="38" y1="28" x2="38" y2="53" />
  <line x1="40" y1="30" x2="40" y2="55" />
  <line x1="42" y1="32" x2="42" y2="58" />
  <line x1="45" y1="35" x2="45" y2="60" />
  <line x1="47" y1="37" x2="47" y2="63" />
  <line x1="49" y1="39" x2="49" y2="65" />
  <line x1="52" y1="42" x2="52" y2="67" />
  <line x1="54" y1="44" x2="54" y2="70" />
  <line x1="57" y1="47" x2="57" y2="72" />
  <line x1="59" y1="49" x2="59" y2="74" />
  <line x1="61" y1="51" x2="61" y2="77" />
  <line x1="64" y1="54" x2="64" y2="79" />
  <line x1="66" y1="56" x2="66" y2="81" />
  <line x1="68" y1="58" x2="68" y2="84" />
  <line x1="71" y1="61" x2="71" y2="86" />
  <line x1="73" y1="63" x2="73" y2="88" />
  <line x1="75" y1="65" x2="75" y2="91" />
  <line x1="78" y1="68" x2="78" y2="93" />
  <line x1="80" y1="70" x2="80" y2="95" />
  <line x1="80" y1="70" x2="80" y2="96" style="stroke-width:2" />

  <!-- Colored Rectangle -->
  <polygon points="10.000000,0.000000 80.588235,70.588235 80.588235,96.000852 10.000000,25.412617" style="fill:#ECB172A0;stroke-width:0"/>

  <!-- Horizontal lines -->
  <line x1="10" y1="0" x2="35" y2="0" style="stroke-width:2" />
  <line x1="12" y1="2" x2="37" y2="2" />
  <line x1="14" y1="4" x2="40" y2="4" />
  <line x1="17" y1="7" x2="42" y2="7" />
  <line x1="19" y1="9" x2="44" y2="9" />
  <line x1="21" y1="11" x2="47" y2="11" />
  <line x1="24" y1="14" x2="49" y2="14" />
  <line x1="26" y1="16" x2="51" y2="16" />
  <line x1="28" y1="18" x2="54" y2="18" />
  <line x1="31" y1="21" x2="56" y2="21" />
  <line x1="33" y1="23" x2="58" y2="23" />
  <line x1="35" y1="25" x2="61" y2="25" />
  <line x1="38" y1="28" x2="63" y2="28" />
  <line x1="40" y1="30" x2="65" y2="30" />
  <line x1="42" y1="32" x2="68" y2="32" />
  <line x1="45" y1="35" x2="70" y2="35" />
  <line x1="47" y1="37" x2="73" y2="37" />
  <line x1="49" y1="39" x2="75" y2="39" />
  <line x1="52" y1="42" x2="77" y2="42" />
  <line x1="54" y1="44" x2="80" y2="44" />
  <line x1="57" y1="47" x2="82" y2="47" />
  <line x1="59" y1="49" x2="84" y2="49" />
  <line x1="61" y1="51" x2="87" y2="51" />
  <line x1="64" y1="54" x2="89" y2="54" />
  <line x1="66" y1="56" x2="91" y2="56" />
  <line x1="68" y1="58" x2="94" y2="58" />
  <line x1="71" y1="61" x2="96" y2="61" />
  <line x1="73" y1="63" x2="98" y2="63" />
  <line x1="75" y1="65" x2="101" y2="65" />
  <line x1="78" y1="68" x2="103" y2="68" />
  <line x1="80" y1="70" x2="105" y2="70" />
  <line x1="80" y1="70" x2="106" y2="70" style="stroke-width:2" />

  <!-- Vertical lines -->
  <line x1="10" y1="0" x2="80" y2="70" style="stroke-width:2" />
  <line x1="13" y1="0" x2="83" y2="70" />
  <line x1="20" y1="0" x2="91" y2="70" />
  <line x1="28" y1="0" x2="99" y2="70" />
  <line x1="35" y1="0" x2="106" y2="70" style="stroke-width:2" />

  <!-- Colored Rectangle -->
  <polygon points="10.000000,0.000000 35.412617,0.000000 106.000852,70.588235 80.588235,70.588235" style="fill:#ECB172A0;stroke-width:0"/>

  <!-- Horizontal lines -->
  <line x1="80" y1="70" x2="106" y2="70" style="stroke-width:2" />
  <line x1="80" y1="76" x2="106" y2="76" />
  <line x1="80" y1="89" x2="106" y2="89" />
  <line x1="80" y1="96" x2="106" y2="96" style="stroke-width:2" />

  <!-- Vertical lines -->
  <line x1="80" y1="70" x2="80" y2="96" style="stroke-width:2" />
  <line x1="83" y1="70" x2="83" y2="96" />
  <line x1="91" y1="70" x2="91" y2="96" />
  <line x1="99" y1="70" x2="99" y2="96" />
  <line x1="106" y1="70" x2="106" y2="96" style="stroke-width:2" />

  <!-- Colored Rectangle -->
  <polygon points="80.588235,70.588235 106.000852,70.588235 106.000852,96.000852 80.588235,96.000852" style="fill:#ECB172A0;stroke-width:0"/>

  <!-- Text -->
  <text x="93.294544" y="116.000852" font-size="1.0rem" font-weight="100" text-anchor="middle" >81</text>
  <text x="126.000852" y="83.294544" font-size="1.0rem" font-weight="100" text-anchor="middle" transform="rotate(0,126.000852,83.294544)">46</text>
  <text x="35.294118" y="80.706734" font-size="1.0rem" font-weight="100" text-anchor="middle" transform="rotate(45,35.294118,80.706734)">262968</text>
</svg>
</td>
</tr>
</table></pre></li><li class='xr-var-item'><div class='xr-var-name'><span>sro</span></div><div class='xr-var-dims'>(time, latitude, longitude)</div><div class='xr-var-dtype'>float64</div><div class='xr-var-preview xr-preview'>dask.array&lt;chunksize=(8760, 10, 10), meta=np.ndarray&gt;</div><input id='attrs-03b9cf74-da6f-4300-9252-d5c7b700006c' class='xr-var-attrs-in' type='checkbox' disabled><label for='attrs-03b9cf74-da6f-4300-9252-d5c7b700006c' title='Show/Hide attributes'><svg class='icon xr-icon-file-text2'><use xlink:href='#icon-file-text2'></use></svg></label><input id='data-897a9171-b834-4656-86c7-9c74e7ac4b2a' class='xr-var-data-in' type='checkbox'><label for='data-897a9171-b834-4656-86c7-9c74e7ac4b2a' title='Show/Hide data repr'><svg class='icon xr-icon-database'><use xlink:href='#icon-database'></use></svg></label><div class='xr-var-attrs'><dl class='xr-attrs'></dl></div><pre class='xr-var-data'><table>
<tr>
<td>
<table>
  <thead>
    <tr><td> </td><th> Array </th><th> Chunk </th></tr>
  </thead>
  <tbody>
    <tr><th> Bytes </th><td> 7.84 GB </td> <td> 43.80 MB </td></tr>
    <tr><th> Shape </th><td> (262968, 46, 81) </td> <td> (8760, 25, 25) </td></tr>
    <tr><th> Count </th><td> 7573 Tasks </td><td> 372 Chunks </td></tr>
    <tr><th> Type </th><td> float64 </td><td> numpy.ndarray </td></tr>
  </tbody>
</table>
</td>
<td>
<svg width="156" height="146" style="stroke:rgb(0,0,0);stroke-width:1" >

  <!-- Horizontal lines -->
  <line x1="10" y1="0" x2="80" y2="70" style="stroke-width:2" />
  <line x1="10" y1="5" x2="80" y2="76" />
  <line x1="10" y1="19" x2="80" y2="89" />
  <line x1="10" y1="25" x2="80" y2="96" style="stroke-width:2" />

  <!-- Vertical lines -->
  <line x1="10" y1="0" x2="10" y2="25" style="stroke-width:2" />
  <line x1="12" y1="2" x2="12" y2="27" />
  <line x1="14" y1="4" x2="14" y2="30" />
  <line x1="17" y1="7" x2="17" y2="32" />
  <line x1="19" y1="9" x2="19" y2="34" />
  <line x1="21" y1="11" x2="21" y2="37" />
  <line x1="24" y1="14" x2="24" y2="39" />
  <line x1="26" y1="16" x2="26" y2="41" />
  <line x1="28" y1="18" x2="28" y2="44" />
  <line x1="31" y1="21" x2="31" y2="46" />
  <line x1="33" y1="23" x2="33" y2="48" />
  <line x1="35" y1="25" x2="35" y2="51" />
  <line x1="38" y1="28" x2="38" y2="53" />
  <line x1="40" y1="30" x2="40" y2="55" />
  <line x1="42" y1="32" x2="42" y2="58" />
  <line x1="45" y1="35" x2="45" y2="60" />
  <line x1="47" y1="37" x2="47" y2="63" />
  <line x1="49" y1="39" x2="49" y2="65" />
  <line x1="52" y1="42" x2="52" y2="67" />
  <line x1="54" y1="44" x2="54" y2="70" />
  <line x1="57" y1="47" x2="57" y2="72" />
  <line x1="59" y1="49" x2="59" y2="74" />
  <line x1="61" y1="51" x2="61" y2="77" />
  <line x1="64" y1="54" x2="64" y2="79" />
  <line x1="66" y1="56" x2="66" y2="81" />
  <line x1="68" y1="58" x2="68" y2="84" />
  <line x1="71" y1="61" x2="71" y2="86" />
  <line x1="73" y1="63" x2="73" y2="88" />
  <line x1="75" y1="65" x2="75" y2="91" />
  <line x1="78" y1="68" x2="78" y2="93" />
  <line x1="80" y1="70" x2="80" y2="95" />
  <line x1="80" y1="70" x2="80" y2="96" style="stroke-width:2" />

  <!-- Colored Rectangle -->
  <polygon points="10.000000,0.000000 80.588235,70.588235 80.588235,96.000852 10.000000,25.412617" style="fill:#ECB172A0;stroke-width:0"/>

  <!-- Horizontal lines -->
  <line x1="10" y1="0" x2="35" y2="0" style="stroke-width:2" />
  <line x1="12" y1="2" x2="37" y2="2" />
  <line x1="14" y1="4" x2="40" y2="4" />
  <line x1="17" y1="7" x2="42" y2="7" />
  <line x1="19" y1="9" x2="44" y2="9" />
  <line x1="21" y1="11" x2="47" y2="11" />
  <line x1="24" y1="14" x2="49" y2="14" />
  <line x1="26" y1="16" x2="51" y2="16" />
  <line x1="28" y1="18" x2="54" y2="18" />
  <line x1="31" y1="21" x2="56" y2="21" />
  <line x1="33" y1="23" x2="58" y2="23" />
  <line x1="35" y1="25" x2="61" y2="25" />
  <line x1="38" y1="28" x2="63" y2="28" />
  <line x1="40" y1="30" x2="65" y2="30" />
  <line x1="42" y1="32" x2="68" y2="32" />
  <line x1="45" y1="35" x2="70" y2="35" />
  <line x1="47" y1="37" x2="73" y2="37" />
  <line x1="49" y1="39" x2="75" y2="39" />
  <line x1="52" y1="42" x2="77" y2="42" />
  <line x1="54" y1="44" x2="80" y2="44" />
  <line x1="57" y1="47" x2="82" y2="47" />
  <line x1="59" y1="49" x2="84" y2="49" />
  <line x1="61" y1="51" x2="87" y2="51" />
  <line x1="64" y1="54" x2="89" y2="54" />
  <line x1="66" y1="56" x2="91" y2="56" />
  <line x1="68" y1="58" x2="94" y2="58" />
  <line x1="71" y1="61" x2="96" y2="61" />
  <line x1="73" y1="63" x2="98" y2="63" />
  <line x1="75" y1="65" x2="101" y2="65" />
  <line x1="78" y1="68" x2="103" y2="68" />
  <line x1="80" y1="70" x2="105" y2="70" />
  <line x1="80" y1="70" x2="106" y2="70" style="stroke-width:2" />

  <!-- Vertical lines -->
  <line x1="10" y1="0" x2="80" y2="70" style="stroke-width:2" />
  <line x1="13" y1="0" x2="83" y2="70" />
  <line x1="20" y1="0" x2="91" y2="70" />
  <line x1="28" y1="0" x2="99" y2="70" />
  <line x1="35" y1="0" x2="106" y2="70" style="stroke-width:2" />

  <!-- Colored Rectangle -->
  <polygon points="10.000000,0.000000 35.412617,0.000000 106.000852,70.588235 80.588235,70.588235" style="fill:#ECB172A0;stroke-width:0"/>

  <!-- Horizontal lines -->
  <line x1="80" y1="70" x2="106" y2="70" style="stroke-width:2" />
  <line x1="80" y1="76" x2="106" y2="76" />
  <line x1="80" y1="89" x2="106" y2="89" />
  <line x1="80" y1="96" x2="106" y2="96" style="stroke-width:2" />

  <!-- Vertical lines -->
  <line x1="80" y1="70" x2="80" y2="96" style="stroke-width:2" />
  <line x1="83" y1="70" x2="83" y2="96" />
  <line x1="91" y1="70" x2="91" y2="96" />
  <line x1="99" y1="70" x2="99" y2="96" />
  <line x1="106" y1="70" x2="106" y2="96" style="stroke-width:2" />

  <!-- Colored Rectangle -->
  <polygon points="80.588235,70.588235 106.000852,70.588235 106.000852,96.000852 80.588235,96.000852" style="fill:#ECB172A0;stroke-width:0"/>

  <!-- Text -->
  <text x="93.294544" y="116.000852" font-size="1.0rem" font-weight="100" text-anchor="middle" >81</text>
  <text x="126.000852" y="83.294544" font-size="1.0rem" font-weight="100" text-anchor="middle" transform="rotate(0,126.000852,83.294544)">46</text>
  <text x="35.294118" y="80.706734" font-size="1.0rem" font-weight="100" text-anchor="middle" transform="rotate(45,35.294118,80.706734)">262968</text>
</svg>
</td>
</tr>
</table></pre></li><li class='xr-var-item'><div class='xr-var-name'><span>ssr</span></div><div class='xr-var-dims'>(time, latitude, longitude)</div><div class='xr-var-dtype'>float64</div><div class='xr-var-preview xr-preview'>dask.array&lt;chunksize=(8760, 10, 10), meta=np.ndarray&gt;</div><input id='attrs-17bdade7-7fd5-4867-99d1-216d8bda34d0' class='xr-var-attrs-in' type='checkbox' disabled><label for='attrs-17bdade7-7fd5-4867-99d1-216d8bda34d0' title='Show/Hide attributes'><svg class='icon xr-icon-file-text2'><use xlink:href='#icon-file-text2'></use></svg></label><input id='data-204a6c65-36a2-42ee-ad5a-8ee182d096db' class='xr-var-data-in' type='checkbox'><label for='data-204a6c65-36a2-42ee-ad5a-8ee182d096db' title='Show/Hide data repr'><svg class='icon xr-icon-database'><use xlink:href='#icon-database'></use></svg></label><div class='xr-var-attrs'><dl class='xr-attrs'></dl></div><pre class='xr-var-data'><table>
<tr>
<td>
<table>
  <thead>
    <tr><td> </td><th> Array </th><th> Chunk </th></tr>
  </thead>
  <tbody>
    <tr><th> Bytes </th><td> 7.84 GB </td> <td> 43.80 MB </td></tr>
    <tr><th> Shape </th><td> (262968, 46, 81) </td> <td> (8760, 25, 25) </td></tr>
    <tr><th> Count </th><td> 7573 Tasks </td><td> 372 Chunks </td></tr>
    <tr><th> Type </th><td> float64 </td><td> numpy.ndarray </td></tr>
  </tbody>
</table>
</td>
<td>
<svg width="156" height="146" style="stroke:rgb(0,0,0);stroke-width:1" >

  <!-- Horizontal lines -->
  <line x1="10" y1="0" x2="80" y2="70" style="stroke-width:2" />
  <line x1="10" y1="5" x2="80" y2="76" />
  <line x1="10" y1="19" x2="80" y2="89" />
  <line x1="10" y1="25" x2="80" y2="96" style="stroke-width:2" />

  <!-- Vertical lines -->
  <line x1="10" y1="0" x2="10" y2="25" style="stroke-width:2" />
  <line x1="12" y1="2" x2="12" y2="27" />
  <line x1="14" y1="4" x2="14" y2="30" />
  <line x1="17" y1="7" x2="17" y2="32" />
  <line x1="19" y1="9" x2="19" y2="34" />
  <line x1="21" y1="11" x2="21" y2="37" />
  <line x1="24" y1="14" x2="24" y2="39" />
  <line x1="26" y1="16" x2="26" y2="41" />
  <line x1="28" y1="18" x2="28" y2="44" />
  <line x1="31" y1="21" x2="31" y2="46" />
  <line x1="33" y1="23" x2="33" y2="48" />
  <line x1="35" y1="25" x2="35" y2="51" />
  <line x1="38" y1="28" x2="38" y2="53" />
  <line x1="40" y1="30" x2="40" y2="55" />
  <line x1="42" y1="32" x2="42" y2="58" />
  <line x1="45" y1="35" x2="45" y2="60" />
  <line x1="47" y1="37" x2="47" y2="63" />
  <line x1="49" y1="39" x2="49" y2="65" />
  <line x1="52" y1="42" x2="52" y2="67" />
  <line x1="54" y1="44" x2="54" y2="70" />
  <line x1="57" y1="47" x2="57" y2="72" />
  <line x1="59" y1="49" x2="59" y2="74" />
  <line x1="61" y1="51" x2="61" y2="77" />
  <line x1="64" y1="54" x2="64" y2="79" />
  <line x1="66" y1="56" x2="66" y2="81" />
  <line x1="68" y1="58" x2="68" y2="84" />
  <line x1="71" y1="61" x2="71" y2="86" />
  <line x1="73" y1="63" x2="73" y2="88" />
  <line x1="75" y1="65" x2="75" y2="91" />
  <line x1="78" y1="68" x2="78" y2="93" />
  <line x1="80" y1="70" x2="80" y2="95" />
  <line x1="80" y1="70" x2="80" y2="96" style="stroke-width:2" />

  <!-- Colored Rectangle -->
  <polygon points="10.000000,0.000000 80.588235,70.588235 80.588235,96.000852 10.000000,25.412617" style="fill:#ECB172A0;stroke-width:0"/>

  <!-- Horizontal lines -->
  <line x1="10" y1="0" x2="35" y2="0" style="stroke-width:2" />
  <line x1="12" y1="2" x2="37" y2="2" />
  <line x1="14" y1="4" x2="40" y2="4" />
  <line x1="17" y1="7" x2="42" y2="7" />
  <line x1="19" y1="9" x2="44" y2="9" />
  <line x1="21" y1="11" x2="47" y2="11" />
  <line x1="24" y1="14" x2="49" y2="14" />
  <line x1="26" y1="16" x2="51" y2="16" />
  <line x1="28" y1="18" x2="54" y2="18" />
  <line x1="31" y1="21" x2="56" y2="21" />
  <line x1="33" y1="23" x2="58" y2="23" />
  <line x1="35" y1="25" x2="61" y2="25" />
  <line x1="38" y1="28" x2="63" y2="28" />
  <line x1="40" y1="30" x2="65" y2="30" />
  <line x1="42" y1="32" x2="68" y2="32" />
  <line x1="45" y1="35" x2="70" y2="35" />
  <line x1="47" y1="37" x2="73" y2="37" />
  <line x1="49" y1="39" x2="75" y2="39" />
  <line x1="52" y1="42" x2="77" y2="42" />
  <line x1="54" y1="44" x2="80" y2="44" />
  <line x1="57" y1="47" x2="82" y2="47" />
  <line x1="59" y1="49" x2="84" y2="49" />
  <line x1="61" y1="51" x2="87" y2="51" />
  <line x1="64" y1="54" x2="89" y2="54" />
  <line x1="66" y1="56" x2="91" y2="56" />
  <line x1="68" y1="58" x2="94" y2="58" />
  <line x1="71" y1="61" x2="96" y2="61" />
  <line x1="73" y1="63" x2="98" y2="63" />
  <line x1="75" y1="65" x2="101" y2="65" />
  <line x1="78" y1="68" x2="103" y2="68" />
  <line x1="80" y1="70" x2="105" y2="70" />
  <line x1="80" y1="70" x2="106" y2="70" style="stroke-width:2" />

  <!-- Vertical lines -->
  <line x1="10" y1="0" x2="80" y2="70" style="stroke-width:2" />
  <line x1="13" y1="0" x2="83" y2="70" />
  <line x1="20" y1="0" x2="91" y2="70" />
  <line x1="28" y1="0" x2="99" y2="70" />
  <line x1="35" y1="0" x2="106" y2="70" style="stroke-width:2" />

  <!-- Colored Rectangle -->
  <polygon points="10.000000,0.000000 35.412617,0.000000 106.000852,70.588235 80.588235,70.588235" style="fill:#ECB172A0;stroke-width:0"/>

  <!-- Horizontal lines -->
  <line x1="80" y1="70" x2="106" y2="70" style="stroke-width:2" />
  <line x1="80" y1="76" x2="106" y2="76" />
  <line x1="80" y1="89" x2="106" y2="89" />
  <line x1="80" y1="96" x2="106" y2="96" style="stroke-width:2" />

  <!-- Vertical lines -->
  <line x1="80" y1="70" x2="80" y2="96" style="stroke-width:2" />
  <line x1="83" y1="70" x2="83" y2="96" />
  <line x1="91" y1="70" x2="91" y2="96" />
  <line x1="99" y1="70" x2="99" y2="96" />
  <line x1="106" y1="70" x2="106" y2="96" style="stroke-width:2" />

  <!-- Colored Rectangle -->
  <polygon points="80.588235,70.588235 106.000852,70.588235 106.000852,96.000852 80.588235,96.000852" style="fill:#ECB172A0;stroke-width:0"/>

  <!-- Text -->
  <text x="93.294544" y="116.000852" font-size="1.0rem" font-weight="100" text-anchor="middle" >81</text>
  <text x="126.000852" y="83.294544" font-size="1.0rem" font-weight="100" text-anchor="middle" transform="rotate(0,126.000852,83.294544)">46</text>
  <text x="35.294118" y="80.706734" font-size="1.0rem" font-weight="100" text-anchor="middle" transform="rotate(45,35.294118,80.706734)">262968</text>
</svg>
</td>
</tr>
</table></pre></li><li class='xr-var-item'><div class='xr-var-name'><span>swvl1</span></div><div class='xr-var-dims'>(time, latitude, longitude)</div><div class='xr-var-dtype'>float64</div><div class='xr-var-preview xr-preview'>dask.array&lt;chunksize=(8760, 10, 10), meta=np.ndarray&gt;</div><input id='attrs-c722ae97-7ba5-4a05-8ca1-d6f135fe88ea' class='xr-var-attrs-in' type='checkbox' disabled><label for='attrs-c722ae97-7ba5-4a05-8ca1-d6f135fe88ea' title='Show/Hide attributes'><svg class='icon xr-icon-file-text2'><use xlink:href='#icon-file-text2'></use></svg></label><input id='data-8c34990f-c795-43d6-befe-d57445403489' class='xr-var-data-in' type='checkbox'><label for='data-8c34990f-c795-43d6-befe-d57445403489' title='Show/Hide data repr'><svg class='icon xr-icon-database'><use xlink:href='#icon-database'></use></svg></label><div class='xr-var-attrs'><dl class='xr-attrs'></dl></div><pre class='xr-var-data'><table>
<tr>
<td>
<table>
  <thead>
    <tr><td> </td><th> Array </th><th> Chunk </th></tr>
  </thead>
  <tbody>
    <tr><th> Bytes </th><td> 7.84 GB </td> <td> 43.80 MB </td></tr>
    <tr><th> Shape </th><td> (262968, 46, 81) </td> <td> (8760, 25, 25) </td></tr>
    <tr><th> Count </th><td> 7573 Tasks </td><td> 372 Chunks </td></tr>
    <tr><th> Type </th><td> float64 </td><td> numpy.ndarray </td></tr>
  </tbody>
</table>
</td>
<td>
<svg width="156" height="146" style="stroke:rgb(0,0,0);stroke-width:1" >

  <!-- Horizontal lines -->
  <line x1="10" y1="0" x2="80" y2="70" style="stroke-width:2" />
  <line x1="10" y1="5" x2="80" y2="76" />
  <line x1="10" y1="19" x2="80" y2="89" />
  <line x1="10" y1="25" x2="80" y2="96" style="stroke-width:2" />

  <!-- Vertical lines -->
  <line x1="10" y1="0" x2="10" y2="25" style="stroke-width:2" />
  <line x1="12" y1="2" x2="12" y2="27" />
  <line x1="14" y1="4" x2="14" y2="30" />
  <line x1="17" y1="7" x2="17" y2="32" />
  <line x1="19" y1="9" x2="19" y2="34" />
  <line x1="21" y1="11" x2="21" y2="37" />
  <line x1="24" y1="14" x2="24" y2="39" />
  <line x1="26" y1="16" x2="26" y2="41" />
  <line x1="28" y1="18" x2="28" y2="44" />
  <line x1="31" y1="21" x2="31" y2="46" />
  <line x1="33" y1="23" x2="33" y2="48" />
  <line x1="35" y1="25" x2="35" y2="51" />
  <line x1="38" y1="28" x2="38" y2="53" />
  <line x1="40" y1="30" x2="40" y2="55" />
  <line x1="42" y1="32" x2="42" y2="58" />
  <line x1="45" y1="35" x2="45" y2="60" />
  <line x1="47" y1="37" x2="47" y2="63" />
  <line x1="49" y1="39" x2="49" y2="65" />
  <line x1="52" y1="42" x2="52" y2="67" />
  <line x1="54" y1="44" x2="54" y2="70" />
  <line x1="57" y1="47" x2="57" y2="72" />
  <line x1="59" y1="49" x2="59" y2="74" />
  <line x1="61" y1="51" x2="61" y2="77" />
  <line x1="64" y1="54" x2="64" y2="79" />
  <line x1="66" y1="56" x2="66" y2="81" />
  <line x1="68" y1="58" x2="68" y2="84" />
  <line x1="71" y1="61" x2="71" y2="86" />
  <line x1="73" y1="63" x2="73" y2="88" />
  <line x1="75" y1="65" x2="75" y2="91" />
  <line x1="78" y1="68" x2="78" y2="93" />
  <line x1="80" y1="70" x2="80" y2="95" />
  <line x1="80" y1="70" x2="80" y2="96" style="stroke-width:2" />

  <!-- Colored Rectangle -->
  <polygon points="10.000000,0.000000 80.588235,70.588235 80.588235,96.000852 10.000000,25.412617" style="fill:#ECB172A0;stroke-width:0"/>

  <!-- Horizontal lines -->
  <line x1="10" y1="0" x2="35" y2="0" style="stroke-width:2" />
  <line x1="12" y1="2" x2="37" y2="2" />
  <line x1="14" y1="4" x2="40" y2="4" />
  <line x1="17" y1="7" x2="42" y2="7" />
  <line x1="19" y1="9" x2="44" y2="9" />
  <line x1="21" y1="11" x2="47" y2="11" />
  <line x1="24" y1="14" x2="49" y2="14" />
  <line x1="26" y1="16" x2="51" y2="16" />
  <line x1="28" y1="18" x2="54" y2="18" />
  <line x1="31" y1="21" x2="56" y2="21" />
  <line x1="33" y1="23" x2="58" y2="23" />
  <line x1="35" y1="25" x2="61" y2="25" />
  <line x1="38" y1="28" x2="63" y2="28" />
  <line x1="40" y1="30" x2="65" y2="30" />
  <line x1="42" y1="32" x2="68" y2="32" />
  <line x1="45" y1="35" x2="70" y2="35" />
  <line x1="47" y1="37" x2="73" y2="37" />
  <line x1="49" y1="39" x2="75" y2="39" />
  <line x1="52" y1="42" x2="77" y2="42" />
  <line x1="54" y1="44" x2="80" y2="44" />
  <line x1="57" y1="47" x2="82" y2="47" />
  <line x1="59" y1="49" x2="84" y2="49" />
  <line x1="61" y1="51" x2="87" y2="51" />
  <line x1="64" y1="54" x2="89" y2="54" />
  <line x1="66" y1="56" x2="91" y2="56" />
  <line x1="68" y1="58" x2="94" y2="58" />
  <line x1="71" y1="61" x2="96" y2="61" />
  <line x1="73" y1="63" x2="98" y2="63" />
  <line x1="75" y1="65" x2="101" y2="65" />
  <line x1="78" y1="68" x2="103" y2="68" />
  <line x1="80" y1="70" x2="105" y2="70" />
  <line x1="80" y1="70" x2="106" y2="70" style="stroke-width:2" />

  <!-- Vertical lines -->
  <line x1="10" y1="0" x2="80" y2="70" style="stroke-width:2" />
  <line x1="13" y1="0" x2="83" y2="70" />
  <line x1="20" y1="0" x2="91" y2="70" />
  <line x1="28" y1="0" x2="99" y2="70" />
  <line x1="35" y1="0" x2="106" y2="70" style="stroke-width:2" />

  <!-- Colored Rectangle -->
  <polygon points="10.000000,0.000000 35.412617,0.000000 106.000852,70.588235 80.588235,70.588235" style="fill:#ECB172A0;stroke-width:0"/>

  <!-- Horizontal lines -->
  <line x1="80" y1="70" x2="106" y2="70" style="stroke-width:2" />
  <line x1="80" y1="76" x2="106" y2="76" />
  <line x1="80" y1="89" x2="106" y2="89" />
  <line x1="80" y1="96" x2="106" y2="96" style="stroke-width:2" />

  <!-- Vertical lines -->
  <line x1="80" y1="70" x2="80" y2="96" style="stroke-width:2" />
  <line x1="83" y1="70" x2="83" y2="96" />
  <line x1="91" y1="70" x2="91" y2="96" />
  <line x1="99" y1="70" x2="99" y2="96" />
  <line x1="106" y1="70" x2="106" y2="96" style="stroke-width:2" />

  <!-- Colored Rectangle -->
  <polygon points="80.588235,70.588235 106.000852,70.588235 106.000852,96.000852 80.588235,96.000852" style="fill:#ECB172A0;stroke-width:0"/>

  <!-- Text -->
  <text x="93.294544" y="116.000852" font-size="1.0rem" font-weight="100" text-anchor="middle" >81</text>
  <text x="126.000852" y="83.294544" font-size="1.0rem" font-weight="100" text-anchor="middle" transform="rotate(0,126.000852,83.294544)">46</text>
  <text x="35.294118" y="80.706734" font-size="1.0rem" font-weight="100" text-anchor="middle" transform="rotate(45,35.294118,80.706734)">262968</text>
</svg>
</td>
</tr>
</table></pre></li><li class='xr-var-item'><div class='xr-var-name'><span>swvl2</span></div><div class='xr-var-dims'>(time, latitude, longitude)</div><div class='xr-var-dtype'>float64</div><div class='xr-var-preview xr-preview'>dask.array&lt;chunksize=(8760, 10, 10), meta=np.ndarray&gt;</div><input id='attrs-3d883225-f76c-40b1-900d-d6b56a76b1e7' class='xr-var-attrs-in' type='checkbox' disabled><label for='attrs-3d883225-f76c-40b1-900d-d6b56a76b1e7' title='Show/Hide attributes'><svg class='icon xr-icon-file-text2'><use xlink:href='#icon-file-text2'></use></svg></label><input id='data-adf6d45f-3bec-4e17-abb1-18ebcdf8ae99' class='xr-var-data-in' type='checkbox'><label for='data-adf6d45f-3bec-4e17-abb1-18ebcdf8ae99' title='Show/Hide data repr'><svg class='icon xr-icon-database'><use xlink:href='#icon-database'></use></svg></label><div class='xr-var-attrs'><dl class='xr-attrs'></dl></div><pre class='xr-var-data'><table>
<tr>
<td>
<table>
  <thead>
    <tr><td> </td><th> Array </th><th> Chunk </th></tr>
  </thead>
  <tbody>
    <tr><th> Bytes </th><td> 7.84 GB </td> <td> 43.80 MB </td></tr>
    <tr><th> Shape </th><td> (262968, 46, 81) </td> <td> (8760, 25, 25) </td></tr>
    <tr><th> Count </th><td> 7573 Tasks </td><td> 372 Chunks </td></tr>
    <tr><th> Type </th><td> float64 </td><td> numpy.ndarray </td></tr>
  </tbody>
</table>
</td>
<td>
<svg width="156" height="146" style="stroke:rgb(0,0,0);stroke-width:1" >

  <!-- Horizontal lines -->
  <line x1="10" y1="0" x2="80" y2="70" style="stroke-width:2" />
  <line x1="10" y1="5" x2="80" y2="76" />
  <line x1="10" y1="19" x2="80" y2="89" />
  <line x1="10" y1="25" x2="80" y2="96" style="stroke-width:2" />

  <!-- Vertical lines -->
  <line x1="10" y1="0" x2="10" y2="25" style="stroke-width:2" />
  <line x1="12" y1="2" x2="12" y2="27" />
  <line x1="14" y1="4" x2="14" y2="30" />
  <line x1="17" y1="7" x2="17" y2="32" />
  <line x1="19" y1="9" x2="19" y2="34" />
  <line x1="21" y1="11" x2="21" y2="37" />
  <line x1="24" y1="14" x2="24" y2="39" />
  <line x1="26" y1="16" x2="26" y2="41" />
  <line x1="28" y1="18" x2="28" y2="44" />
  <line x1="31" y1="21" x2="31" y2="46" />
  <line x1="33" y1="23" x2="33" y2="48" />
  <line x1="35" y1="25" x2="35" y2="51" />
  <line x1="38" y1="28" x2="38" y2="53" />
  <line x1="40" y1="30" x2="40" y2="55" />
  <line x1="42" y1="32" x2="42" y2="58" />
  <line x1="45" y1="35" x2="45" y2="60" />
  <line x1="47" y1="37" x2="47" y2="63" />
  <line x1="49" y1="39" x2="49" y2="65" />
  <line x1="52" y1="42" x2="52" y2="67" />
  <line x1="54" y1="44" x2="54" y2="70" />
  <line x1="57" y1="47" x2="57" y2="72" />
  <line x1="59" y1="49" x2="59" y2="74" />
  <line x1="61" y1="51" x2="61" y2="77" />
  <line x1="64" y1="54" x2="64" y2="79" />
  <line x1="66" y1="56" x2="66" y2="81" />
  <line x1="68" y1="58" x2="68" y2="84" />
  <line x1="71" y1="61" x2="71" y2="86" />
  <line x1="73" y1="63" x2="73" y2="88" />
  <line x1="75" y1="65" x2="75" y2="91" />
  <line x1="78" y1="68" x2="78" y2="93" />
  <line x1="80" y1="70" x2="80" y2="95" />
  <line x1="80" y1="70" x2="80" y2="96" style="stroke-width:2" />

  <!-- Colored Rectangle -->
  <polygon points="10.000000,0.000000 80.588235,70.588235 80.588235,96.000852 10.000000,25.412617" style="fill:#ECB172A0;stroke-width:0"/>

  <!-- Horizontal lines -->
  <line x1="10" y1="0" x2="35" y2="0" style="stroke-width:2" />
  <line x1="12" y1="2" x2="37" y2="2" />
  <line x1="14" y1="4" x2="40" y2="4" />
  <line x1="17" y1="7" x2="42" y2="7" />
  <line x1="19" y1="9" x2="44" y2="9" />
  <line x1="21" y1="11" x2="47" y2="11" />
  <line x1="24" y1="14" x2="49" y2="14" />
  <line x1="26" y1="16" x2="51" y2="16" />
  <line x1="28" y1="18" x2="54" y2="18" />
  <line x1="31" y1="21" x2="56" y2="21" />
  <line x1="33" y1="23" x2="58" y2="23" />
  <line x1="35" y1="25" x2="61" y2="25" />
  <line x1="38" y1="28" x2="63" y2="28" />
  <line x1="40" y1="30" x2="65" y2="30" />
  <line x1="42" y1="32" x2="68" y2="32" />
  <line x1="45" y1="35" x2="70" y2="35" />
  <line x1="47" y1="37" x2="73" y2="37" />
  <line x1="49" y1="39" x2="75" y2="39" />
  <line x1="52" y1="42" x2="77" y2="42" />
  <line x1="54" y1="44" x2="80" y2="44" />
  <line x1="57" y1="47" x2="82" y2="47" />
  <line x1="59" y1="49" x2="84" y2="49" />
  <line x1="61" y1="51" x2="87" y2="51" />
  <line x1="64" y1="54" x2="89" y2="54" />
  <line x1="66" y1="56" x2="91" y2="56" />
  <line x1="68" y1="58" x2="94" y2="58" />
  <line x1="71" y1="61" x2="96" y2="61" />
  <line x1="73" y1="63" x2="98" y2="63" />
  <line x1="75" y1="65" x2="101" y2="65" />
  <line x1="78" y1="68" x2="103" y2="68" />
  <line x1="80" y1="70" x2="105" y2="70" />
  <line x1="80" y1="70" x2="106" y2="70" style="stroke-width:2" />

  <!-- Vertical lines -->
  <line x1="10" y1="0" x2="80" y2="70" style="stroke-width:2" />
  <line x1="13" y1="0" x2="83" y2="70" />
  <line x1="20" y1="0" x2="91" y2="70" />
  <line x1="28" y1="0" x2="99" y2="70" />
  <line x1="35" y1="0" x2="106" y2="70" style="stroke-width:2" />

  <!-- Colored Rectangle -->
  <polygon points="10.000000,0.000000 35.412617,0.000000 106.000852,70.588235 80.588235,70.588235" style="fill:#ECB172A0;stroke-width:0"/>

  <!-- Horizontal lines -->
  <line x1="80" y1="70" x2="106" y2="70" style="stroke-width:2" />
  <line x1="80" y1="76" x2="106" y2="76" />
  <line x1="80" y1="89" x2="106" y2="89" />
  <line x1="80" y1="96" x2="106" y2="96" style="stroke-width:2" />

  <!-- Vertical lines -->
  <line x1="80" y1="70" x2="80" y2="96" style="stroke-width:2" />
  <line x1="83" y1="70" x2="83" y2="96" />
  <line x1="91" y1="70" x2="91" y2="96" />
  <line x1="99" y1="70" x2="99" y2="96" />
  <line x1="106" y1="70" x2="106" y2="96" style="stroke-width:2" />

  <!-- Colored Rectangle -->
  <polygon points="80.588235,70.588235 106.000852,70.588235 106.000852,96.000852 80.588235,96.000852" style="fill:#ECB172A0;stroke-width:0"/>

  <!-- Text -->
  <text x="93.294544" y="116.000852" font-size="1.0rem" font-weight="100" text-anchor="middle" >81</text>
  <text x="126.000852" y="83.294544" font-size="1.0rem" font-weight="100" text-anchor="middle" transform="rotate(0,126.000852,83.294544)">46</text>
  <text x="35.294118" y="80.706734" font-size="1.0rem" font-weight="100" text-anchor="middle" transform="rotate(45,35.294118,80.706734)">262968</text>
</svg>
</td>
</tr>
</table></pre></li><li class='xr-var-item'><div class='xr-var-name'><span>swvl3</span></div><div class='xr-var-dims'>(time, latitude, longitude)</div><div class='xr-var-dtype'>float64</div><div class='xr-var-preview xr-preview'>dask.array&lt;chunksize=(8760, 10, 10), meta=np.ndarray&gt;</div><input id='attrs-5d4ae8ff-0f9d-48f7-9e81-d77f19a97caa' class='xr-var-attrs-in' type='checkbox' disabled><label for='attrs-5d4ae8ff-0f9d-48f7-9e81-d77f19a97caa' title='Show/Hide attributes'><svg class='icon xr-icon-file-text2'><use xlink:href='#icon-file-text2'></use></svg></label><input id='data-bbe92c7f-4698-4334-8793-fde30515c74a' class='xr-var-data-in' type='checkbox'><label for='data-bbe92c7f-4698-4334-8793-fde30515c74a' title='Show/Hide data repr'><svg class='icon xr-icon-database'><use xlink:href='#icon-database'></use></svg></label><div class='xr-var-attrs'><dl class='xr-attrs'></dl></div><pre class='xr-var-data'><table>
<tr>
<td>
<table>
  <thead>
    <tr><td> </td><th> Array </th><th> Chunk </th></tr>
  </thead>
  <tbody>
    <tr><th> Bytes </th><td> 7.84 GB </td> <td> 43.80 MB </td></tr>
    <tr><th> Shape </th><td> (262968, 46, 81) </td> <td> (8760, 25, 25) </td></tr>
    <tr><th> Count </th><td> 7573 Tasks </td><td> 372 Chunks </td></tr>
    <tr><th> Type </th><td> float64 </td><td> numpy.ndarray </td></tr>
  </tbody>
</table>
</td>
<td>
<svg width="156" height="146" style="stroke:rgb(0,0,0);stroke-width:1" >

  <!-- Horizontal lines -->
  <line x1="10" y1="0" x2="80" y2="70" style="stroke-width:2" />
  <line x1="10" y1="5" x2="80" y2="76" />
  <line x1="10" y1="19" x2="80" y2="89" />
  <line x1="10" y1="25" x2="80" y2="96" style="stroke-width:2" />

  <!-- Vertical lines -->
  <line x1="10" y1="0" x2="10" y2="25" style="stroke-width:2" />
  <line x1="12" y1="2" x2="12" y2="27" />
  <line x1="14" y1="4" x2="14" y2="30" />
  <line x1="17" y1="7" x2="17" y2="32" />
  <line x1="19" y1="9" x2="19" y2="34" />
  <line x1="21" y1="11" x2="21" y2="37" />
  <line x1="24" y1="14" x2="24" y2="39" />
  <line x1="26" y1="16" x2="26" y2="41" />
  <line x1="28" y1="18" x2="28" y2="44" />
  <line x1="31" y1="21" x2="31" y2="46" />
  <line x1="33" y1="23" x2="33" y2="48" />
  <line x1="35" y1="25" x2="35" y2="51" />
  <line x1="38" y1="28" x2="38" y2="53" />
  <line x1="40" y1="30" x2="40" y2="55" />
  <line x1="42" y1="32" x2="42" y2="58" />
  <line x1="45" y1="35" x2="45" y2="60" />
  <line x1="47" y1="37" x2="47" y2="63" />
  <line x1="49" y1="39" x2="49" y2="65" />
  <line x1="52" y1="42" x2="52" y2="67" />
  <line x1="54" y1="44" x2="54" y2="70" />
  <line x1="57" y1="47" x2="57" y2="72" />
  <line x1="59" y1="49" x2="59" y2="74" />
  <line x1="61" y1="51" x2="61" y2="77" />
  <line x1="64" y1="54" x2="64" y2="79" />
  <line x1="66" y1="56" x2="66" y2="81" />
  <line x1="68" y1="58" x2="68" y2="84" />
  <line x1="71" y1="61" x2="71" y2="86" />
  <line x1="73" y1="63" x2="73" y2="88" />
  <line x1="75" y1="65" x2="75" y2="91" />
  <line x1="78" y1="68" x2="78" y2="93" />
  <line x1="80" y1="70" x2="80" y2="95" />
  <line x1="80" y1="70" x2="80" y2="96" style="stroke-width:2" />

  <!-- Colored Rectangle -->
  <polygon points="10.000000,0.000000 80.588235,70.588235 80.588235,96.000852 10.000000,25.412617" style="fill:#ECB172A0;stroke-width:0"/>

  <!-- Horizontal lines -->
  <line x1="10" y1="0" x2="35" y2="0" style="stroke-width:2" />
  <line x1="12" y1="2" x2="37" y2="2" />
  <line x1="14" y1="4" x2="40" y2="4" />
  <line x1="17" y1="7" x2="42" y2="7" />
  <line x1="19" y1="9" x2="44" y2="9" />
  <line x1="21" y1="11" x2="47" y2="11" />
  <line x1="24" y1="14" x2="49" y2="14" />
  <line x1="26" y1="16" x2="51" y2="16" />
  <line x1="28" y1="18" x2="54" y2="18" />
  <line x1="31" y1="21" x2="56" y2="21" />
  <line x1="33" y1="23" x2="58" y2="23" />
  <line x1="35" y1="25" x2="61" y2="25" />
  <line x1="38" y1="28" x2="63" y2="28" />
  <line x1="40" y1="30" x2="65" y2="30" />
  <line x1="42" y1="32" x2="68" y2="32" />
  <line x1="45" y1="35" x2="70" y2="35" />
  <line x1="47" y1="37" x2="73" y2="37" />
  <line x1="49" y1="39" x2="75" y2="39" />
  <line x1="52" y1="42" x2="77" y2="42" />
  <line x1="54" y1="44" x2="80" y2="44" />
  <line x1="57" y1="47" x2="82" y2="47" />
  <line x1="59" y1="49" x2="84" y2="49" />
  <line x1="61" y1="51" x2="87" y2="51" />
  <line x1="64" y1="54" x2="89" y2="54" />
  <line x1="66" y1="56" x2="91" y2="56" />
  <line x1="68" y1="58" x2="94" y2="58" />
  <line x1="71" y1="61" x2="96" y2="61" />
  <line x1="73" y1="63" x2="98" y2="63" />
  <line x1="75" y1="65" x2="101" y2="65" />
  <line x1="78" y1="68" x2="103" y2="68" />
  <line x1="80" y1="70" x2="105" y2="70" />
  <line x1="80" y1="70" x2="106" y2="70" style="stroke-width:2" />

  <!-- Vertical lines -->
  <line x1="10" y1="0" x2="80" y2="70" style="stroke-width:2" />
  <line x1="13" y1="0" x2="83" y2="70" />
  <line x1="20" y1="0" x2="91" y2="70" />
  <line x1="28" y1="0" x2="99" y2="70" />
  <line x1="35" y1="0" x2="106" y2="70" style="stroke-width:2" />

  <!-- Colored Rectangle -->
  <polygon points="10.000000,0.000000 35.412617,0.000000 106.000852,70.588235 80.588235,70.588235" style="fill:#ECB172A0;stroke-width:0"/>

  <!-- Horizontal lines -->
  <line x1="80" y1="70" x2="106" y2="70" style="stroke-width:2" />
  <line x1="80" y1="76" x2="106" y2="76" />
  <line x1="80" y1="89" x2="106" y2="89" />
  <line x1="80" y1="96" x2="106" y2="96" style="stroke-width:2" />

  <!-- Vertical lines -->
  <line x1="80" y1="70" x2="80" y2="96" style="stroke-width:2" />
  <line x1="83" y1="70" x2="83" y2="96" />
  <line x1="91" y1="70" x2="91" y2="96" />
  <line x1="99" y1="70" x2="99" y2="96" />
  <line x1="106" y1="70" x2="106" y2="96" style="stroke-width:2" />

  <!-- Colored Rectangle -->
  <polygon points="80.588235,70.588235 106.000852,70.588235 106.000852,96.000852 80.588235,96.000852" style="fill:#ECB172A0;stroke-width:0"/>

  <!-- Text -->
  <text x="93.294544" y="116.000852" font-size="1.0rem" font-weight="100" text-anchor="middle" >81</text>
  <text x="126.000852" y="83.294544" font-size="1.0rem" font-weight="100" text-anchor="middle" transform="rotate(0,126.000852,83.294544)">46</text>
  <text x="35.294118" y="80.706734" font-size="1.0rem" font-weight="100" text-anchor="middle" transform="rotate(45,35.294118,80.706734)">262968</text>
</svg>
</td>
</tr>
</table></pre></li><li class='xr-var-item'><div class='xr-var-name'><span>t2m</span></div><div class='xr-var-dims'>(time, latitude, longitude)</div><div class='xr-var-dtype'>float64</div><div class='xr-var-preview xr-preview'>dask.array&lt;chunksize=(8760, 10, 10), meta=np.ndarray&gt;</div><input id='attrs-be8b8b51-c464-4398-8f4c-e379f6eba5d7' class='xr-var-attrs-in' type='checkbox' disabled><label for='attrs-be8b8b51-c464-4398-8f4c-e379f6eba5d7' title='Show/Hide attributes'><svg class='icon xr-icon-file-text2'><use xlink:href='#icon-file-text2'></use></svg></label><input id='data-60cd06e9-b8f4-4dca-af12-8462c260848c' class='xr-var-data-in' type='checkbox'><label for='data-60cd06e9-b8f4-4dca-af12-8462c260848c' title='Show/Hide data repr'><svg class='icon xr-icon-database'><use xlink:href='#icon-database'></use></svg></label><div class='xr-var-attrs'><dl class='xr-attrs'></dl></div><pre class='xr-var-data'><table>
<tr>
<td>
<table>
  <thead>
    <tr><td> </td><th> Array </th><th> Chunk </th></tr>
  </thead>
  <tbody>
    <tr><th> Bytes </th><td> 7.84 GB </td> <td> 43.80 MB </td></tr>
    <tr><th> Shape </th><td> (262968, 46, 81) </td> <td> (8760, 25, 25) </td></tr>
    <tr><th> Count </th><td> 7573 Tasks </td><td> 372 Chunks </td></tr>
    <tr><th> Type </th><td> float64 </td><td> numpy.ndarray </td></tr>
  </tbody>
</table>
</td>
<td>
<svg width="156" height="146" style="stroke:rgb(0,0,0);stroke-width:1" >

  <!-- Horizontal lines -->
  <line x1="10" y1="0" x2="80" y2="70" style="stroke-width:2" />
  <line x1="10" y1="5" x2="80" y2="76" />
  <line x1="10" y1="19" x2="80" y2="89" />
  <line x1="10" y1="25" x2="80" y2="96" style="stroke-width:2" />

  <!-- Vertical lines -->
  <line x1="10" y1="0" x2="10" y2="25" style="stroke-width:2" />
  <line x1="12" y1="2" x2="12" y2="27" />
  <line x1="14" y1="4" x2="14" y2="30" />
  <line x1="17" y1="7" x2="17" y2="32" />
  <line x1="19" y1="9" x2="19" y2="34" />
  <line x1="21" y1="11" x2="21" y2="37" />
  <line x1="24" y1="14" x2="24" y2="39" />
  <line x1="26" y1="16" x2="26" y2="41" />
  <line x1="28" y1="18" x2="28" y2="44" />
  <line x1="31" y1="21" x2="31" y2="46" />
  <line x1="33" y1="23" x2="33" y2="48" />
  <line x1="35" y1="25" x2="35" y2="51" />
  <line x1="38" y1="28" x2="38" y2="53" />
  <line x1="40" y1="30" x2="40" y2="55" />
  <line x1="42" y1="32" x2="42" y2="58" />
  <line x1="45" y1="35" x2="45" y2="60" />
  <line x1="47" y1="37" x2="47" y2="63" />
  <line x1="49" y1="39" x2="49" y2="65" />
  <line x1="52" y1="42" x2="52" y2="67" />
  <line x1="54" y1="44" x2="54" y2="70" />
  <line x1="57" y1="47" x2="57" y2="72" />
  <line x1="59" y1="49" x2="59" y2="74" />
  <line x1="61" y1="51" x2="61" y2="77" />
  <line x1="64" y1="54" x2="64" y2="79" />
  <line x1="66" y1="56" x2="66" y2="81" />
  <line x1="68" y1="58" x2="68" y2="84" />
  <line x1="71" y1="61" x2="71" y2="86" />
  <line x1="73" y1="63" x2="73" y2="88" />
  <line x1="75" y1="65" x2="75" y2="91" />
  <line x1="78" y1="68" x2="78" y2="93" />
  <line x1="80" y1="70" x2="80" y2="95" />
  <line x1="80" y1="70" x2="80" y2="96" style="stroke-width:2" />

  <!-- Colored Rectangle -->
  <polygon points="10.000000,0.000000 80.588235,70.588235 80.588235,96.000852 10.000000,25.412617" style="fill:#ECB172A0;stroke-width:0"/>

  <!-- Horizontal lines -->
  <line x1="10" y1="0" x2="35" y2="0" style="stroke-width:2" />
  <line x1="12" y1="2" x2="37" y2="2" />
  <line x1="14" y1="4" x2="40" y2="4" />
  <line x1="17" y1="7" x2="42" y2="7" />
  <line x1="19" y1="9" x2="44" y2="9" />
  <line x1="21" y1="11" x2="47" y2="11" />
  <line x1="24" y1="14" x2="49" y2="14" />
  <line x1="26" y1="16" x2="51" y2="16" />
  <line x1="28" y1="18" x2="54" y2="18" />
  <line x1="31" y1="21" x2="56" y2="21" />
  <line x1="33" y1="23" x2="58" y2="23" />
  <line x1="35" y1="25" x2="61" y2="25" />
  <line x1="38" y1="28" x2="63" y2="28" />
  <line x1="40" y1="30" x2="65" y2="30" />
  <line x1="42" y1="32" x2="68" y2="32" />
  <line x1="45" y1="35" x2="70" y2="35" />
  <line x1="47" y1="37" x2="73" y2="37" />
  <line x1="49" y1="39" x2="75" y2="39" />
  <line x1="52" y1="42" x2="77" y2="42" />
  <line x1="54" y1="44" x2="80" y2="44" />
  <line x1="57" y1="47" x2="82" y2="47" />
  <line x1="59" y1="49" x2="84" y2="49" />
  <line x1="61" y1="51" x2="87" y2="51" />
  <line x1="64" y1="54" x2="89" y2="54" />
  <line x1="66" y1="56" x2="91" y2="56" />
  <line x1="68" y1="58" x2="94" y2="58" />
  <line x1="71" y1="61" x2="96" y2="61" />
  <line x1="73" y1="63" x2="98" y2="63" />
  <line x1="75" y1="65" x2="101" y2="65" />
  <line x1="78" y1="68" x2="103" y2="68" />
  <line x1="80" y1="70" x2="105" y2="70" />
  <line x1="80" y1="70" x2="106" y2="70" style="stroke-width:2" />

  <!-- Vertical lines -->
  <line x1="10" y1="0" x2="80" y2="70" style="stroke-width:2" />
  <line x1="13" y1="0" x2="83" y2="70" />
  <line x1="20" y1="0" x2="91" y2="70" />
  <line x1="28" y1="0" x2="99" y2="70" />
  <line x1="35" y1="0" x2="106" y2="70" style="stroke-width:2" />

  <!-- Colored Rectangle -->
  <polygon points="10.000000,0.000000 35.412617,0.000000 106.000852,70.588235 80.588235,70.588235" style="fill:#ECB172A0;stroke-width:0"/>

  <!-- Horizontal lines -->
  <line x1="80" y1="70" x2="106" y2="70" style="stroke-width:2" />
  <line x1="80" y1="76" x2="106" y2="76" />
  <line x1="80" y1="89" x2="106" y2="89" />
  <line x1="80" y1="96" x2="106" y2="96" style="stroke-width:2" />

  <!-- Vertical lines -->
  <line x1="80" y1="70" x2="80" y2="96" style="stroke-width:2" />
  <line x1="83" y1="70" x2="83" y2="96" />
  <line x1="91" y1="70" x2="91" y2="96" />
  <line x1="99" y1="70" x2="99" y2="96" />
  <line x1="106" y1="70" x2="106" y2="96" style="stroke-width:2" />

  <!-- Colored Rectangle -->
  <polygon points="80.588235,70.588235 106.000852,70.588235 106.000852,96.000852 80.588235,96.000852" style="fill:#ECB172A0;stroke-width:0"/>

  <!-- Text -->
  <text x="93.294544" y="116.000852" font-size="1.0rem" font-weight="100" text-anchor="middle" >81</text>
  <text x="126.000852" y="83.294544" font-size="1.0rem" font-weight="100" text-anchor="middle" transform="rotate(0,126.000852,83.294544)">46</text>
  <text x="35.294118" y="80.706734" font-size="1.0rem" font-weight="100" text-anchor="middle" transform="rotate(45,35.294118,80.706734)">262968</text>
</svg>
</td>
</tr>
</table></pre></li><li class='xr-var-item'><div class='xr-var-name'><span>tp</span></div><div class='xr-var-dims'>(time, latitude, longitude)</div><div class='xr-var-dtype'>float64</div><div class='xr-var-preview xr-preview'>dask.array&lt;chunksize=(8760, 10, 10), meta=np.ndarray&gt;</div><input id='attrs-004b1b3d-51d5-4823-b87d-4477ccd59598' class='xr-var-attrs-in' type='checkbox' disabled><label for='attrs-004b1b3d-51d5-4823-b87d-4477ccd59598' title='Show/Hide attributes'><svg class='icon xr-icon-file-text2'><use xlink:href='#icon-file-text2'></use></svg></label><input id='data-a46a1d85-8134-4131-96cc-209c3668eb56' class='xr-var-data-in' type='checkbox'><label for='data-a46a1d85-8134-4131-96cc-209c3668eb56' title='Show/Hide data repr'><svg class='icon xr-icon-database'><use xlink:href='#icon-database'></use></svg></label><div class='xr-var-attrs'><dl class='xr-attrs'></dl></div><pre class='xr-var-data'><table>
<tr>
<td>
<table>
  <thead>
    <tr><td> </td><th> Array </th><th> Chunk </th></tr>
  </thead>
  <tbody>
    <tr><th> Bytes </th><td> 7.84 GB </td> <td> 43.80 MB </td></tr>
    <tr><th> Shape </th><td> (262968, 46, 81) </td> <td> (8760, 25, 25) </td></tr>
    <tr><th> Count </th><td> 7573 Tasks </td><td> 372 Chunks </td></tr>
    <tr><th> Type </th><td> float64 </td><td> numpy.ndarray </td></tr>
  </tbody>
</table>
</td>
<td>
<svg width="156" height="146" style="stroke:rgb(0,0,0);stroke-width:1" >

  <!-- Horizontal lines -->
  <line x1="10" y1="0" x2="80" y2="70" style="stroke-width:2" />
  <line x1="10" y1="5" x2="80" y2="76" />
  <line x1="10" y1="19" x2="80" y2="89" />
  <line x1="10" y1="25" x2="80" y2="96" style="stroke-width:2" />

  <!-- Vertical lines -->
  <line x1="10" y1="0" x2="10" y2="25" style="stroke-width:2" />
  <line x1="12" y1="2" x2="12" y2="27" />
  <line x1="14" y1="4" x2="14" y2="30" />
  <line x1="17" y1="7" x2="17" y2="32" />
  <line x1="19" y1="9" x2="19" y2="34" />
  <line x1="21" y1="11" x2="21" y2="37" />
  <line x1="24" y1="14" x2="24" y2="39" />
  <line x1="26" y1="16" x2="26" y2="41" />
  <line x1="28" y1="18" x2="28" y2="44" />
  <line x1="31" y1="21" x2="31" y2="46" />
  <line x1="33" y1="23" x2="33" y2="48" />
  <line x1="35" y1="25" x2="35" y2="51" />
  <line x1="38" y1="28" x2="38" y2="53" />
  <line x1="40" y1="30" x2="40" y2="55" />
  <line x1="42" y1="32" x2="42" y2="58" />
  <line x1="45" y1="35" x2="45" y2="60" />
  <line x1="47" y1="37" x2="47" y2="63" />
  <line x1="49" y1="39" x2="49" y2="65" />
  <line x1="52" y1="42" x2="52" y2="67" />
  <line x1="54" y1="44" x2="54" y2="70" />
  <line x1="57" y1="47" x2="57" y2="72" />
  <line x1="59" y1="49" x2="59" y2="74" />
  <line x1="61" y1="51" x2="61" y2="77" />
  <line x1="64" y1="54" x2="64" y2="79" />
  <line x1="66" y1="56" x2="66" y2="81" />
  <line x1="68" y1="58" x2="68" y2="84" />
  <line x1="71" y1="61" x2="71" y2="86" />
  <line x1="73" y1="63" x2="73" y2="88" />
  <line x1="75" y1="65" x2="75" y2="91" />
  <line x1="78" y1="68" x2="78" y2="93" />
  <line x1="80" y1="70" x2="80" y2="95" />
  <line x1="80" y1="70" x2="80" y2="96" style="stroke-width:2" />

  <!-- Colored Rectangle -->
  <polygon points="10.000000,0.000000 80.588235,70.588235 80.588235,96.000852 10.000000,25.412617" style="fill:#ECB172A0;stroke-width:0"/>

  <!-- Horizontal lines -->
  <line x1="10" y1="0" x2="35" y2="0" style="stroke-width:2" />
  <line x1="12" y1="2" x2="37" y2="2" />
  <line x1="14" y1="4" x2="40" y2="4" />
  <line x1="17" y1="7" x2="42" y2="7" />
  <line x1="19" y1="9" x2="44" y2="9" />
  <line x1="21" y1="11" x2="47" y2="11" />
  <line x1="24" y1="14" x2="49" y2="14" />
  <line x1="26" y1="16" x2="51" y2="16" />
  <line x1="28" y1="18" x2="54" y2="18" />
  <line x1="31" y1="21" x2="56" y2="21" />
  <line x1="33" y1="23" x2="58" y2="23" />
  <line x1="35" y1="25" x2="61" y2="25" />
  <line x1="38" y1="28" x2="63" y2="28" />
  <line x1="40" y1="30" x2="65" y2="30" />
  <line x1="42" y1="32" x2="68" y2="32" />
  <line x1="45" y1="35" x2="70" y2="35" />
  <line x1="47" y1="37" x2="73" y2="37" />
  <line x1="49" y1="39" x2="75" y2="39" />
  <line x1="52" y1="42" x2="77" y2="42" />
  <line x1="54" y1="44" x2="80" y2="44" />
  <line x1="57" y1="47" x2="82" y2="47" />
  <line x1="59" y1="49" x2="84" y2="49" />
  <line x1="61" y1="51" x2="87" y2="51" />
  <line x1="64" y1="54" x2="89" y2="54" />
  <line x1="66" y1="56" x2="91" y2="56" />
  <line x1="68" y1="58" x2="94" y2="58" />
  <line x1="71" y1="61" x2="96" y2="61" />
  <line x1="73" y1="63" x2="98" y2="63" />
  <line x1="75" y1="65" x2="101" y2="65" />
  <line x1="78" y1="68" x2="103" y2="68" />
  <line x1="80" y1="70" x2="105" y2="70" />
  <line x1="80" y1="70" x2="106" y2="70" style="stroke-width:2" />

  <!-- Vertical lines -->
  <line x1="10" y1="0" x2="80" y2="70" style="stroke-width:2" />
  <line x1="13" y1="0" x2="83" y2="70" />
  <line x1="20" y1="0" x2="91" y2="70" />
  <line x1="28" y1="0" x2="99" y2="70" />
  <line x1="35" y1="0" x2="106" y2="70" style="stroke-width:2" />

  <!-- Colored Rectangle -->
  <polygon points="10.000000,0.000000 35.412617,0.000000 106.000852,70.588235 80.588235,70.588235" style="fill:#ECB172A0;stroke-width:0"/>

  <!-- Horizontal lines -->
  <line x1="80" y1="70" x2="106" y2="70" style="stroke-width:2" />
  <line x1="80" y1="76" x2="106" y2="76" />
  <line x1="80" y1="89" x2="106" y2="89" />
  <line x1="80" y1="96" x2="106" y2="96" style="stroke-width:2" />

  <!-- Vertical lines -->
  <line x1="80" y1="70" x2="80" y2="96" style="stroke-width:2" />
  <line x1="83" y1="70" x2="83" y2="96" />
  <line x1="91" y1="70" x2="91" y2="96" />
  <line x1="99" y1="70" x2="99" y2="96" />
  <line x1="106" y1="70" x2="106" y2="96" style="stroke-width:2" />

  <!-- Colored Rectangle -->
  <polygon points="80.588235,70.588235 106.000852,70.588235 106.000852,96.000852 80.588235,96.000852" style="fill:#ECB172A0;stroke-width:0"/>

  <!-- Text -->
  <text x="93.294544" y="116.000852" font-size="1.0rem" font-weight="100" text-anchor="middle" >81</text>
  <text x="126.000852" y="83.294544" font-size="1.0rem" font-weight="100" text-anchor="middle" transform="rotate(0,126.000852,83.294544)">46</text>
  <text x="35.294118" y="80.706734" font-size="1.0rem" font-weight="100" text-anchor="middle" transform="rotate(45,35.294118,80.706734)">262968</text>
</svg>
</td>
</tr>
</table></pre></li><li class='xr-var-item'><div class='xr-var-name'><span>tsn</span></div><div class='xr-var-dims'>(time, latitude, longitude)</div><div class='xr-var-dtype'>float64</div><div class='xr-var-preview xr-preview'>dask.array&lt;chunksize=(8760, 10, 10), meta=np.ndarray&gt;</div><input id='attrs-9f8849eb-cb41-429c-af52-68919d336f3e' class='xr-var-attrs-in' type='checkbox' disabled><label for='attrs-9f8849eb-cb41-429c-af52-68919d336f3e' title='Show/Hide attributes'><svg class='icon xr-icon-file-text2'><use xlink:href='#icon-file-text2'></use></svg></label><input id='data-057dc30b-b94e-4feb-b5b6-264477a2d197' class='xr-var-data-in' type='checkbox'><label for='data-057dc30b-b94e-4feb-b5b6-264477a2d197' title='Show/Hide data repr'><svg class='icon xr-icon-database'><use xlink:href='#icon-database'></use></svg></label><div class='xr-var-attrs'><dl class='xr-attrs'></dl></div><pre class='xr-var-data'><table>
<tr>
<td>
<table>
  <thead>
    <tr><td> </td><th> Array </th><th> Chunk </th></tr>
  </thead>
  <tbody>
    <tr><th> Bytes </th><td> 7.84 GB </td> <td> 43.80 MB </td></tr>
    <tr><th> Shape </th><td> (262968, 46, 81) </td> <td> (8760, 25, 25) </td></tr>
    <tr><th> Count </th><td> 7573 Tasks </td><td> 372 Chunks </td></tr>
    <tr><th> Type </th><td> float64 </td><td> numpy.ndarray </td></tr>
  </tbody>
</table>
</td>
<td>
<svg width="156" height="146" style="stroke:rgb(0,0,0);stroke-width:1" >

  <!-- Horizontal lines -->
  <line x1="10" y1="0" x2="80" y2="70" style="stroke-width:2" />
  <line x1="10" y1="5" x2="80" y2="76" />
  <line x1="10" y1="19" x2="80" y2="89" />
  <line x1="10" y1="25" x2="80" y2="96" style="stroke-width:2" />

  <!-- Vertical lines -->
  <line x1="10" y1="0" x2="10" y2="25" style="stroke-width:2" />
  <line x1="12" y1="2" x2="12" y2="27" />
  <line x1="14" y1="4" x2="14" y2="30" />
  <line x1="17" y1="7" x2="17" y2="32" />
  <line x1="19" y1="9" x2="19" y2="34" />
  <line x1="21" y1="11" x2="21" y2="37" />
  <line x1="24" y1="14" x2="24" y2="39" />
  <line x1="26" y1="16" x2="26" y2="41" />
  <line x1="28" y1="18" x2="28" y2="44" />
  <line x1="31" y1="21" x2="31" y2="46" />
  <line x1="33" y1="23" x2="33" y2="48" />
  <line x1="35" y1="25" x2="35" y2="51" />
  <line x1="38" y1="28" x2="38" y2="53" />
  <line x1="40" y1="30" x2="40" y2="55" />
  <line x1="42" y1="32" x2="42" y2="58" />
  <line x1="45" y1="35" x2="45" y2="60" />
  <line x1="47" y1="37" x2="47" y2="63" />
  <line x1="49" y1="39" x2="49" y2="65" />
  <line x1="52" y1="42" x2="52" y2="67" />
  <line x1="54" y1="44" x2="54" y2="70" />
  <line x1="57" y1="47" x2="57" y2="72" />
  <line x1="59" y1="49" x2="59" y2="74" />
  <line x1="61" y1="51" x2="61" y2="77" />
  <line x1="64" y1="54" x2="64" y2="79" />
  <line x1="66" y1="56" x2="66" y2="81" />
  <line x1="68" y1="58" x2="68" y2="84" />
  <line x1="71" y1="61" x2="71" y2="86" />
  <line x1="73" y1="63" x2="73" y2="88" />
  <line x1="75" y1="65" x2="75" y2="91" />
  <line x1="78" y1="68" x2="78" y2="93" />
  <line x1="80" y1="70" x2="80" y2="95" />
  <line x1="80" y1="70" x2="80" y2="96" style="stroke-width:2" />

  <!-- Colored Rectangle -->
  <polygon points="10.000000,0.000000 80.588235,70.588235 80.588235,96.000852 10.000000,25.412617" style="fill:#ECB172A0;stroke-width:0"/>

  <!-- Horizontal lines -->
  <line x1="10" y1="0" x2="35" y2="0" style="stroke-width:2" />
  <line x1="12" y1="2" x2="37" y2="2" />
  <line x1="14" y1="4" x2="40" y2="4" />
  <line x1="17" y1="7" x2="42" y2="7" />
  <line x1="19" y1="9" x2="44" y2="9" />
  <line x1="21" y1="11" x2="47" y2="11" />
  <line x1="24" y1="14" x2="49" y2="14" />
  <line x1="26" y1="16" x2="51" y2="16" />
  <line x1="28" y1="18" x2="54" y2="18" />
  <line x1="31" y1="21" x2="56" y2="21" />
  <line x1="33" y1="23" x2="58" y2="23" />
  <line x1="35" y1="25" x2="61" y2="25" />
  <line x1="38" y1="28" x2="63" y2="28" />
  <line x1="40" y1="30" x2="65" y2="30" />
  <line x1="42" y1="32" x2="68" y2="32" />
  <line x1="45" y1="35" x2="70" y2="35" />
  <line x1="47" y1="37" x2="73" y2="37" />
  <line x1="49" y1="39" x2="75" y2="39" />
  <line x1="52" y1="42" x2="77" y2="42" />
  <line x1="54" y1="44" x2="80" y2="44" />
  <line x1="57" y1="47" x2="82" y2="47" />
  <line x1="59" y1="49" x2="84" y2="49" />
  <line x1="61" y1="51" x2="87" y2="51" />
  <line x1="64" y1="54" x2="89" y2="54" />
  <line x1="66" y1="56" x2="91" y2="56" />
  <line x1="68" y1="58" x2="94" y2="58" />
  <line x1="71" y1="61" x2="96" y2="61" />
  <line x1="73" y1="63" x2="98" y2="63" />
  <line x1="75" y1="65" x2="101" y2="65" />
  <line x1="78" y1="68" x2="103" y2="68" />
  <line x1="80" y1="70" x2="105" y2="70" />
  <line x1="80" y1="70" x2="106" y2="70" style="stroke-width:2" />

  <!-- Vertical lines -->
  <line x1="10" y1="0" x2="80" y2="70" style="stroke-width:2" />
  <line x1="13" y1="0" x2="83" y2="70" />
  <line x1="20" y1="0" x2="91" y2="70" />
  <line x1="28" y1="0" x2="99" y2="70" />
  <line x1="35" y1="0" x2="106" y2="70" style="stroke-width:2" />

  <!-- Colored Rectangle -->
  <polygon points="10.000000,0.000000 35.412617,0.000000 106.000852,70.588235 80.588235,70.588235" style="fill:#ECB172A0;stroke-width:0"/>

  <!-- Horizontal lines -->
  <line x1="80" y1="70" x2="106" y2="70" style="stroke-width:2" />
  <line x1="80" y1="76" x2="106" y2="76" />
  <line x1="80" y1="89" x2="106" y2="89" />
  <line x1="80" y1="96" x2="106" y2="96" style="stroke-width:2" />

  <!-- Vertical lines -->
  <line x1="80" y1="70" x2="80" y2="96" style="stroke-width:2" />
  <line x1="83" y1="70" x2="83" y2="96" />
  <line x1="91" y1="70" x2="91" y2="96" />
  <line x1="99" y1="70" x2="99" y2="96" />
  <line x1="106" y1="70" x2="106" y2="96" style="stroke-width:2" />

  <!-- Colored Rectangle -->
  <polygon points="80.588235,70.588235 106.000852,70.588235 106.000852,96.000852 80.588235,96.000852" style="fill:#ECB172A0;stroke-width:0"/>

  <!-- Text -->
  <text x="93.294544" y="116.000852" font-size="1.0rem" font-weight="100" text-anchor="middle" >81</text>
  <text x="126.000852" y="83.294544" font-size="1.0rem" font-weight="100" text-anchor="middle" transform="rotate(0,126.000852,83.294544)">46</text>
  <text x="35.294118" y="80.706734" font-size="1.0rem" font-weight="100" text-anchor="middle" transform="rotate(45,35.294118,80.706734)">262968</text>
</svg>
</td>
</tr>
</table></pre></li><li class='xr-var-item'><div class='xr-var-name'><span>u10</span></div><div class='xr-var-dims'>(time, latitude, longitude)</div><div class='xr-var-dtype'>float64</div><div class='xr-var-preview xr-preview'>dask.array&lt;chunksize=(8760, 10, 10), meta=np.ndarray&gt;</div><input id='attrs-43127828-13c0-466a-8401-36cb11f888c7' class='xr-var-attrs-in' type='checkbox' disabled><label for='attrs-43127828-13c0-466a-8401-36cb11f888c7' title='Show/Hide attributes'><svg class='icon xr-icon-file-text2'><use xlink:href='#icon-file-text2'></use></svg></label><input id='data-2263fe78-5936-4410-86df-637b973439d6' class='xr-var-data-in' type='checkbox'><label for='data-2263fe78-5936-4410-86df-637b973439d6' title='Show/Hide data repr'><svg class='icon xr-icon-database'><use xlink:href='#icon-database'></use></svg></label><div class='xr-var-attrs'><dl class='xr-attrs'></dl></div><pre class='xr-var-data'><table>
<tr>
<td>
<table>
  <thead>
    <tr><td> </td><th> Array </th><th> Chunk </th></tr>
  </thead>
  <tbody>
    <tr><th> Bytes </th><td> 7.84 GB </td> <td> 43.80 MB </td></tr>
    <tr><th> Shape </th><td> (262968, 46, 81) </td> <td> (8760, 25, 25) </td></tr>
    <tr><th> Count </th><td> 7573 Tasks </td><td> 372 Chunks </td></tr>
    <tr><th> Type </th><td> float64 </td><td> numpy.ndarray </td></tr>
  </tbody>
</table>
</td>
<td>
<svg width="156" height="146" style="stroke:rgb(0,0,0);stroke-width:1" >

  <!-- Horizontal lines -->
  <line x1="10" y1="0" x2="80" y2="70" style="stroke-width:2" />
  <line x1="10" y1="5" x2="80" y2="76" />
  <line x1="10" y1="19" x2="80" y2="89" />
  <line x1="10" y1="25" x2="80" y2="96" style="stroke-width:2" />

  <!-- Vertical lines -->
  <line x1="10" y1="0" x2="10" y2="25" style="stroke-width:2" />
  <line x1="12" y1="2" x2="12" y2="27" />
  <line x1="14" y1="4" x2="14" y2="30" />
  <line x1="17" y1="7" x2="17" y2="32" />
  <line x1="19" y1="9" x2="19" y2="34" />
  <line x1="21" y1="11" x2="21" y2="37" />
  <line x1="24" y1="14" x2="24" y2="39" />
  <line x1="26" y1="16" x2="26" y2="41" />
  <line x1="28" y1="18" x2="28" y2="44" />
  <line x1="31" y1="21" x2="31" y2="46" />
  <line x1="33" y1="23" x2="33" y2="48" />
  <line x1="35" y1="25" x2="35" y2="51" />
  <line x1="38" y1="28" x2="38" y2="53" />
  <line x1="40" y1="30" x2="40" y2="55" />
  <line x1="42" y1="32" x2="42" y2="58" />
  <line x1="45" y1="35" x2="45" y2="60" />
  <line x1="47" y1="37" x2="47" y2="63" />
  <line x1="49" y1="39" x2="49" y2="65" />
  <line x1="52" y1="42" x2="52" y2="67" />
  <line x1="54" y1="44" x2="54" y2="70" />
  <line x1="57" y1="47" x2="57" y2="72" />
  <line x1="59" y1="49" x2="59" y2="74" />
  <line x1="61" y1="51" x2="61" y2="77" />
  <line x1="64" y1="54" x2="64" y2="79" />
  <line x1="66" y1="56" x2="66" y2="81" />
  <line x1="68" y1="58" x2="68" y2="84" />
  <line x1="71" y1="61" x2="71" y2="86" />
  <line x1="73" y1="63" x2="73" y2="88" />
  <line x1="75" y1="65" x2="75" y2="91" />
  <line x1="78" y1="68" x2="78" y2="93" />
  <line x1="80" y1="70" x2="80" y2="95" />
  <line x1="80" y1="70" x2="80" y2="96" style="stroke-width:2" />

  <!-- Colored Rectangle -->
  <polygon points="10.000000,0.000000 80.588235,70.588235 80.588235,96.000852 10.000000,25.412617" style="fill:#ECB172A0;stroke-width:0"/>

  <!-- Horizontal lines -->
  <line x1="10" y1="0" x2="35" y2="0" style="stroke-width:2" />
  <line x1="12" y1="2" x2="37" y2="2" />
  <line x1="14" y1="4" x2="40" y2="4" />
  <line x1="17" y1="7" x2="42" y2="7" />
  <line x1="19" y1="9" x2="44" y2="9" />
  <line x1="21" y1="11" x2="47" y2="11" />
  <line x1="24" y1="14" x2="49" y2="14" />
  <line x1="26" y1="16" x2="51" y2="16" />
  <line x1="28" y1="18" x2="54" y2="18" />
  <line x1="31" y1="21" x2="56" y2="21" />
  <line x1="33" y1="23" x2="58" y2="23" />
  <line x1="35" y1="25" x2="61" y2="25" />
  <line x1="38" y1="28" x2="63" y2="28" />
  <line x1="40" y1="30" x2="65" y2="30" />
  <line x1="42" y1="32" x2="68" y2="32" />
  <line x1="45" y1="35" x2="70" y2="35" />
  <line x1="47" y1="37" x2="73" y2="37" />
  <line x1="49" y1="39" x2="75" y2="39" />
  <line x1="52" y1="42" x2="77" y2="42" />
  <line x1="54" y1="44" x2="80" y2="44" />
  <line x1="57" y1="47" x2="82" y2="47" />
  <line x1="59" y1="49" x2="84" y2="49" />
  <line x1="61" y1="51" x2="87" y2="51" />
  <line x1="64" y1="54" x2="89" y2="54" />
  <line x1="66" y1="56" x2="91" y2="56" />
  <line x1="68" y1="58" x2="94" y2="58" />
  <line x1="71" y1="61" x2="96" y2="61" />
  <line x1="73" y1="63" x2="98" y2="63" />
  <line x1="75" y1="65" x2="101" y2="65" />
  <line x1="78" y1="68" x2="103" y2="68" />
  <line x1="80" y1="70" x2="105" y2="70" />
  <line x1="80" y1="70" x2="106" y2="70" style="stroke-width:2" />

  <!-- Vertical lines -->
  <line x1="10" y1="0" x2="80" y2="70" style="stroke-width:2" />
  <line x1="13" y1="0" x2="83" y2="70" />
  <line x1="20" y1="0" x2="91" y2="70" />
  <line x1="28" y1="0" x2="99" y2="70" />
  <line x1="35" y1="0" x2="106" y2="70" style="stroke-width:2" />

  <!-- Colored Rectangle -->
  <polygon points="10.000000,0.000000 35.412617,0.000000 106.000852,70.588235 80.588235,70.588235" style="fill:#ECB172A0;stroke-width:0"/>

  <!-- Horizontal lines -->
  <line x1="80" y1="70" x2="106" y2="70" style="stroke-width:2" />
  <line x1="80" y1="76" x2="106" y2="76" />
  <line x1="80" y1="89" x2="106" y2="89" />
  <line x1="80" y1="96" x2="106" y2="96" style="stroke-width:2" />

  <!-- Vertical lines -->
  <line x1="80" y1="70" x2="80" y2="96" style="stroke-width:2" />
  <line x1="83" y1="70" x2="83" y2="96" />
  <line x1="91" y1="70" x2="91" y2="96" />
  <line x1="99" y1="70" x2="99" y2="96" />
  <line x1="106" y1="70" x2="106" y2="96" style="stroke-width:2" />

  <!-- Colored Rectangle -->
  <polygon points="80.588235,70.588235 106.000852,70.588235 106.000852,96.000852 80.588235,96.000852" style="fill:#ECB172A0;stroke-width:0"/>

  <!-- Text -->
  <text x="93.294544" y="116.000852" font-size="1.0rem" font-weight="100" text-anchor="middle" >81</text>
  <text x="126.000852" y="83.294544" font-size="1.0rem" font-weight="100" text-anchor="middle" transform="rotate(0,126.000852,83.294544)">46</text>
  <text x="35.294118" y="80.706734" font-size="1.0rem" font-weight="100" text-anchor="middle" transform="rotate(45,35.294118,80.706734)">262968</text>
</svg>
</td>
</tr>
</table></pre></li><li class='xr-var-item'><div class='xr-var-name'><span>v10</span></div><div class='xr-var-dims'>(time, latitude, longitude)</div><div class='xr-var-dtype'>float64</div><div class='xr-var-preview xr-preview'>dask.array&lt;chunksize=(8760, 10, 10), meta=np.ndarray&gt;</div><input id='attrs-1815f20a-640d-4207-b73d-5fccea288f47' class='xr-var-attrs-in' type='checkbox' disabled><label for='attrs-1815f20a-640d-4207-b73d-5fccea288f47' title='Show/Hide attributes'><svg class='icon xr-icon-file-text2'><use xlink:href='#icon-file-text2'></use></svg></label><input id='data-7eef019a-055a-455b-b567-6d6ba6270e48' class='xr-var-data-in' type='checkbox'><label for='data-7eef019a-055a-455b-b567-6d6ba6270e48' title='Show/Hide data repr'><svg class='icon xr-icon-database'><use xlink:href='#icon-database'></use></svg></label><div class='xr-var-attrs'><dl class='xr-attrs'></dl></div><pre class='xr-var-data'><table>
<tr>
<td>
<table>
  <thead>
    <tr><td> </td><th> Array </th><th> Chunk </th></tr>
  </thead>
  <tbody>
    <tr><th> Bytes </th><td> 7.84 GB </td> <td> 43.80 MB </td></tr>
    <tr><th> Shape </th><td> (262968, 46, 81) </td> <td> (8760, 25, 25) </td></tr>
    <tr><th> Count </th><td> 7573 Tasks </td><td> 372 Chunks </td></tr>
    <tr><th> Type </th><td> float64 </td><td> numpy.ndarray </td></tr>
  </tbody>
</table>
</td>
<td>
<svg width="156" height="146" style="stroke:rgb(0,0,0);stroke-width:1" >

  <!-- Horizontal lines -->
  <line x1="10" y1="0" x2="80" y2="70" style="stroke-width:2" />
  <line x1="10" y1="5" x2="80" y2="76" />
  <line x1="10" y1="19" x2="80" y2="89" />
  <line x1="10" y1="25" x2="80" y2="96" style="stroke-width:2" />

  <!-- Vertical lines -->
  <line x1="10" y1="0" x2="10" y2="25" style="stroke-width:2" />
  <line x1="12" y1="2" x2="12" y2="27" />
  <line x1="14" y1="4" x2="14" y2="30" />
  <line x1="17" y1="7" x2="17" y2="32" />
  <line x1="19" y1="9" x2="19" y2="34" />
  <line x1="21" y1="11" x2="21" y2="37" />
  <line x1="24" y1="14" x2="24" y2="39" />
  <line x1="26" y1="16" x2="26" y2="41" />
  <line x1="28" y1="18" x2="28" y2="44" />
  <line x1="31" y1="21" x2="31" y2="46" />
  <line x1="33" y1="23" x2="33" y2="48" />
  <line x1="35" y1="25" x2="35" y2="51" />
  <line x1="38" y1="28" x2="38" y2="53" />
  <line x1="40" y1="30" x2="40" y2="55" />
  <line x1="42" y1="32" x2="42" y2="58" />
  <line x1="45" y1="35" x2="45" y2="60" />
  <line x1="47" y1="37" x2="47" y2="63" />
  <line x1="49" y1="39" x2="49" y2="65" />
  <line x1="52" y1="42" x2="52" y2="67" />
  <line x1="54" y1="44" x2="54" y2="70" />
  <line x1="57" y1="47" x2="57" y2="72" />
  <line x1="59" y1="49" x2="59" y2="74" />
  <line x1="61" y1="51" x2="61" y2="77" />
  <line x1="64" y1="54" x2="64" y2="79" />
  <line x1="66" y1="56" x2="66" y2="81" />
  <line x1="68" y1="58" x2="68" y2="84" />
  <line x1="71" y1="61" x2="71" y2="86" />
  <line x1="73" y1="63" x2="73" y2="88" />
  <line x1="75" y1="65" x2="75" y2="91" />
  <line x1="78" y1="68" x2="78" y2="93" />
  <line x1="80" y1="70" x2="80" y2="95" />
  <line x1="80" y1="70" x2="80" y2="96" style="stroke-width:2" />

  <!-- Colored Rectangle -->
  <polygon points="10.000000,0.000000 80.588235,70.588235 80.588235,96.000852 10.000000,25.412617" style="fill:#ECB172A0;stroke-width:0"/>

  <!-- Horizontal lines -->
  <line x1="10" y1="0" x2="35" y2="0" style="stroke-width:2" />
  <line x1="12" y1="2" x2="37" y2="2" />
  <line x1="14" y1="4" x2="40" y2="4" />
  <line x1="17" y1="7" x2="42" y2="7" />
  <line x1="19" y1="9" x2="44" y2="9" />
  <line x1="21" y1="11" x2="47" y2="11" />
  <line x1="24" y1="14" x2="49" y2="14" />
  <line x1="26" y1="16" x2="51" y2="16" />
  <line x1="28" y1="18" x2="54" y2="18" />
  <line x1="31" y1="21" x2="56" y2="21" />
  <line x1="33" y1="23" x2="58" y2="23" />
  <line x1="35" y1="25" x2="61" y2="25" />
  <line x1="38" y1="28" x2="63" y2="28" />
  <line x1="40" y1="30" x2="65" y2="30" />
  <line x1="42" y1="32" x2="68" y2="32" />
  <line x1="45" y1="35" x2="70" y2="35" />
  <line x1="47" y1="37" x2="73" y2="37" />
  <line x1="49" y1="39" x2="75" y2="39" />
  <line x1="52" y1="42" x2="77" y2="42" />
  <line x1="54" y1="44" x2="80" y2="44" />
  <line x1="57" y1="47" x2="82" y2="47" />
  <line x1="59" y1="49" x2="84" y2="49" />
  <line x1="61" y1="51" x2="87" y2="51" />
  <line x1="64" y1="54" x2="89" y2="54" />
  <line x1="66" y1="56" x2="91" y2="56" />
  <line x1="68" y1="58" x2="94" y2="58" />
  <line x1="71" y1="61" x2="96" y2="61" />
  <line x1="73" y1="63" x2="98" y2="63" />
  <line x1="75" y1="65" x2="101" y2="65" />
  <line x1="78" y1="68" x2="103" y2="68" />
  <line x1="80" y1="70" x2="105" y2="70" />
  <line x1="80" y1="70" x2="106" y2="70" style="stroke-width:2" />

  <!-- Vertical lines -->
  <line x1="10" y1="0" x2="80" y2="70" style="stroke-width:2" />
  <line x1="13" y1="0" x2="83" y2="70" />
  <line x1="20" y1="0" x2="91" y2="70" />
  <line x1="28" y1="0" x2="99" y2="70" />
  <line x1="35" y1="0" x2="106" y2="70" style="stroke-width:2" />

  <!-- Colored Rectangle -->
  <polygon points="10.000000,0.000000 35.412617,0.000000 106.000852,70.588235 80.588235,70.588235" style="fill:#ECB172A0;stroke-width:0"/>

  <!-- Horizontal lines -->
  <line x1="80" y1="70" x2="106" y2="70" style="stroke-width:2" />
  <line x1="80" y1="76" x2="106" y2="76" />
  <line x1="80" y1="89" x2="106" y2="89" />
  <line x1="80" y1="96" x2="106" y2="96" style="stroke-width:2" />

  <!-- Vertical lines -->
  <line x1="80" y1="70" x2="80" y2="96" style="stroke-width:2" />
  <line x1="83" y1="70" x2="83" y2="96" />
  <line x1="91" y1="70" x2="91" y2="96" />
  <line x1="99" y1="70" x2="99" y2="96" />
  <line x1="106" y1="70" x2="106" y2="96" style="stroke-width:2" />

  <!-- Colored Rectangle -->
  <polygon points="80.588235,70.588235 106.000852,70.588235 106.000852,96.000852 80.588235,96.000852" style="fill:#ECB172A0;stroke-width:0"/>

  <!-- Text -->
  <text x="93.294544" y="116.000852" font-size="1.0rem" font-weight="100" text-anchor="middle" >81</text>
  <text x="126.000852" y="83.294544" font-size="1.0rem" font-weight="100" text-anchor="middle" transform="rotate(0,126.000852,83.294544)">46</text>
  <text x="35.294118" y="80.706734" font-size="1.0rem" font-weight="100" text-anchor="middle" transform="rotate(45,35.294118,80.706734)">262968</text>
</svg>
</td>
</tr>
</table></pre></li></ul></div></li><li class='xr-section-item'><input id='section-a5673cd4-8d99-4b05-a0aa-43397032f56b' class='xr-section-summary-in' type='checkbox' disabled ><label for='section-a5673cd4-8d99-4b05-a0aa-43397032f56b' class='xr-section-summary'  title='Expand/collapse section'>Attributes: <span>(0)</span></label><div class='xr-section-inline-details'></div><div class='xr-section-details'><dl class='xr-attrs'></dl></div></li></ul></div></div>



## Précipitation moyenne annuelle (MAP)


```python
# tp : total precipitation
da_tp = ds.tp
```


```python
# Les données de précipitation ERA5-Land sont cumulatives sur un jour.
# La fonction ci-dessous permet de décumuler les grilles 
da_decumulated = xr.where(da_tp.time.dt.hour == 1,
                          da_tp,
                          xr.concat([da_tp.isel(time=0),
                                     da_tp.diff(dim='time')],
                                    dim='time'))
```


```python
da_tp_moyen = da_decumulated.resample(time='1Y').sum().mean('time').compute()
```


```python
da_tp_moyen.hvplot()
```






<div id='3134'>





  <div class="bk-root" id="e94480fd-c07f-466d-a9d1-9c31301b5901" data-root-id="3134"></div>
</div>
<script type="application/javascript">(function(root) {
  function embed_document(root) {
  var docs_json = {"8e1aac3d-aacd-439b-bc37-92c344644fa7":{"roots":{"references":[{"attributes":{"children":[{"id":"3135"},{"id":"3139"},{"id":"3193"}],"margin":[0,0,0,0],"name":"Row01503","tags":["embedded"]},"id":"3134","type":"Row"},{"attributes":{},"id":"3181","type":"BasicTickFormatter"},{"attributes":{},"id":"3156","type":"SaveTool"},{"attributes":{"bottom_units":"screen","fill_alpha":0.5,"fill_color":"lightgrey","left_units":"screen","level":"overlay","line_alpha":1.0,"line_color":"black","line_dash":[4,4],"line_width":2,"render_mode":"css","right_units":"screen","top_units":"screen"},"id":"3161","type":"BoxAnnotation"},{"attributes":{"text":"","text_color":{"value":"black"},"text_font_size":{"value":"12pt"}},"id":"3140","type":"Title"},{"attributes":{},"id":"3157","type":"PanTool"},{"attributes":{"overlay":{"id":"3161"}},"id":"3159","type":"BoxZoomTool"},{"attributes":{"end":-73.95,"reset_end":-73.95,"reset_start":-82.05,"start":-82.05,"tags":[[["longitude","longitude","degrees_east"]]]},"id":"3136","type":"Range1d"},{"attributes":{},"id":"3189","type":"BasicTickFormatter"},{"attributes":{"margin":[5,5,5,5],"name":"HSpacer01508","sizing_mode":"stretch_width"},"id":"3193","type":"Spacer"},{"attributes":{},"id":"3158","type":"WheelZoomTool"},{"attributes":{"axis_label":"longitude (degrees_east)","bounds":"auto","formatter":{"id":"3181"},"major_label_orientation":"horizontal","ticker":{"id":"3149"}},"id":"3148","type":"LinearAxis"},{"attributes":{},"id":"3191","type":"UnionRenderers"},{"attributes":{},"id":"3171","type":"Selection"},{"attributes":{},"id":"3183","type":"BasicTickFormatter"},{"attributes":{},"id":"3146","type":"LinearScale"},{"attributes":{"data":{"dh":[4.599999999999994],"dw":[8.099999999999994],"image":[{"__ndarray__":"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","dtype":"float32","shape":[46,81]}],"x":[-82.05],"y":[44.45]},"selected":{"id":"3171"},"selection_policy":{"id":"3191"}},"id":"3170","type":"ColumnDataSource"},{"attributes":{"callback":null,"renderers":[{"id":"3175"}],"tags":["hv_created"],"tooltips":[["longitude (degrees_east)","$x"],["latitude (degrees_north)","$y"],["value","@image"]]},"id":"3138","type":"HoverTool"},{"attributes":{"margin":[5,5,5,5],"name":"HSpacer01507","sizing_mode":"stretch_width"},"id":"3135","type":"Spacer"},{"attributes":{},"id":"3149","type":"BasicTicker"},{"attributes":{"end":49.05,"reset_end":49.05,"reset_start":44.45,"start":44.45,"tags":[[["latitude","latitude","degrees_north"]]]},"id":"3137","type":"Range1d"},{"attributes":{},"id":"3153","type":"BasicTicker"},{"attributes":{"align":null,"below":[{"id":"3148"}],"center":[{"id":"3151"},{"id":"3155"}],"left":[{"id":"3152"}],"margin":null,"min_border_bottom":10,"min_border_left":10,"min_border_right":10,"min_border_top":10,"plot_height":300,"plot_width":700,"renderers":[{"id":"3175"}],"right":[{"id":"3178"}],"sizing_mode":"fixed","title":{"id":"3140"},"toolbar":{"id":"3162"},"x_range":{"id":"3136"},"x_scale":{"id":"3144"},"y_range":{"id":"3137"},"y_scale":{"id":"3146"}},"id":"3139","subtype":"Figure","type":"Plot"},{"attributes":{"axis":{"id":"3148"},"grid_line_color":null,"ticker":null},"id":"3151","type":"Grid"},{"attributes":{"axis_label":"latitude (degrees_north)","bounds":"auto","formatter":{"id":"3183"},"major_label_orientation":"horizontal","ticker":{"id":"3153"}},"id":"3152","type":"LinearAxis"},{"attributes":{"axis":{"id":"3152"},"dimension":1,"grid_line_color":null,"ticker":null},"id":"3155","type":"Grid"},{"attributes":{"active_drag":"auto","active_inspect":"auto","active_multi":null,"active_scroll":"auto","active_tap":"auto","tools":[{"id":"3138"},{"id":"3156"},{"id":"3157"},{"id":"3158"},{"id":"3159"},{"id":"3160"}]},"id":"3162","type":"Toolbar"},{"attributes":{"data_source":{"id":"3170"},"glyph":{"id":"3173"},"hover_glyph":null,"muted_glyph":null,"nonselection_glyph":{"id":"3174"},"selection_glyph":null,"view":{"id":"3176"}},"id":"3175","type":"GlyphRenderer"},{"attributes":{},"id":"3160","type":"ResetTool"},{"attributes":{"high":1.3218961954116821,"low":0.8154664635658264,"nan_color":"rgba(0, 0, 0, 0)","palette":["#b3fef5","#b0fef5","#adfdf5","#a9fcf5","#a6fbf6","#a3faf6","#a0faf6","#9df9f6","#9af8f6","#97f7f6","#93f7f6","#90f6f6","#8df5f6","#8af4f7","#87f3f7","#83f2f7","#80f2f7","#7df1f7","#79f0f7","#76eff7","#73eef7","#6fedf8","#6cecf8","#68ecf8","#65ebf8","#61eaf8","#5ee9f8","#5ae8f8","#57e7f8","#53e6f8","#50e5f9","#4ce4f9","#49e3f9","#45e2f9","#42e1f9","#3ee0f9","#3bdff9","#38def9","#35ddf9","#32dcf9","#30dbfa","#2ed9fa","#2dd8fa","#2cd7fa","#2bd6fa","#2bd5fa","#2ad3fa","#2ad2fa","#29d1fa","#29d0fb","#29cffb","#28cdfb","#28ccfb","#28cbfb","#28cafb","#28c8fb","#28c7fb","#29c6fb","#29c5fb","#29c4fb","#29c2fb","#2ac1fb","#2ac0fb","#2bbffb","#2bbdfc","#2cbcfc","#2dbbfc","#2db9fc","#2eb8fc","#2fb7fc","#2fb6fc","#30b4fc","#31b3fc","#32b2fc","#32b0fc","#33affc","#33aefc","#34adfc","#34abfc","#34aafc","#35a9fc","#35a8fc","#35a6fc","#35a5fc","#35a4fc","#35a3fc","#35a1fc","#35a0fc","#359ffc","#359dfc","#359cfc","#359bfc","#349afd","#3498fd","#3497fd","#3396fd","#3395fd","#3293fd","#3292fd","#3191fd","#3090fd","#308ffd","#2f8dfd","#2f8cfd","#2e8bfd","#2e8afd","#2d88fd","#2d87fd","#2c86fd","#2c84fd","#2c83fd","#2c82fd","#2b81fd","#2b7ffd","#2b7efd","#2b7dfd","#2b7bfd","#2b7afd","#2b79fd","#2b77fd","#2b76fd","#2b75fd","#2b73fd","#2c72fd","#2c71fd","#2c6ffd","#2c6efd","#2d6cfd","#2d6bfd","#2d6afc","#2e68fc","#2e67fc","#2e65fc","#2e64fc","#2f62fc","#2f61fc","#2f5ffc","#2f5efc","#2f5dfc","#2f5bfc","#2f5afc","#2f58fb","#2f57fb","#2f55fb","#2f53fb","#2f52fb","#2f50fb","#2f4ffb","#2f4dfb","#2e4cfb","#2e4afb","#2e48fb","#2e47fa","#2d45fa","#2d43fa","#2d42fa","#2d40fa","#2c3efa","#2c3dfa","#2b3bf9","#2b39f9","#2a37f9","#2a36f8","#2934f8","#2832f7","#2831f7","#272ff6","#262ef5","#252cf5","#252af4","#2429f3","#2327f2","#2226f1","#2124f0","#2023ef","#1f22ee","#1e20ed","#1d1feb","#1c1eea","#1b1ce9","#1a1be7","#181ae6","#1719e5","#1618e3","#1417e1","#1316e0","#1215de","#1014dc","#0f13db","#0e12d9","#0d11d7","#0c10d5","#0b0fd3","#0a0ed1","#090dd0","#080dce","#080ccc","#070bca","#070ac8","#0709c6","#0708c4","#0707c2","#0707bf","#0806bd","#0806bb","#0905b9","#0904b7","#0a04b5","#0a04b2","#0b03b0","#0c03ae","#0d02ab","#0e02a9","#0e02a7","#0f02a4","#0f01a2","#1001a0","#10019d","#10019b","#100199","#100197","#100194","#0f0192","#0f0190","#0f018e","#0e018b","#0e0189","#0d0187","#0d0185","#0c0183","#0b0181","#0b017e","#0a017c","#09017a","#090178","#080276","#070274","#060272","#060270","#05026e","#04026c","#030269","#030267","#020265","#010263","#010261","#00025f","#00025d","#00025b","#000259","#000257","#000255","#000154","#000152","#000150","#00004e"]},"id":"3169","type":"LinearColorMapper"},{"attributes":{},"id":"3144","type":"LinearScale"},{"attributes":{"color_mapper":{"id":"3169"},"dh":{"field":"dh","units":"data"},"dw":{"field":"dw","units":"data"},"global_alpha":0.1,"image":{"field":"image"},"x":{"field":"x"},"y":{"field":"y"}},"id":"3174","type":"Image"},{"attributes":{"source":{"id":"3170"}},"id":"3176","type":"CDSView"},{"attributes":{"color_mapper":{"id":"3169"},"dh":{"field":"dh","units":"data"},"dw":{"field":"dw","units":"data"},"image":{"field":"image"},"x":{"field":"x"},"y":{"field":"y"}},"id":"3173","type":"Image"},{"attributes":{},"id":"3177","type":"BasicTicker"},{"attributes":{"bar_line_color":{"value":"black"},"color_mapper":{"id":"3169"},"formatter":{"id":"3189"},"label_standoff":8,"location":[0,0],"major_tick_line_color":"black","ticker":{"id":"3177"}},"id":"3178","type":"ColorBar"}],"root_ids":["3134"]},"title":"Bokeh Application","version":"2.0.1"}};
  var render_items = [{"docid":"8e1aac3d-aacd-439b-bc37-92c344644fa7","root_ids":["3134"],"roots":{"3134":"e94480fd-c07f-466d-a9d1-9c31301b5901"}}];
  root.Bokeh.embed.embed_items_notebook(docs_json, render_items);
  }
if (root.Bokeh !== undefined) {
    embed_document(root);
  } else {
    var attempts = 0;
    var timer = setInterval(function(root) {
      if (root.Bokeh !== undefined) {
        clearInterval(timer);
        embed_document(root);
      } else if (document.readyState == "complete") {
        attempts++;
        if (attempts > 100) {
          clearInterval(timer);
          console.log("Bokeh: ERROR: Unable to run BokehJS code because BokehJS library is missing");
        }
      }
    }, 10, root)
  }
})(window);</script>



## Température moyenne saisonnière


```python
da_t2m = ds.t2m - 273.15

```


```python
da_t2m_pr = da_t2m.sel(time = np.isin(da_t2m['time.month'], test_elements=[3,4,5,6]))
da_t2m_ete = da_t2m.sel(time = np.isin(da_t2m['time.month'], test_elements=[7,8]))
da_t2m_automne = da_t2m.sel(time = np.isin(da_t2m['time.month'], test_elements=[9,10,11]))
da_t2m_hiver = da_t2m.sel(time = np.isin(da_t2m['time.month'], test_elements=[12,1,2]))

```


```python
da_t2m_pr_moyen = da_t2m_pr.resample(time='1Y').mean().mean('time').compute()
da_t2m_ete_moyen  = da_t2m_ete.resample(time='1Y').mean().mean('time').compute()
da_t2m_automne_moyen  = da_t2m_automne.resample(time='1Y').mean().mean('time').compute()
da_t2m_hiver_moyen  = da_t2m_hiver.resample(time='1Y').mean().mean('time').compute()
```


```python
(da_t2m_pr_moyen.hvplot(label='Printemps', cmap='bwr') + \
 da_t2m_ete_moyen.hvplot(label='Été', cmap='bwr') + \
 da_t2m_automne_moyen.hvplot(label='Automne', cmap='bwr') + \
 da_t2m_hiver_moyen.hvplot(label='Hiver', cmap='bwr')).cols(1)
```






<div id='10178'>





  <div class="bk-root" id="701dd0aa-3b0c-4e8a-88db-590cf763f2fb" data-root-id="10178"></div>
</div>
<script type="application/javascript">(function(root) {
  function embed_document(root) {
  var docs_json = {"985211b5-b297-4789-9667-5350fedd51ee":{"roots":{"references":[{"attributes":{"callback":null,"renderers":[{"id":"10219"}],"tags":["hv_created"],"tooltips":[["longitude (degrees_east)","$x"],["latitude (degrees_north)","$y"],["t2m","@image"]]},"id":"10182","type":"HoverTool"},{"attributes":{"end":49.05,"reset_end":49.05,"reset_start":44.45,"start":44.45,"tags":[[["latitude","latitude","degrees_north"]]]},"id":"10181","type":"Range1d"},{"attributes":{},"id":"10215","type":"Selection"},{"attributes":{},"id":"10371","type":"BasicTickFormatter"},{"attributes":{"color_mapper":{"id":"10213"},"dh":{"field":"dh","units":"data"},"dw":{"field":"dw","units":"data"},"image":{"field":"image"},"x":{"field":"x"},"y":{"field":"y"}},"id":"10217","type":"Image"},{"attributes":{},"id":"10225","type":"BasicTickFormatter"},{"attributes":{"axis":{"id":"10242"},"dimension":1,"grid_line_color":null,"ticker":null},"id":"10245","type":"Grid"},{"attributes":{},"id":"10247","type":"PanTool"},{"attributes":{},"id":"10267","type":"BasicTicker"},{"attributes":{"data_source":{"id":"10214"},"glyph":{"id":"10217"},"hover_glyph":null,"muted_glyph":null,"nonselection_glyph":{"id":"10218"},"selection_glyph":null,"view":{"id":"10220"}},"id":"10219","type":"GlyphRenderer"},{"attributes":{},"id":"10227","type":"BasicTickFormatter"},{"attributes":{},"id":"10221","type":"BasicTicker"},{"attributes":{},"id":"10250","type":"ResetTool"},{"attributes":{"data":{"dh":[4.599999999999994],"dw":[8.099999999999994],"image":[{"__ndarray__":"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","dtype":"float32","shape":[46,81]}],"x":[-82.05],"y":[44.45]},"selected":{"id":"10353"},"selection_policy":{"id":"10403"}},"id":"10352","type":"ColumnDataSource"},{"attributes":{"overlay":{"id":"10251"}},"id":"10249","type":"BoxZoomTool"},{"attributes":{"bottom_units":"screen","fill_alpha":0.5,"fill_color":"lightgrey","left_units":"screen","level":"overlay","line_alpha":1.0,"line_color":"black","line_dash":[4,4],"line_width":2,"render_mode":"css","right_units":"screen","top_units":"screen"},"id":"10251","type":"BoxAnnotation"},{"attributes":{},"id":"10373","type":"UnionRenderers"},{"attributes":{"end":-73.95,"reset_end":-73.95,"reset_start":-82.05,"start":-82.05,"tags":[[["longitude","longitude","degrees_east"]]]},"id":"10180","type":"Range1d"},{"attributes":{},"id":"10342","type":"ResetTool"},{"attributes":{},"id":"10381","type":"BasicTickFormatter"},{"attributes":{},"id":"10248","type":"WheelZoomTool"},{"attributes":{"source":{"id":"10214"}},"id":"10220","type":"CDSView"},{"attributes":{"active_drag":"auto","active_inspect":"auto","active_multi":null,"active_scroll":"auto","active_tap":"auto","tools":[{"id":"10228"},{"id":"10246"},{"id":"10247"},{"id":"10248"},{"id":"10249"},{"id":"10250"}]},"id":"10252","type":"Toolbar"},{"attributes":{"bottom_units":"screen","fill_alpha":0.5,"fill_color":"lightgrey","left_units":"screen","level":"overlay","line_alpha":1.0,"line_color":"black","line_dash":[4,4],"line_width":2,"render_mode":"css","right_units":"screen","top_units":"screen"},"id":"10205","type":"BoxAnnotation"},{"attributes":{},"id":"10246","type":"SaveTool"},{"attributes":{"bar_line_color":{"value":"black"},"color_mapper":{"id":"10213"},"formatter":{"id":"10371"},"label_standoff":8,"location":[0,0],"major_tick_line_color":"black","ticker":{"id":"10221"}},"id":"10222","type":"ColorBar"},{"attributes":{"color_mapper":{"id":"10213"},"dh":{"field":"dh","units":"data"},"dw":{"field":"dw","units":"data"},"global_alpha":0.1,"image":{"field":"image"},"x":{"field":"x"},"y":{"field":"y"}},"id":"10218","type":"Image"},{"attributes":{"overlay":{"id":"10343"}},"id":"10341","type":"BoxZoomTool"},{"attributes":{"bar_line_color":{"value":"black"},"color_mapper":{"id":"10259"},"formatter":{"id":"10381"},"label_standoff":8,"location":[0,0],"major_tick_line_color":"black","ticker":{"id":"10267"}},"id":"10268","type":"ColorBar"},{"attributes":{"bottom_units":"screen","fill_alpha":0.5,"fill_color":"lightgrey","left_units":"screen","level":"overlay","line_alpha":1.0,"line_color":"black","line_dash":[4,4],"line_width":2,"render_mode":"css","right_units":"screen","top_units":"screen"},"id":"10343","type":"BoxAnnotation"},{"attributes":{},"id":"10200","type":"SaveTool"},{"attributes":{"align":null,"below":[{"id":"10238"}],"center":[{"id":"10241"},{"id":"10245"}],"left":[{"id":"10242"}],"margin":null,"min_border_bottom":10,"min_border_left":10,"min_border_right":10,"min_border_top":10,"plot_height":300,"plot_width":700,"renderers":[{"id":"10265"}],"right":[{"id":"10268"}],"sizing_mode":"fixed","title":{"id":"10230"},"toolbar":{"id":"10252"},"toolbar_location":null,"x_range":{"id":"10180"},"x_scale":{"id":"10234"},"y_range":{"id":"10181"},"y_scale":{"id":"10236"}},"id":"10229","subtype":"Figure","type":"Plot"},{"attributes":{},"id":"10201","type":"PanTool"},{"attributes":{"overlay":{"id":"10297"}},"id":"10295","type":"BoxZoomTool"},{"attributes":{"text":"Hiver","text_color":{"value":"black"},"text_font_size":{"value":"12pt"}},"id":"10322","type":"Title"},{"attributes":{"axis":{"id":"10330"},"grid_line_color":null,"ticker":null},"id":"10333","type":"Grid"},{"attributes":{},"id":"10317","type":"BasicTickFormatter"},{"attributes":{},"id":"10401","type":"BasicTickFormatter"},{"attributes":{},"id":"10280","type":"LinearScale"},{"attributes":{},"id":"10326","type":"LinearScale"},{"attributes":{"align":null,"below":[{"id":"10284"}],"center":[{"id":"10287"},{"id":"10291"}],"left":[{"id":"10288"}],"margin":null,"min_border_bottom":10,"min_border_left":10,"min_border_right":10,"min_border_top":10,"plot_height":300,"plot_width":700,"renderers":[{"id":"10311"}],"right":[{"id":"10314"}],"sizing_mode":"fixed","title":{"id":"10276"},"toolbar":{"id":"10298"},"toolbar_location":null,"x_range":{"id":"10180"},"x_scale":{"id":"10280"},"y_range":{"id":"10181"},"y_scale":{"id":"10282"}},"id":"10275","subtype":"Figure","type":"Plot"},{"attributes":{},"id":"10363","type":"BasicTickFormatter"},{"attributes":{},"id":"10313","type":"BasicTicker"},{"attributes":{"source":{"id":"10352"}},"id":"10358","type":"CDSView"},{"attributes":{"active_drag":"auto","active_inspect":"auto","active_multi":null,"active_scroll":"auto","active_tap":"auto","tools":[{"id":"10274"},{"id":"10292"},{"id":"10293"},{"id":"10294"},{"id":"10295"},{"id":"10296"}]},"id":"10298","type":"Toolbar"},{"attributes":{"high":2.6370770931243896,"low":-1.5352720022201538,"nan_color":"rgba(0, 0, 0, 0)","palette":["#0000ff","#0202ff","#0404ff","#0606ff","#0808ff","#0a0aff","#0c0cff","#0e0eff","#1010ff","#1212ff","#1414ff","#1616ff","#1818ff","#1a1aff","#1c1cff","#1e1eff","#2020ff","#2222ff","#2424ff","#2626ff","#2828ff","#2a2aff","#2c2cff","#2e2eff","#3030ff","#3232ff","#3434ff","#3636ff","#3838ff","#3a3aff","#3c3cff","#3e3eff","#4040ff","#4141ff","#4444ff","#4646ff","#4848ff","#4949ff","#4c4cff","#4e4eff","#5050ff","#5151ff","#5454ff","#5656ff","#5858ff","#5959ff","#5c5cff","#5e5eff","#6060ff","#6161ff","#6464ff","#6666ff","#6868ff","#6969ff","#6c6cff","#6e6eff","#7070ff","#7171ff","#7474ff","#7676ff","#7878ff","#7979ff","#7c7cff","#7e7eff","#8080ff","#8282ff","#8383ff","#8686ff","#8888ff","#8a8aff","#8c8cff","#8e8eff","#9090ff","#9292ff","#9393ff","#9696ff","#9898ff","#9a9aff","#9c9cff","#9e9eff","#a0a0ff","#a2a2ff","#a3a3ff","#a6a6ff","#a8a8ff","#aaaaff","#acacff","#aeaeff","#b0b0ff","#b2b2ff","#b3b3ff","#b6b6ff","#b8b8ff","#babaff","#bcbcff","#bebeff","#c0c0ff","#c2c2ff","#c3c3ff","#c6c6ff","#c8c8ff","#cacaff","#ccccff","#ceceff","#d0d0ff","#d2d2ff","#d3d3ff","#d6d6ff","#d8d8ff","#dadaff","#dcdcff","#dedeff","#e0e0ff","#e2e2ff","#e3e3ff","#e6e6ff","#e8e8ff","#eaeaff","#ececff","#eeeeff","#f0f0ff","#f2f2ff","#f3f3ff","#f6f6ff","#f8f8ff","#fafaff","#fcfcff","#fefeff","#fffefe","#fffcfc","#fffafa","#fff8f8","#fff6f6","#fff4f4","#fff2f2","#fff0f0","#ffeeee","#ffecec","#ffeaea","#ffe8e8","#ffe6e6","#ffe4e4","#ffe2e2","#ffe0e0","#ffdede","#ffdcdc","#ffdada","#ffd8d8","#ffd6d6","#ffd3d3","#ffd2d2","#ffd0d0","#ffcece","#ffcccc","#ffcaca","#ffc8c8","#ffc6c6","#ffc3c3","#ffc2c2","#ffc0c0","#ffbebe","#ffbcbc","#ffbaba","#ffb8b8","#ffb6b6","#ffb3b3","#ffb2b2","#ffb0b0","#ffaeae","#ffacac","#ffaaaa","#ffa8a8","#ffa6a6","#ffa3a3","#ffa2a2","#ffa0a0","#ff9e9e","#ff9c9c","#ff9a9a","#ff9898","#ff9696","#ff9393","#ff9292","#ff9090","#ff8e8e","#ff8c8c","#ff8a8a","#ff8888","#ff8686","#ff8383","#ff8282","#ff8080","#ff7e7e","#ff7c7c","#ff7979","#ff7878","#ff7676","#ff7474","#ff7171","#ff7070","#ff6e6e","#ff6c6c","#ff6969","#ff6868","#ff6666","#ff6464","#ff6161","#ff6060","#ff5e5e","#ff5c5c","#ff5959","#ff5858","#ff5656","#ff5454","#ff5151","#ff5050","#ff4e4e","#ff4c4c","#ff4949","#ff4848","#ff4646","#ff4444","#ff4141","#ff4040","#ff3e3e","#ff3c3c","#ff3939","#ff3838","#ff3636","#ff3434","#ff3131","#ff3030","#ff2e2e","#ff2c2c","#ff2929","#ff2828","#ff2626","#ff2424","#ff2121","#ff2020","#ff1e1e","#ff1c1c","#ff1919","#ff1818","#ff1616","#ff1414","#ff1111","#ff1010","#ff0e0e","#ff0c0c","#ff0909","#ff0808","#ff0606","#ff0404","#ff0101","#ff0000"]},"id":"10305","type":"LinearColorMapper"},{"attributes":{},"id":"10365","type":"BasicTickFormatter"},{"attributes":{},"id":"10204","type":"ResetTool"},{"attributes":{"data":{"dh":[4.599999999999994],"dw":[8.099999999999994],"image":[{"__ndarray__":"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","dtype":"float32","shape":[46,81]}],"x":[-82.05],"y":[44.45]},"selected":{"id":"10261"},"selection_policy":{"id":"10383"}},"id":"10260","type":"ColumnDataSource"},{"attributes":{},"id":"10340","type":"WheelZoomTool"},{"attributes":{},"id":"10285","type":"BasicTicker"},{"attributes":{},"id":"10319","type":"BasicTickFormatter"},{"attributes":{"callback":null,"renderers":[{"id":"10357"}],"tags":["hv_created"],"tooltips":[["longitude (degrees_east)","$x"],["latitude (degrees_north)","$y"],["t2m","@image"]]},"id":"10320","type":"HoverTool"},{"attributes":{"axis_label":"latitude (degrees_north)","bounds":"auto","formatter":{"id":"10273"},"major_label_orientation":"horizontal","ticker":{"id":"10243"}},"id":"10242","type":"LinearAxis"},{"attributes":{"high":4.796209812164307,"low":-4.796209812164307,"nan_color":"rgba(0, 0, 0, 0)","palette":["#0000ff","#0202ff","#0404ff","#0606ff","#0808ff","#0a0aff","#0c0cff","#0e0eff","#1010ff","#1212ff","#1414ff","#1616ff","#1818ff","#1a1aff","#1c1cff","#1e1eff","#2020ff","#2222ff","#2424ff","#2626ff","#2828ff","#2a2aff","#2c2cff","#2e2eff","#3030ff","#3232ff","#3434ff","#3636ff","#3838ff","#3a3aff","#3c3cff","#3e3eff","#4040ff","#4141ff","#4444ff","#4646ff","#4848ff","#4949ff","#4c4cff","#4e4eff","#5050ff","#5151ff","#5454ff","#5656ff","#5858ff","#5959ff","#5c5cff","#5e5eff","#6060ff","#6161ff","#6464ff","#6666ff","#6868ff","#6969ff","#6c6cff","#6e6eff","#7070ff","#7171ff","#7474ff","#7676ff","#7878ff","#7979ff","#7c7cff","#7e7eff","#8080ff","#8282ff","#8383ff","#8686ff","#8888ff","#8a8aff","#8c8cff","#8e8eff","#9090ff","#9292ff","#9393ff","#9696ff","#9898ff","#9a9aff","#9c9cff","#9e9eff","#a0a0ff","#a2a2ff","#a3a3ff","#a6a6ff","#a8a8ff","#aaaaff","#acacff","#aeaeff","#b0b0ff","#b2b2ff","#b3b3ff","#b6b6ff","#b8b8ff","#babaff","#bcbcff","#bebeff","#c0c0ff","#c2c2ff","#c3c3ff","#c6c6ff","#c8c8ff","#cacaff","#ccccff","#ceceff","#d0d0ff","#d2d2ff","#d3d3ff","#d6d6ff","#d8d8ff","#dadaff","#dcdcff","#dedeff","#e0e0ff","#e2e2ff","#e3e3ff","#e6e6ff","#e8e8ff","#eaeaff","#ececff","#eeeeff","#f0f0ff","#f2f2ff","#f3f3ff","#f6f6ff","#f8f8ff","#fafaff","#fcfcff","#fefeff","#fffefe","#fffcfc","#fffafa","#fff8f8","#fff6f6","#fff4f4","#fff2f2","#fff0f0","#ffeeee","#ffecec","#ffeaea","#ffe8e8","#ffe6e6","#ffe4e4","#ffe2e2","#ffe0e0","#ffdede","#ffdcdc","#ffdada","#ffd8d8","#ffd6d6","#ffd3d3","#ffd2d2","#ffd0d0","#ffcece","#ffcccc","#ffcaca","#ffc8c8","#ffc6c6","#ffc3c3","#ffc2c2","#ffc0c0","#ffbebe","#ffbcbc","#ffbaba","#ffb8b8","#ffb6b6","#ffb3b3","#ffb2b2","#ffb0b0","#ffaeae","#ffacac","#ffaaaa","#ffa8a8","#ffa6a6","#ffa3a3","#ffa2a2","#ffa0a0","#ff9e9e","#ff9c9c","#ff9a9a","#ff9898","#ff9696","#ff9393","#ff9292","#ff9090","#ff8e8e","#ff8c8c","#ff8a8a","#ff8888","#ff8686","#ff8383","#ff8282","#ff8080","#ff7e7e","#ff7c7c","#ff7979","#ff7878","#ff7676","#ff7474","#ff7171","#ff7070","#ff6e6e","#ff6c6c","#ff6969","#ff6868","#ff6666","#ff6464","#ff6161","#ff6060","#ff5e5e","#ff5c5c","#ff5959","#ff5858","#ff5656","#ff5454","#ff5151","#ff5050","#ff4e4e","#ff4c4c","#ff4949","#ff4848","#ff4646","#ff4444","#ff4141","#ff4040","#ff3e3e","#ff3c3c","#ff3939","#ff3838","#ff3636","#ff3434","#ff3131","#ff3030","#ff2e2e","#ff2c2c","#ff2929","#ff2828","#ff2626","#ff2424","#ff2121","#ff2020","#ff1e1e","#ff1c1c","#ff1919","#ff1818","#ff1616","#ff1414","#ff1111","#ff1010","#ff0e0e","#ff0c0c","#ff0909","#ff0808","#ff0606","#ff0404","#ff0101","#ff0000"]},"id":"10213","type":"LinearColorMapper"},{"attributes":{},"id":"10293","type":"PanTool"},{"attributes":{"axis":{"id":"10284"},"grid_line_color":null,"ticker":null},"id":"10287","type":"Grid"},{"attributes":{},"id":"10239","type":"BasicTicker"},{"attributes":{"high":-3.030102014541626,"low":-14.707056999206543,"nan_color":"rgba(0, 0, 0, 0)","palette":["#0000ff","#0202ff","#0404ff","#0606ff","#0808ff","#0a0aff","#0c0cff","#0e0eff","#1010ff","#1212ff","#1414ff","#1616ff","#1818ff","#1a1aff","#1c1cff","#1e1eff","#2020ff","#2222ff","#2424ff","#2626ff","#2828ff","#2a2aff","#2c2cff","#2e2eff","#3030ff","#3232ff","#3434ff","#3636ff","#3838ff","#3a3aff","#3c3cff","#3e3eff","#4040ff","#4141ff","#4444ff","#4646ff","#4848ff","#4949ff","#4c4cff","#4e4eff","#5050ff","#5151ff","#5454ff","#5656ff","#5858ff","#5959ff","#5c5cff","#5e5eff","#6060ff","#6161ff","#6464ff","#6666ff","#6868ff","#6969ff","#6c6cff","#6e6eff","#7070ff","#7171ff","#7474ff","#7676ff","#7878ff","#7979ff","#7c7cff","#7e7eff","#8080ff","#8282ff","#8383ff","#8686ff","#8888ff","#8a8aff","#8c8cff","#8e8eff","#9090ff","#9292ff","#9393ff","#9696ff","#9898ff","#9a9aff","#9c9cff","#9e9eff","#a0a0ff","#a2a2ff","#a3a3ff","#a6a6ff","#a8a8ff","#aaaaff","#acacff","#aeaeff","#b0b0ff","#b2b2ff","#b3b3ff","#b6b6ff","#b8b8ff","#babaff","#bcbcff","#bebeff","#c0c0ff","#c2c2ff","#c3c3ff","#c6c6ff","#c8c8ff","#cacaff","#ccccff","#ceceff","#d0d0ff","#d2d2ff","#d3d3ff","#d6d6ff","#d8d8ff","#dadaff","#dcdcff","#dedeff","#e0e0ff","#e2e2ff","#e3e3ff","#e6e6ff","#e8e8ff","#eaeaff","#ececff","#eeeeff","#f0f0ff","#f2f2ff","#f3f3ff","#f6f6ff","#f8f8ff","#fafaff","#fcfcff","#fefeff","#fffefe","#fffcfc","#fffafa","#fff8f8","#fff6f6","#fff4f4","#fff2f2","#fff0f0","#ffeeee","#ffecec","#ffeaea","#ffe8e8","#ffe6e6","#ffe4e4","#ffe2e2","#ffe0e0","#ffdede","#ffdcdc","#ffdada","#ffd8d8","#ffd6d6","#ffd3d3","#ffd2d2","#ffd0d0","#ffcece","#ffcccc","#ffcaca","#ffc8c8","#ffc6c6","#ffc3c3","#ffc2c2","#ffc0c0","#ffbebe","#ffbcbc","#ffbaba","#ffb8b8","#ffb6b6","#ffb3b3","#ffb2b2","#ffb0b0","#ffaeae","#ffacac","#ffaaaa","#ffa8a8","#ffa6a6","#ffa3a3","#ffa2a2","#ffa0a0","#ff9e9e","#ff9c9c","#ff9a9a","#ff9898","#ff9696","#ff9393","#ff9292","#ff9090","#ff8e8e","#ff8c8c","#ff8a8a","#ff8888","#ff8686","#ff8383","#ff8282","#ff8080","#ff7e7e","#ff7c7c","#ff7979","#ff7878","#ff7676","#ff7474","#ff7171","#ff7070","#ff6e6e","#ff6c6c","#ff6969","#ff6868","#ff6666","#ff6464","#ff6161","#ff6060","#ff5e5e","#ff5c5c","#ff5959","#ff5858","#ff5656","#ff5454","#ff5151","#ff5050","#ff4e4e","#ff4c4c","#ff4949","#ff4848","#ff4646","#ff4444","#ff4141","#ff4040","#ff3e3e","#ff3c3c","#ff3939","#ff3838","#ff3636","#ff3434","#ff3131","#ff3030","#ff2e2e","#ff2c2c","#ff2929","#ff2828","#ff2626","#ff2424","#ff2121","#ff2020","#ff1e1e","#ff1c1c","#ff1919","#ff1818","#ff1616","#ff1414","#ff1111","#ff1010","#ff0e0e","#ff0c0c","#ff0909","#ff0808","#ff0606","#ff0404","#ff0101","#ff0000"]},"id":"10351","type":"LinearColorMapper"},{"attributes":{"align":null,"below":[{"id":"10330"}],"center":[{"id":"10333"},{"id":"10337"}],"left":[{"id":"10334"}],"margin":null,"min_border_bottom":10,"min_border_left":10,"min_border_right":10,"min_border_top":10,"plot_height":300,"plot_width":700,"renderers":[{"id":"10357"}],"right":[{"id":"10360"}],"sizing_mode":"fixed","title":{"id":"10322"},"toolbar":{"id":"10344"},"toolbar_location":null,"x_range":{"id":"10180"},"x_scale":{"id":"10326"},"y_range":{"id":"10181"},"y_scale":{"id":"10328"}},"id":"10321","subtype":"Figure","type":"Plot"},{"attributes":{"children":[[{"id":"10183"},0,0],[{"id":"10229"},1,0],[{"id":"10275"},2,0],[{"id":"10321"},3,0]]},"id":"10406","type":"GridBox"},{"attributes":{"axis_label":"longitude (degrees_east)","bounds":"auto","formatter":{"id":"10271"},"major_label_orientation":"horizontal","ticker":{"id":"10239"}},"id":"10238","type":"LinearAxis"},{"attributes":{},"id":"10282","type":"LinearScale"},{"attributes":{},"id":"10331","type":"BasicTicker"},{"attributes":{"axis":{"id":"10288"},"dimension":1,"grid_line_color":null,"ticker":null},"id":"10291","type":"Grid"},{"attributes":{"color_mapper":{"id":"10305"},"dh":{"field":"dh","units":"data"},"dw":{"field":"dw","units":"data"},"image":{"field":"image"},"x":{"field":"x"},"y":{"field":"y"}},"id":"10309","type":"Image"},{"attributes":{"source":{"id":"10306"}},"id":"10312","type":"CDSView"},{"attributes":{},"id":"10359","type":"BasicTicker"},{"attributes":{"text":"Printemps","text_color":{"value":"black"},"text_font_size":{"value":"12pt"}},"id":"10184","type":"Title"},{"attributes":{},"id":"10202","type":"WheelZoomTool"},{"attributes":{"color_mapper":{"id":"10351"},"dh":{"field":"dh","units":"data"},"dw":{"field":"dw","units":"data"},"image":{"field":"image"},"x":{"field":"x"},"y":{"field":"y"}},"id":"10355","type":"Image"},{"attributes":{"text":"\u00c9t\u00e9","text_color":{"value":"black"},"text_font_size":{"value":"12pt"}},"id":"10230","type":"Title"},{"attributes":{"active_drag":"auto","active_inspect":"auto","active_multi":null,"active_scroll":"auto","active_tap":"auto","tools":[{"id":"10320"},{"id":"10338"},{"id":"10339"},{"id":"10340"},{"id":"10341"},{"id":"10342"}]},"id":"10344","type":"Toolbar"},{"attributes":{},"id":"10236","type":"LinearScale"},{"attributes":{"children":[{"id":"10408"},{"id":"10406"}]},"id":"10409","type":"Column"},{"attributes":{"source":{"id":"10260"}},"id":"10266","type":"CDSView"},{"attributes":{"axis":{"id":"10192"},"grid_line_color":null,"ticker":null},"id":"10195","type":"Grid"},{"attributes":{"margin":[5,5,5,5],"name":"HSpacer01971","sizing_mode":"stretch_width"},"id":"10179","type":"Spacer"},{"attributes":{},"id":"10296","type":"ResetTool"},{"attributes":{"margin":[5,5,5,5],"name":"HSpacer01972","sizing_mode":"stretch_width"},"id":"10698","type":"Spacer"},{"attributes":{"active_drag":"auto","active_inspect":"auto","active_multi":null,"active_scroll":"auto","active_tap":"auto","tools":[{"id":"10182"},{"id":"10200"},{"id":"10201"},{"id":"10202"},{"id":"10203"},{"id":"10204"}]},"id":"10206","type":"Toolbar"},{"attributes":{},"id":"10197","type":"BasicTicker"},{"attributes":{"text":"Automne","text_color":{"value":"black"},"text_font_size":{"value":"12pt"}},"id":"10276","type":"Title"},{"attributes":{},"id":"10339","type":"PanTool"},{"attributes":{"high":-4.016224384307861,"low":-39.71299743652344,"nan_color":"rgba(0, 0, 0, 0)","palette":["#0000ff","#0202ff","#0404ff","#0606ff","#0808ff","#0a0aff","#0c0cff","#0e0eff","#1010ff","#1212ff","#1414ff","#1616ff","#1818ff","#1a1aff","#1c1cff","#1e1eff","#2020ff","#2222ff","#2424ff","#2626ff","#2828ff","#2a2aff","#2c2cff","#2e2eff","#3030ff","#3232ff","#3434ff","#3636ff","#3838ff","#3a3aff","#3c3cff","#3e3eff","#4040ff","#4141ff","#4444ff","#4646ff","#4848ff","#4949ff","#4c4cff","#4e4eff","#5050ff","#5151ff","#5454ff","#5656ff","#5858ff","#5959ff","#5c5cff","#5e5eff","#6060ff","#6161ff","#6464ff","#6666ff","#6868ff","#6969ff","#6c6cff","#6e6eff","#7070ff","#7171ff","#7474ff","#7676ff","#7878ff","#7979ff","#7c7cff","#7e7eff","#8080ff","#8282ff","#8383ff","#8686ff","#8888ff","#8a8aff","#8c8cff","#8e8eff","#9090ff","#9292ff","#9393ff","#9696ff","#9898ff","#9a9aff","#9c9cff","#9e9eff","#a0a0ff","#a2a2ff","#a3a3ff","#a6a6ff","#a8a8ff","#aaaaff","#acacff","#aeaeff","#b0b0ff","#b2b2ff","#b3b3ff","#b6b6ff","#b8b8ff","#babaff","#bcbcff","#bebeff","#c0c0ff","#c2c2ff","#c3c3ff","#c6c6ff","#c8c8ff","#cacaff","#ccccff","#ceceff","#d0d0ff","#d2d2ff","#d3d3ff","#d6d6ff","#d8d8ff","#dadaff","#dcdcff","#dedeff","#e0e0ff","#e2e2ff","#e3e3ff","#e6e6ff","#e8e8ff","#eaeaff","#ececff","#eeeeff","#f0f0ff","#f2f2ff","#f3f3ff","#f6f6ff","#f8f8ff","#fafaff","#fcfcff","#fefeff","#fffefe","#fffcfc","#fffafa","#fff8f8","#fff6f6","#fff4f4","#fff2f2","#fff0f0","#ffeeee","#ffecec","#ffeaea","#ffe8e8","#ffe6e6","#ffe4e4","#ffe2e2","#ffe0e0","#ffdede","#ffdcdc","#ffdada","#ffd8d8","#ffd6d6","#ffd3d3","#ffd2d2","#ffd0d0","#ffcece","#ffcccc","#ffcaca","#ffc8c8","#ffc6c6","#ffc3c3","#ffc2c2","#ffc0c0","#ffbebe","#ffbcbc","#ffbaba","#ffb8b8","#ffb6b6","#ffb3b3","#ffb2b2","#ffb0b0","#ffaeae","#ffacac","#ffaaaa","#ffa8a8","#ffa6a6","#ffa3a3","#ffa2a2","#ffa0a0","#ff9e9e","#ff9c9c","#ff9a9a","#ff9898","#ff9696","#ff9393","#ff9292","#ff9090","#ff8e8e","#ff8c8c","#ff8a8a","#ff8888","#ff8686","#ff8383","#ff8282","#ff8080","#ff7e7e","#ff7c7c","#ff7979","#ff7878","#ff7676","#ff7474","#ff7171","#ff7070","#ff6e6e","#ff6c6c","#ff6969","#ff6868","#ff6666","#ff6464","#ff6161","#ff6060","#ff5e5e","#ff5c5c","#ff5959","#ff5858","#ff5656","#ff5454","#ff5151","#ff5050","#ff4e4e","#ff4c4c","#ff4949","#ff4848","#ff4646","#ff4444","#ff4141","#ff4040","#ff3e3e","#ff3c3c","#ff3939","#ff3838","#ff3636","#ff3434","#ff3131","#ff3030","#ff2e2e","#ff2c2c","#ff2929","#ff2828","#ff2626","#ff2424","#ff2121","#ff2020","#ff1e1e","#ff1c1c","#ff1919","#ff1818","#ff1616","#ff1414","#ff1111","#ff1010","#ff0e0e","#ff0c0c","#ff0909","#ff0808","#ff0606","#ff0404","#ff0101","#ff0000"]},"id":"10259","type":"LinearColorMapper"},{"attributes":{"align":null,"below":[{"id":"10192"}],"center":[{"id":"10195"},{"id":"10199"}],"left":[{"id":"10196"}],"margin":null,"min_border_bottom":10,"min_border_left":10,"min_border_right":10,"min_border_top":10,"plot_height":300,"plot_width":700,"renderers":[{"id":"10219"}],"right":[{"id":"10222"}],"sizing_mode":"fixed","title":{"id":"10184"},"toolbar":{"id":"10206"},"toolbar_location":null,"x_range":{"id":"10180"},"x_scale":{"id":"10188"},"y_range":{"id":"10181"},"y_scale":{"id":"10190"}},"id":"10183","subtype":"Figure","type":"Plot"},{"attributes":{"data_source":{"id":"10260"},"glyph":{"id":"10263"},"hover_glyph":null,"muted_glyph":null,"nonselection_glyph":{"id":"10264"},"selection_glyph":null,"view":{"id":"10266"}},"id":"10265","type":"GlyphRenderer"},{"attributes":{},"id":"10243","type":"BasicTicker"},{"attributes":{"data":{"dh":[4.599999999999994],"dw":[8.099999999999994],"image":[{"__ndarray__":"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","dtype":"float32","shape":[46,81]}],"x":[-82.05],"y":[44.45]},"selected":{"id":"10307"},"selection_policy":{"id":"10393"}},"id":"10306","type":"ColumnDataSource"},{"attributes":{"bar_line_color":{"value":"black"},"color_mapper":{"id":"10305"},"formatter":{"id":"10391"},"label_standoff":8,"location":[0,0],"major_tick_line_color":"black","ticker":{"id":"10313"}},"id":"10314","type":"ColorBar"},{"attributes":{"axis":{"id":"10334"},"dimension":1,"grid_line_color":null,"ticker":null},"id":"10337","type":"Grid"},{"attributes":{"color_mapper":{"id":"10259"},"dh":{"field":"dh","units":"data"},"dw":{"field":"dw","units":"data"},"global_alpha":0.1,"image":{"field":"image"},"x":{"field":"x"},"y":{"field":"y"}},"id":"10264","type":"Image"},{"attributes":{},"id":"10261","type":"Selection"},{"attributes":{},"id":"10292","type":"SaveTool"},{"attributes":{},"id":"10294","type":"WheelZoomTool"},{"attributes":{},"id":"10383","type":"UnionRenderers"},{"attributes":{"data":{"dh":[4.599999999999994],"dw":[8.099999999999994],"image":[{"__ndarray__":"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","dtype":"float32","shape":[46,81]}],"x":[-82.05],"y":[44.45]},"selected":{"id":"10215"},"selection_policy":{"id":"10373"}},"id":"10214","type":"ColumnDataSource"},{"attributes":{},"id":"10289","type":"BasicTicker"},{"attributes":{},"id":"10338","type":"SaveTool"},{"attributes":{},"id":"10234","type":"LinearScale"},{"attributes":{"toolbar":{"id":"10407"},"toolbar_location":"above"},"id":"10408","type":"ToolbarBox"},{"attributes":{"data_source":{"id":"10352"},"glyph":{"id":"10355"},"hover_glyph":null,"muted_glyph":null,"nonselection_glyph":{"id":"10356"},"selection_glyph":null,"view":{"id":"10358"}},"id":"10357","type":"GlyphRenderer"},{"attributes":{"axis":{"id":"10196"},"dimension":1,"grid_line_color":null,"ticker":null},"id":"10199","type":"Grid"},{"attributes":{"axis_label":"longitude (degrees_east)","bounds":"auto","formatter":{"id":"10317"},"major_label_orientation":"horizontal","ticker":{"id":"10285"}},"id":"10284","type":"LinearAxis"},{"attributes":{"axis_label":"latitude (degrees_north)","bounds":"auto","formatter":{"id":"10365"},"major_label_orientation":"horizontal","ticker":{"id":"10335"}},"id":"10334","type":"LinearAxis"},{"attributes":{},"id":"10307","type":"Selection"},{"attributes":{},"id":"10403","type":"UnionRenderers"},{"attributes":{"children":[{"id":"10179"},{"id":"10409"},{"id":"10698"}],"margin":[0,0,0,0],"name":"Row01967","tags":["embedded"]},"id":"10178","type":"Row"},{"attributes":{},"id":"10273","type":"BasicTickFormatter"},{"attributes":{},"id":"10335","type":"BasicTicker"},{"attributes":{"callback":null,"renderers":[{"id":"10265"}],"tags":["hv_created"],"tooltips":[["longitude (degrees_east)","$x"],["latitude (degrees_north)","$y"],["t2m","@image"]]},"id":"10228","type":"HoverTool"},{"attributes":{},"id":"10188","type":"LinearScale"},{"attributes":{},"id":"10328","type":"LinearScale"},{"attributes":{},"id":"10353","type":"Selection"},{"attributes":{"toolbars":[{"id":"10206"},{"id":"10252"},{"id":"10298"},{"id":"10344"}],"tools":[{"id":"10182"},{"id":"10200"},{"id":"10201"},{"id":"10202"},{"id":"10203"},{"id":"10204"},{"id":"10228"},{"id":"10246"},{"id":"10247"},{"id":"10248"},{"id":"10249"},{"id":"10250"},{"id":"10274"},{"id":"10292"},{"id":"10293"},{"id":"10294"},{"id":"10295"},{"id":"10296"},{"id":"10320"},{"id":"10338"},{"id":"10339"},{"id":"10340"},{"id":"10341"},{"id":"10342"}]},"id":"10407","type":"ProxyToolbar"},{"attributes":{},"id":"10271","type":"BasicTickFormatter"},{"attributes":{"color_mapper":{"id":"10305"},"dh":{"field":"dh","units":"data"},"dw":{"field":"dw","units":"data"},"global_alpha":0.1,"image":{"field":"image"},"x":{"field":"x"},"y":{"field":"y"}},"id":"10310","type":"Image"},{"attributes":{"axis_label":"longitude (degrees_east)","bounds":"auto","formatter":{"id":"10225"},"major_label_orientation":"horizontal","ticker":{"id":"10193"}},"id":"10192","type":"LinearAxis"},{"attributes":{"bar_line_color":{"value":"black"},"color_mapper":{"id":"10351"},"formatter":{"id":"10401"},"label_standoff":8,"location":[0,0],"major_tick_line_color":"black","ticker":{"id":"10359"}},"id":"10360","type":"ColorBar"},{"attributes":{},"id":"10190","type":"LinearScale"},{"attributes":{"bottom_units":"screen","fill_alpha":0.5,"fill_color":"lightgrey","left_units":"screen","level":"overlay","line_alpha":1.0,"line_color":"black","line_dash":[4,4],"line_width":2,"render_mode":"css","right_units":"screen","top_units":"screen"},"id":"10297","type":"BoxAnnotation"},{"attributes":{},"id":"10391","type":"BasicTickFormatter"},{"attributes":{"data_source":{"id":"10306"},"glyph":{"id":"10309"},"hover_glyph":null,"muted_glyph":null,"nonselection_glyph":{"id":"10310"},"selection_glyph":null,"view":{"id":"10312"}},"id":"10311","type":"GlyphRenderer"},{"attributes":{"color_mapper":{"id":"10259"},"dh":{"field":"dh","units":"data"},"dw":{"field":"dw","units":"data"},"image":{"field":"image"},"x":{"field":"x"},"y":{"field":"y"}},"id":"10263","type":"Image"},{"attributes":{"callback":null,"renderers":[{"id":"10311"}],"tags":["hv_created"],"tooltips":[["longitude (degrees_east)","$x"],["latitude (degrees_north)","$y"],["t2m","@image"]]},"id":"10274","type":"HoverTool"},{"attributes":{"overlay":{"id":"10205"}},"id":"10203","type":"BoxZoomTool"},{"attributes":{"axis_label":"latitude (degrees_north)","bounds":"auto","formatter":{"id":"10319"},"major_label_orientation":"horizontal","ticker":{"id":"10289"}},"id":"10288","type":"LinearAxis"},{"attributes":{},"id":"10193","type":"BasicTicker"},{"attributes":{},"id":"10393","type":"UnionRenderers"},{"attributes":{"axis_label":"longitude (degrees_east)","bounds":"auto","formatter":{"id":"10363"},"major_label_orientation":"horizontal","ticker":{"id":"10331"}},"id":"10330","type":"LinearAxis"},{"attributes":{"color_mapper":{"id":"10351"},"dh":{"field":"dh","units":"data"},"dw":{"field":"dw","units":"data"},"global_alpha":0.1,"image":{"field":"image"},"x":{"field":"x"},"y":{"field":"y"}},"id":"10356","type":"Image"},{"attributes":{"axis_label":"latitude (degrees_north)","bounds":"auto","formatter":{"id":"10227"},"major_label_orientation":"horizontal","ticker":{"id":"10197"}},"id":"10196","type":"LinearAxis"},{"attributes":{"axis":{"id":"10238"},"grid_line_color":null,"ticker":null},"id":"10241","type":"Grid"}],"root_ids":["10178"]},"title":"Bokeh Application","version":"2.0.1"}};
  var render_items = [{"docid":"985211b5-b297-4789-9667-5350fedd51ee","root_ids":["10178"],"roots":{"10178":"701dd0aa-3b0c-4e8a-88db-590cf763f2fb"}}];
  root.Bokeh.embed.embed_items_notebook(docs_json, render_items);
  }
if (root.Bokeh !== undefined) {
    embed_document(root);
  } else {
    var attempts = 0;
    var timer = setInterval(function(root) {
      if (root.Bokeh !== undefined) {
        clearInterval(timer);
        embed_document(root);
      } else if (document.readyState == "complete") {
        attempts++;
        if (attempts > 100) {
          clearInterval(timer);
          console.log("Bokeh: ERROR: Unable to run BokehJS code because BokehJS library is missing");
        }
      }
    }, 10, root)
  }
})(window);</script>




```python

```
