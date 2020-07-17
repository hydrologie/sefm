import xarray as xr
import os
from retrying import retry


@retry(wait_random_min=2000, wait_random_max=3000,stop_max_attempt_number=10)
def reduce_netcdf(files, output_path, key, year):
    ds = xr.open_mfdataset(files, combine='by_coords', parallel=True).load()
    print(year)
    ds = ds.rename({'lat':'latitude',
                    'lon':'longitude'})
    ds.coords['longitude'] = (ds.coords['longitude'] + 180) % 360 - 180
    ds = ds.sortby(ds.longitude)
    ds.to_netcdf(os.path.join(output_path,'{}.{}.nc'.format(key,year)))


@retry(wait_random_min=2000, wait_random_max=3000,stop_max_attempt_number=10)
def reduce_netcdf_all(files, output_path):
    ds = xr.open_mfdataset(files, combine='by_coords', parallel=True)
    ds = ds.rename({'lat':'latitude',
                    'lon':'longitude'})
    ds.coords['longitude'] = (ds.coords['longitude'] + 180) % 360 - 180
    ds = ds.sortby(ds.longitude)
    ds.to_netcdf(os.path.join(output_path,'pressure-levels.nc'))